---
topic: Using Version Control
trigger: Read before committing to Git repository.
version: 1.0.0
---

# Using Version Control

## Committing Work

Commit often, doing so when one of these conditions is met:

1. An individual step of an ongoing implementation plan is complete.
2. The work just done is clearly separate from the work ahead.
3. The current state is a good checkpoint to return to in the future via checkout.

## Commit Messages

Good commit messages are one-liners with a concise description of the applied changes. Avoid unnecessary prose, attributions or meta-commentary.

Follow the commit message style of the project so far, including use of verbs/nouns/adjectives/voice and things like prefix or tagging strategies. If unsure, check the latest in the git log to adapt.


## Important: Using Git Commands

- Call `git` commands on their own line, rather than chaining them by doing `other-command && git add` or `other-command && git commit`.

Bad:
```
git add file && git commit -m "Add some file"
```

Good:
```
git add file
git commit -m "Add some file"
```

