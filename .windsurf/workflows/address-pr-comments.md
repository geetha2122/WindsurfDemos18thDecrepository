---
description: 
auto_execution_mode: 1
---

# address-pr-comments
> Address PR comments and update code accordingly.

## Steps
1. Checkout the PR branch: `gh pr checkout {{pr_number}}`
2. List open comments and summarize changes.
3. Edit files to address each comment; include tests for fixes.
4. Run unit tests: `python -m pytest`
5. Commit: `git commit -am "Address PR comments (#{{pr_number}})"`
6. Push: `git push`
7. Post a summary reply per comment with diffs.