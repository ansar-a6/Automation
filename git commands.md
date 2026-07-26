# Git Commands

## Basic Overview
prints each commit on a single line.
Git commands allow developers to configure their working environment, retrieve remote repositories, record software changes (commits), inspect revision history, and safely undo changes.

- **Configuration:** Set up user identity per repository or globally across your machine.
- **Repository Operations:** Clone remote repositories or fetch updates without modifying local working files.
- **Committing Changes:** Record staged snapshots with single or multi-line messages.
- **History & Reverting:** Inspect line-by-line diffs and create inverse commits to safely roll back changes.

> 💡 **CLI vs GUI Commit Messages**
> Using multiple `-m` flags (e.g., `git commit -m "Heading" -m "Body"`) allows you to structure a title and detailed body directly from the CLI (terminal). 
> 
> Note that this syntax is specific to command-line interfaces; GUI code editors or editor extensions (like VS Code) usually rely on their integrated commit text area rather than multiple command flags.

---

## Commands Reference

| Command | Description |
| :--- | :--- |
| `git config user.name '<yourname>'` | Sets the author name for the current local repository. |
| `git config user.email '<youremail>'` | Sets the author email for the current local repository. |
| `git config --global user.name '<yourname>'` | Sets the default author name globally across all repositories on your system. |
| `git clone '<link>'` | Clones a remote repository into a new local directory. |
| `git fetch` | Downloads commits, refs, and files from a remote repository without merging into your working files. |
| `git commit -m '<message>'` | Commits staged changes with a single summary message. |
| `git commit -m '<heading>' -m '<body>'` | Commits staged changes with a separate heading (title) and detailed body description. |
| `git commit -m '<heading>' -m '<body>' -m '<short-explain>'` | Commits staged changes using multiple `-m` flags for multi-paragraph notes (CLI only). |
| `git commit -a -m '<message>'` | Automatically stages modified tracked files and commits them with a message. |
| `git commit -a -m '<heading>' -m '<body>'` | Automatically stages modified tracked files and commits them with a heading and body message. |
| `git log -p` | Displays commit history along with the detailed patch/diff for each commit. |
| `git log -p -2` | Displays commit history along with diffs restricted to the 2 most recent commits. |
| `git revert HEAD` | Creates a new commit that undoes the changes introduced by the most recent commit (`HEAD`). |
| `git revert <id>` | Creates a new commit that undoes changes introduced by a specific commit hash/ID. |
