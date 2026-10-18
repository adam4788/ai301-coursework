"""Deterministic ranker regression tests; fixture records are tests, not scan evidence."""
import unittest
from datetime import datetime, timezone

class RankingTest(unittest.TestCase):
    def test_duplicate_urls_keep_first_metadata_and_union_queries(self):
        import rank_candidates
        r = dict(url='https://github.com/test/repo/issues/1', title='JSON bug',
                 updatedAt='2026-10-17T00:00:00Z', commentsCount=2, labels=[],
                 assignees=[], state='open', isPullRequest=False, repository={'nameWithOwner':'test/repo'})
        result = rank_candidates.rank([('Q1', [r]), ('Q2', [dict(r, commentsCount=3)])],
                                      datetime(2026,10,17,tzinfo=timezone.utc))
        self.assertEqual(result['counts']['unique'], 1)
        self.assertEqual(result['ranked'][0]['queries'], ['Q1','Q2'])
        self.assertEqual(result['ranked'][0]['commentsCount'], 2)
        self.assertEqual(len(result['conflicts']), 1)

    def test_metadata_filters_and_total_order(self):
        import rank_candidates
        base = dict(title='Plain', updatedAt='2026-10-17T00:00:00Z', commentsCount=0,
                    labels=[], assignees=[], state='open', isPullRequest=False,
                    repository={'nameWithOwner':'test/repo'})
        def item(n, **kw): return dict(base, url=f'https://github.com/test/repo/issues/{n}', **kw)
        records = [item('plain'), item('json-old', title='JSON parser', commentsCount=1, updatedAt='2026-10-16T00:00:00Z'),
                   item('json-new', title='JSON parser', commentsCount=1),
                   item('bug', title='Agent tool', labels=[{'name':'bug'}], commentsCount=8),
                   item('assigned', assignees=[{'login':'taken'}]), item('closed', state='closed'),
                   item('pr', isPullRequest=True), item('stale', updatedAt='2026-07-18T00:00:00Z'),
                   item('boundary', updatedAt='2026-07-19T00:00:00Z')]
        result = rank_candidates.rank([('Q1', records)], datetime(2026,10,17,tzinfo=timezone.utc))
        self.assertEqual([r['url'].split('/')[-1] for r in result['ranked']],
                         ['bug','json-new','json-old','plain','boundary'])
        self.assertEqual(result['counts']['dropped'], 4)
        self.assertEqual(len(result['top_five']), 5)
        again = rank_candidates.rank([('Q1', list(reversed(records)))], datetime(2026,10,17,tzinfo=timezone.utc))
        self.assertEqual(result['ranked'], again['ranked'])
        with self.assertRaises(ValueError):
            rank_candidates.rank([('Q1', records[:-1])], datetime(2026,10,17,tzinfo=timezone.utc), require_five=True)
        with self.assertRaises(KeyError):
            rank_candidates.rank([('Q1', [{'url':'missing-fields'}])], datetime(2026,10,17,tzinfo=timezone.utc))

if __name__ == '__main__': unittest.main()
