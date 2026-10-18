"""Metadata-only ranking for issue-scout; no network or model calls."""

import re
from datetime import datetime, timedelta


def rank(batches, captured_at, require_five=False):
    unique, conflicts = {}, []
    total = 0
    for query, records in batches:
        for record in records:
            total += 1
            url = record['url']
            if url not in unique:
                unique[url] = dict(record, queries=[query])
            else:
                first = unique[url]
                diff = {key: [first.get(key), value] for key, value in record.items()
                        if first.get(key) != value}
                if diff: conflicts.append(dict(url=url, query=query, fields=diff))
                first['queries'] = sorted(set(first['queries'] + [query]))
    kept, dropped = [], []
    for record in unique.values():
        # Index every required field: omitted API evidence is never an empty value.
        for key in ('title','updatedAt','commentsCount','labels','assignees','state','isPullRequest','repository'):
            record[key]
        reasons = []
        if record['state'].lower() != 'open': reasons.append('not-open')
        if record['isPullRequest']: reasons.append('pull-request')
        if record['assignees']: reasons.append('assigned')
        if datetime.fromisoformat(record['updatedAt'].replace('Z','+00:00')) < captured_at-timedelta(days=90):
            reasons.append('updated-more-than-90-days-ago')
        if reasons: dropped.append(dict(url=record['url'], reasons=reasons))
        else: kept.append(record)
    keywords = re.compile(r'\b(json|documents?|pdf|ingestion|parser|parsing|llm|agents?|tools?)\b', re.I)
    def order(record):
        labels = {label['name'].lower() for label in record['labels']}
        return (not bool(keywords.search(record['title'])), 'bug' not in labels,
                'good first issue' not in labels, record['commentsCount'],
                -datetime.fromisoformat(record['updatedAt'].replace('Z','+00:00')).timestamp(), record['url'])
    kept.sort(key=order)
    if require_five and len(kept) < 5: raise ValueError('Fewer than five survivors: revise strategy')
    return dict(counts=dict(fetched=total, unique=len(unique), duplicates=total-len(unique),
                            dropped=len(dropped), survivors=len(kept)),
                conflicts=conflicts, dropped=dropped, ranked=kept, top_five=kept[:5])
