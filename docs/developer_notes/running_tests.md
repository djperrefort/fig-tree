# Running Tests

Fig-Tree is built as a collection of applications that work together to form a cohesive front-end interface.
In addition to testing each application individually, Fig-Tree also includes tests for the overall rendered front-end.

The entire test suite can be executed using the Fig-Tree management command listed below.
Instructions for running subsets of tests are provided in later sections.

```bash
fig-tree-manage test
```

!!! note

    All testing commands in this document support the `--parallel auto` option to run tests in parallel.
    The `auto` feature will automatically run one test process for each available processor core.

## Unit Tests

Unit tests are used to verify behavior for discrete units of code (functions, methods, classes, etc.).
These tests specifically target backend systems and utilities, and do not cover front end functionality.

Each Fig-Tree application includes a dedicated set of unit tests located in the same directory as the parent application.
Unit tests for one or more applications can be executed by specifying the application directory:

```bash
# Execute unit tests for the signup app
fig-tree-manage test fig_tree/apps/signup

# Execute unit tests for the signup and authentication apps
fig-tree-manage test fig_tree/apps/signup fig_tree/tests/authentication
```

Similarly, unit tests for all applications are executed running the following command:

```bash
fig-tree-manage test fig_tree/apps 
```

## Function Tests

Function tests are used to evaluate the functionality of application front-ends.
These tests use a web driver to interact with rendered web pages and monitor the resulting behavior.
Tests in this category do not cover back end functionality.

Function tests are stored in the `fig_tree/tests` directory.
At first glance, the subdirectory structure is similar to that of the unit tests.
However, instead of being organized to mimic the structure of individual applications, function tests are organized to reflect the structure of the rendered Fig-Tree website.
The resulting test organization is similar, but not identical.

The full set of function tests can be executed using the following command:

```bash
fig-tree-manage test fig_tree/tests 
```

A specific set of function tests can be executed by specifying the test subdirectory:

```bash
fig-tree-manage test fig_tree/apps/signup fig_tree/tests/authentication 
```
