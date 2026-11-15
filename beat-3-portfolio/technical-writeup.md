# Meeting Copilot

## Overview

Meeting Copilot is uh Hermes plugin and Hermes is a open source software where you can plug and play your own AI. Um, uh I made Meeting Copilot because I was, for example, um, in a meeting and sometimes I forget about the stuff I've done or like the stuff um my teammate done. Um, with the Meeting Copilot, um, the AI is able to listen in and help you out by uh checking your previous session and previous messages as well as online. So it's like a uh someone that helps you um answer questions and provide technical knowledge as well as a help with um technical depth and technical um uh knowledge that's missing

I basically just tell the AI what's missing, what I need it to be, what um, what is my inspiration, in this time I told it to use uh Cluely and Meetily for inspiration and then I'm also asking it to um, help me with um, the UI UX designing it um, uh, just making it uh, usable

I added some test and then the maintainer approved it.

https://github.com/NousResearch/hermes-agent/pull/152088

## What happened

### My design decisions

a lot of the UI UX have a lot of um, uh text that's unnecessary. Um, I also uh I like the way um the transcript look in some of the uh other inspiration, so I had to change the um the transcript look, the UI UX, and then the overall user experience, I make sure to um adjust it to something that I like. And also, I make sure to check Hermes's own rules and guidelines, um, so that the plugin can be accepted and um, published to the uh uh marketplace

### Cross-platform challenges

just making the uh cross platform work, I want it to work both in Mac and Windows and the listening sometimes not working in either one whenever I updated one or the other. Um, I also um, was struggling with uh some of the uh UI UX and the overall like um CI/CD because I was trying to see when it's update, I want it to update on both my Mac and Windows device and see the up changes but I was unable to see the changes uh after I merged it, so those are some of the struggle

### Review feedback

the maintainer asked me to make sure the audio usage doesn't actually expose any credentials than it needed

Review excerpt — `teknium1`, `CHANGES_REQUESTED`; [original review](https://github.com/NousResearch/hermes-agent/pull/152088#pullrequestreview-5838935445):

> The audio worker gets the whole environment minus a denylist (https://github.com/adam4788/meeting-copilot/blob/eb7d4cdac46260e7b1cd9629ce548db5aa8d0d9f/macos_audio.py#L144-L149, spawned at https://github.com/adam4788/meeting-copilot/blob/eb7d4cdac46260e7b1cd9629ce548db5aa8d0d9f/macos_audio.py#L268-L270), so tokens like `TELEGRAM_BOT_TOKEN`, `SLACK_BOT_TOKEN`, `GITHUB_TOKEN`, `HF_TOKEN` and `AWS_SECRET_ACCESS_KEY` still reach third-party compiled wheels and the Swift helper.

### Revision and verification

I disabled the automatic use of Hugging Face token

Before — `worker_env`, [runtime eb7d4cda](https://github.com/adam4788/meeting-copilot/blob/eb7d4cdac46260e7b1cd9629ce548db5aa8d0d9f/macos_audio.py#L144-L152):

```python
def worker_env(provider='local'):
    """Hermetic env for the isolated worker: never inherit the launcher's
    PYTHONPATH/PYTHONHOME (e.g. Hermes's own 3.14 site-packages), which would
    shadow the audio-runtime's 3.12 packages and break model loading."""
    env = {k: v for k, v in os.environ.items()
           if k not in ('PYTHONPATH', 'PYTHONHOME', 'MODEL_API_KEY', 'HERMES_LAUNCHD_LABEL') and not k.endswith(('_API_KEY', '_ACCESS_TOKEN', '_AUTH_TOKEN', '_SECRET_KEY'))}
    return env
```

After — `worker_env`, [runtime 0cb8cfea](https://github.com/adam4788/meeting-copilot/blob/0cb8cfeaa03115c7738007ce39c345a120efc834/macos_audio.py#L144-L165):

```python
def worker_env(provider='local'):
    """Pass only named OS/locale and public-model cache settings to workers.

    Never inherit host credentials or Python/dynamic-loader configuration.
    Meta credentials use the separate, request-scoped stdin handoff. Keep model
    settings explicit: HF_HUB_* can contain credentials and is not a safe prefix.
    """
    allowed = {
        'PATH', 'HOME', 'USER', 'LOGNAME', 'TMPDIR', 'LANG',
        'LC_ALL', 'LC_CTYPE', 'LC_MESSAGES', 'LC_NUMERIC', 'LC_TIME',
        'LC_COLLATE', 'LC_MONETARY', 'LC_PAPER', 'LC_NAME', 'LC_ADDRESS',
        'LC_TELEPHONE', 'LC_MEASUREMENT', 'LC_IDENTIFICATION',
        '__CF_USER_TEXT_ENCODING',
    }
    if provider == 'local':
        allowed.update({'HF_HOME', 'HF_HUB_CACHE', 'HF_HUB_OFFLINE'})
    env = {key: value for key, value in os.environ.items() if key in allowed}
    # Public Whisper weights need no account token, including cached logins.
    env['HF_HUB_DISABLE_IMPLICIT_TOKEN'] = '1'
    return env
```

Historical CI — [Ubuntu / Python 3.11 job](https://github.com/adam4788/meeting-copilot/actions/runs/42830034513/job/129877355614), source head `f5f038ecabf28dfb161f9a9fc8166392e34dcac5`. GitHub transport prefixes removed; output messages unchanged:

```text
test_local_worker_scrubs_provider_credentials_and_never_resolves_meta (tests.test_credential_runtime.CredentialRuntimeTests.test_local_worker_scrubs_provider_credentials_and_never_resolves_meta) ... ok
test_meta_worker_environment_contains_no_provider_key (tests.test_credential_runtime.CredentialRuntimeTests.test_meta_worker_environment_contains_no_provider_key) ... ok
test_worker_env_is_an_exact_allowlist_for_each_provider (tests.test_macos_audio.GatewayTests.test_worker_env_is_an_exact_allowlist_for_each_provider) ... ok
test_worker_spawn_uses_hermetic_env (tests.test_macos_audio.GatewayTests.test_worker_spawn_uses_hermetic_env) ... ok
Ran 925 tests in 75.319s
OK (skipped=21)
# tests 281
# pass 281
# fail 0
```

### Outcome

I added some test and then the maintainer approved it.

Approval — `teknium1`, [original approval](https://github.com/NousResearch/hermes-agent/pull/152088#pullrequestreview-5851300687):

> Re-reviewed at the current pin: the blocking asks from our earlier review are fixed. Approving for the catalog; we added any disclosure line and version floor as a merge chore. Thanks!

PR metadata — [main catalog submission](https://github.com/NousResearch/hermes-agent/pull/152088); Arizona merge time `2026-11-10 17:31:43 MST`:

```json
{
  "url": "https://github.com/NousResearch/hermes-agent/pull/152088",
  "state": "MERGED",
  "mergedAt": "2026-11-11T00:31:43Z"
}
```

## Limitations and what's next

just making it actually work seamlessly, I feel like it's not as seamless as I thought it would be. Um, you still have to do clicks, set up the transcription, um, set up the other, uh, models. Um, so I wanted in the future to be just people just, um, install the plugin and then they can just start using it using all the default Hermes but right now I'm still working on that.
