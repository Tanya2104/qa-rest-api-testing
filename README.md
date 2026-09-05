# REST API Testing Portfolio Project

[![Tests](https://img.shields.io/badge/pytest-44%20passed-brightgreen)](#test-results) [![API](https://img.shields.io/badge/FastAPI-1.0.0-009688)](#tested-application)

## Overview
A complete junior QA portfolio project: a small online-store REST API plus functional/negative test assets, automated regression, SQL checks, defect history, and a ready-to-import Postman suite.

## Tested Application
FastAPI service backed by SQLAlchemy and SQLite. It exposes CRUD for **users** and **products**, order creation/read/delete with inventory and calculated totals, and demo login. Interactive OpenAPI documentation is served at `/docs`.

## Testing Scope
HTTP/JSON contracts, positive CRUD flows, validation and boundaries, duplicate and nonexistent resources, authentication, order business rules, persistence, and error responses.

## Technologies
Python · FastAPI · Pydantic · SQLAlchemy · SQLite · pytest · HTTPX · Postman · OpenAPI/Swagger · Git

## Test Documentation
- [Test plan](docs/test-plan.md)
- [60-check checklist](docs/checklist.md)
- [30 detailed test cases](docs/test-cases.md)
- [Resolved bug reports](docs/bug-reports.md)
- [Final test report](docs/test-report.md)

## Test Design Techniques
[Concrete examples](docs/test-design.md) apply equivalence partitioning, boundary value analysis, decision tables, and positive/negative testing to API fields and business rules.

## API Automation
The `tests/` suite contains 44 independent tests organized by users, products, orders, authentication, and cross-cutting validation. A fresh SQLite schema is created for each test.

## Postman
Import both JSON files from `postman/`, select **QA REST API - Local**, and run the collection. Folders cover Users, Products, Orders, Authentication, and Negative Tests; scripts assert status, JSON content type/shape, values, and response time while capturing entity IDs.

## SQL Checks
[Ten practical queries](docs/sql-checks.md) verify records, constraints, orphan relationships, stock, and order totals.

## Project Structure
```text
app/       FastAPI application, schemas, database, routers
tests/     pytest API regression suite
docs/      QA plan, design, cases, checklist, bugs, SQL, report
postman/   importable collection and local environment
```

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Running the Application
```bash
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## Running Tests
```bash
pytest
```

## Test Results
**44 passed, 0 failed** in the final regression run. Five historical defects were fixed; there are no known functional issues in scope.

## Key QA Skills Demonstrated
REST/HTTP and JSON validation · functional and negative testing · test design · boundary analysis · business-rule verification · pytest automation · Postman scripting · OpenAPI review · SQL validation · defect reporting · Git workflow

> **Known limitations:** Authentication intentionally uses plaintext demo passwords and a fixed token. SQLite, concurrency/load, cancellation/stock restoration, security, and production deployment are outside this educational project's scope.
