# Test Plan — QA Portfolio Shop API

## Objective
Verify that the store REST API satisfies documented CRUD, validation, authentication, inventory, persistence, and error-handling requirements.

## Scope
Users, products, orders, login, OpenAPI contract, HTTP/JSON behavior, and SQLite data integrity.

## Features to be Tested
CRUD operations; input constraints and boundaries; duplicate email; order price/inventory rules; authentication outcomes; response schemas and status codes.

## Features Not to be Tested
Load, security penetration, UI, payment, shipping, production authentication, order cancellation, and cross-browser behavior.

## Test Types
Functional, negative, boundary, API contract, integration, regression, and database testing.

## Test Environment
Local Python 3.11+, FastAPI/Uvicorn, SQLite, HTTPX TestClient; base URL `http://127.0.0.1:8000`.

## Tools
pytest, HTTPX, Postman, Swagger UI/OpenAPI, SQLAlchemy, SQLite, and Git.

## Entry Criteria
Dependencies installed; API starts; database is writable; requirements and OpenAPI endpoints are available.

## Exit Criteria
All 44 automated tests pass; critical/high defects are fixed; documentation and collection match the final API.

## Risks
SQLite differs from production databases; plaintext demo passwords and fixed token are intentionally non-production; concurrent stock updates are not load-tested.
