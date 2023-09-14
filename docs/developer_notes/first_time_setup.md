# First-Time Setup

This page provides instructions for setting up a new Python development environment.
In most cases, these steps only need to be performed once.

## Prerequisites

Please ensure the following utilities are pre-installed and properly configured on your system:

- [Conda](https://docs.conda.io/en/latest/) - for managing Python environments
- [Poetry](https://python-poetry.org/) - for managing project dependencies
- [Selenium WebDriver](https://www.selenium.dev/) - optional, but required for locally running function tests

!!! note

    While it is possible to install Poetry in a virtual environment, this can result in unexpected behavior.
    It is strongly recommended that developers install Poetry at the system level.

## Installing Dependencies

To avoid dependency conflicts with other projects, start by creating a new virtual environment:

```bash
conda create -y -n fig-tree python=3.11
conda activate fig-tree
```

After activating the environment, install the necessary Python dependencies using Poetry.
Developers will want to use the `--with` option to install optional dependencies for running tests and building documentation.

```bash
poetry install --with tests docs
```

The Django web framework provides a `manage.py` file for executing administrative tasks.
For convenience, Fig-Tree exposes this utility as the `fig-tree-manage` command-line utility.
If your installation was successful, running the utility will display a list of available subcommands.


```bash
fig-tree-manage
```

## Running Management Commands

Fig-Tree can be configured using any of the available [application settings](../deployment_guide/configuration.md).
Enabling debug mode allows developers to skip most of the required configuration to get up and running quickly.

```bash
export DEBUG=1
```
!!! danger

    **Never** enable debug mode in a production setting.
    See [Configuration and Settings](../deployment_guide/configuration.md) for more details.

When running in debug mode, Fig-Tree will automatically create a SQLite database.
Before launching the application, apply the required database schema.

```bash
fig-tree-manage migrate
```

Once the database is ready, Fig-Tree can be launched via the management utility.

```bash
fig-tree-manage runserver  # Run the application
```

