# Git Branches

## What is a Branch?

In Git, a **branch** is a separate path or workspace where you can work on new ideas, bug fixes, or features without disturbing the main project line. 

Think of your project as a main notebook (often named `main` or `master`) containing your polished, production-ready work. When you want to experiment or add something new, you create a new branch (a separate draft). 

- **If it works:** You can merge it back into the main notebook.
- **If it doesn't:** You can simply discard or delete the branch without affecting your primary codebase.

> 💡 **Analogy & Example**
> Imagine writing a story. The `main` branch is your final draft—neat and ready to share. 
> 
> When you want to test an alternative ending, you create a new branch—a separate draft where you can write and revise freely without altering your original story. Once you are happy with the new ending, you **merge** it back into the main draft.

---

## Commands Reference

| Command | Description |
| :--- | :--- |
| `git branch` | Lists all local branches in your repository. |
| `git branch <name>` | Creates a new branch with the specified name. |
| `git branch -d <name>` | Safely deletes the specified branch (fails if unmerged). |
| `git branch -D <name>` | Force deletes the specified branch regardless of merge status. |
| `git checkout <branch>` | Switches your working tree to the specified branch. |
| `git checkout -b <new-branch>` | Creates a new branch and switches to it in a single step. |
| `git merge <branch>` | Merges changes from the specified branch into your current active branch. |
| `git merge --abort` | Aborts the current merge process and restores the pre-merge state (used during conflict resolution). |