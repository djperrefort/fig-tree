# Running Tests

Fig-Tree comprises multiple individual applications that collectively form a cohesive front-end interface. 
In addition to testing individual applications, Fig-Tree also includes tests for the overall rendered interface. 
This page provides a high-level overview of the Fig-Tree test suite and instructions for executing individual tests.

For quick reference, the entire test suite can be executed using the Fig-Tree management utility:

```bash
fig-tree-manage test
```

## Unit Tests

Unit tests are a type of software testing that assesses discrete units of code, such as functions, methods, or classes.
These tests are used to verify the behavior of backend systems and utilities.
Front end functionality is **not** covered by unit tests.

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

Function tests are used to evaluate the functionality of application front-ends by simulating user interactions.
For Fig-Tree, these tests rely on the Selenium WebDriver to interact with rendered web pages and monitor the resulting behavior.
Tests in this category do **not** cover back end functionality.

Tests are collectively written under the `fig_tree/tests` directory.
At first glance, the subdirectory structure is similar to that of the unit tests.
However, instead of being organized to mimic the structure of individual applications, function tests are organized to reflect the structure of the rendered Fig-Tree website.
The resulting structures are similar, but not always identical.

The full set of function tests can be executed using th following command:

```bash
fig-tree-manage test fig_tree/tests 
```

A specific set of function tests can be executed by specifying the test subdirectory:

```bash
fig-tree-manage test fig_tree/apps/signup fig_tree/tests/authentication 
```
