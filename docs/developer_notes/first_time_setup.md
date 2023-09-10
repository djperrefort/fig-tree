# First Time Setup

## Prerequisites

This project uses the following developer utilities to manage application dependencies.
Please ensure all listed utilities are pre-installed and properly configured on your chosen system.

- [Conda](https://docs.conda.io/en/latest/) - for managing Python environments
- [Poetry](https://python-poetry.org/) - for managing project dependencies

!!! note

    While it is possible to install Poetry within a virtual environment, this practice is discouraged.
    It is strongly recomended developers install Poetry at the system level.

## Installing Dependencies

To avoid dependency conflicts with other projects, start by creating a new virtual environment: 

```bash
conda create -y -n fig-tree python=3.11
conda activate fig-tree
```

Once the environment is active, install the necessary Python dependencies using poetry.
Developers will want to use the `--with` option to install optional dependencies for running tests and building documentation.

```bash
poetry install --with tests docs
```

The Django web framework provides a `manage.py` utility for executing administrative tasks.
For convenience, Fig-Tree exposes this utility as the `fig-tree-manage` command line utility.
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
    See [Configuration and Settings](configuration.md) for more details.

When running in debug mde, Fig-Tree will automatically create a Sqlite database.
Before launching the application, apply the required database schema.

```bash
fig-tree-manage migrate
```

Once the database is ready, Fig-Tree can be launched via the management utility.

```bash
fig-tree-manage runserver  # Run the application
```

