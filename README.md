# Challenge

This is just a simple example

## Precommit Hooks

We use [pre-commit](https://pre-commit.com/) to enforce e.g. code formatting,
linting and type checking prior to committing to the repository.
The `.pre-commit-config.yaml` in the repository includes all of the requirements.
The required packages must be declared on `pyproject.toml`.

Prior to your first commit you need to run

```zsh
pre-commit install
```

If you want to manually run it on all files without a commit

```zsh
pre-commit run --all-files
```

### Setup environment

#### Poetry virtual env

In order to setup the environment you need to
[download poetry](https://python-poetry.org/docs/) and install it using

```zsh
poetry install
```

After that you need to start the environment. For that you should use:

```zsh
poetry shell
```
