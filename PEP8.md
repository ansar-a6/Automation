# Using PEP 8 Style in a Git Repository

## Start Here

PEP 8 is a style guide for Python code. A style guide gives a team shared
rules for writing code, for example how to indent code, name variables, and
separate functions. When everyone follows the same rules, code is easier to
read, review, and change.

Git does not format Python code. Git saves versions of files. We add style
tools to a Git repository so that code can be checked before it is committed
and shared with the team.

This guide shows two different tasks:

1. **Create a new repository with style rules.** Do this once when starting a
   project.
2. **Edit an existing repository that already has style rules.** Do this every
   time you work on a project.

## A Few PEP 8 Rules

These are common Python style rules:

- Indent code with four spaces.
- Use `snake_case` for functions and variables, such as `calculate_total`.
- Use `PascalCase` for class names, such as `OrderSummary`.
- Leave blank lines between functions and classes.
- Use clear, meaningful names.

You do not need to remember every rule. A formatter and linter can help you
apply and check them.

## 1. Create a New Repository with Style Rules

### Create the repository

In a terminal, create a folder, enter it, and start Git:

```bash
mkdir my-python-project
cd my-python-project
git init
```

Create a Python file named `app.py` with a small program:

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Ada")
```

### Install the style tools

Install these tools in your Python environment:

```bash
pip install black flake8 pre-commit
```

- `black` automatically formats Python code.
- `flake8` reports style problems.
- `pre-commit` runs checks automatically before a Git commit.

### Add the configuration files

Create `pyproject.toml` for Black:

```toml
[tool.black]
line-length = 79
```

Create `.flake8` for Flake8:

```ini
[flake8]
max-line-length = 79
extend-ignore = E203, W503
```

Create `.pre-commit-config.yaml` to run the tools before each commit:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.10.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 7.1.1
    hooks:
      - id: flake8
```

Install the hook and run it on all current files:

```bash
pre-commit install
pre-commit run --all-files
```

If Black changes a file, that is normal. Read the changes and save them.

### Make the first commit

Check which files Git will save, then commit them:

```bash
git status
git add app.py pyproject.toml .flake8 .pre-commit-config.yaml
git commit -m "Set up Python style checks"
```

Your new repository now has the same style rules for every contributor.

## 2. Edit a Repository That Already Has Style Rules

When joining or returning to a project, first look for these files in the
repository folder:

- `pyproject.toml` — usually contains formatter settings.
- `.flake8` — contains Flake8 rules.
- `.pre-commit-config.yaml` — lists checks that run before commits.
- `README.md` or `CONTRIBUTING.md` — may describe extra team rules.

Do not replace these files with your own settings unless the team asks you to.
They are shared rules for the project.

### Get the project and install its hooks

If the repository is online, copy it to your computer with `git clone`:

```bash
git clone <repository-url>
cd <repository-folder>
```

Install the project's hooks once on your computer:

```bash
pip install -r requirements.txt
pre-commit install
```

If the project does not have `requirements.txt`, follow the instructions in
its README or ask the team how to install its development tools.

### Edit code and check the style

1. Open the Python file you need to change.
2. Make a small, focused change.
3. Save the file.
4. Format and check it:

```bash
black path/to/file.py
flake8 path/to/file.py
```

Replace `path/to/file.py` with the real file name, for example `black app.py`.

If Flake8 reports a problem, read the message, fix the code, and run the
command again. If Black reformats the file, review the result before you
continue.

### Review and commit your edit

Use Git to see exactly what you changed:

```bash
git status
git diff
```

When the change looks correct, stage and commit it:

```bash
git add path/to/file.py
git diff --staged
git commit -m "Describe the change"
```

The pre-commit hook runs during `git commit`. If it finds a problem or formats
a file, fix or stage the updated file and run the commit command again.

## Quick Checklist

Before every commit, make sure you can answer **yes** to these questions:

- Did I follow the repository's existing style configuration?
- Did I run the formatter and linter?
- Did I review `git diff` before staging files?
- Does my commit contain only the changes I intended to make?

## Questions Beginners Often Ask

### Why use Black, Flake8, and pre-commit?

You do not have to use these tools for Python to run. They help a team keep
its code consistent and catch common style problems before code is shared.

- `black` automatically formats Python code. It can change whitespace, blank
  lines, indentation, and line wrapping, but it is intended not to change what
  the program does.
- `flake8` checks Python files and reports possible style problems. It normally
  does not edit files for you.
- `pre-commit` runs selected checks automatically when you use `git commit`.

Git itself does not understand PEP 8 and does not format code. Git only saves
versions of files. The style tools are separate programs that you choose to
run locally, with a Git hook, or in CI.

### Should style configuration files go in `.gitignore`?

Usually, **no**. Commit shared style configuration files so every contributor
and the CI server uses the same rules. Common examples are:

- `pyproject.toml`
- `.flake8`
- `.pre-commit-config.yaml`

Add personal or generated files to `.gitignore` instead. For example:

```gitignore
.venv/
__pycache__/
.pytest_cache/
.mypy_cache/
```

The virtual environment and cache files are different on each computer and do
not need to be shared. The configuration files are team instructions and do
need to be shared.

### What really happens when style tools are used?

The configuration files do nothing on their own. They only take effect when a
tool reads them.

1. You create or edit a Python file.
2. You run `black app.py`. Black may change only the file's formatting.
3. You run `flake8 app.py`. Flake8 prints style issues that you may need to
   fix.
4. You review the changes with `git diff`, then commit the intended files.
5. Other contributors can install the same tools and get the same results.

If a pre-commit hook is installed, these checks can run automatically during
`git commit`. If CI is configured, the same checks can also run when code is
pushed or a pull request is opened. A team may choose to require passing checks
before a pull request can be merged.
