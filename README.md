# TDD/BDD Final Project – Product Catalogue

This repository contains the final project for the IBM DevOps and Software Engineering Professional Certificate course on Test Driven Development and Behaviour Driven Development.

## Project Structure

```
├── service/
│   └── routes.py          # Flask REST API route handlers
├── tests/
│   ├── factories.py        # factory_boy ProductFactory for fake test data
│   ├── test_models.py      # TDD unit tests for the Product model
│   └── test_routes.py      # TDD unit tests for the REST API routes
└── features/
    ├── products.feature    # BDD Gherkin scenarios
    └── steps/
        ├── load_steps.py   # BDD background data loading step
        └── web_steps.py    # BDD Selenium step definitions
```

## Tech Stack

- Python, Flask, SQLAlchemy
- factory_boy (TDD fake data)
- Behave + Selenium (BDD)
