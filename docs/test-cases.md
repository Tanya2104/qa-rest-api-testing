# Detailed Test Cases

> Execution baseline: local clean SQLite database. “Passed” actual results were recorded by the final automated regression run.

## TC-001 — Create a user
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /users. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `valid user`
- **Expected Result:** 201; user returned without password.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-002 — Reject duplicate email
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST same user twice. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `same email`
- **Expected Result:** 409 with detail.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-003 — Reject invalid email
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /users. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `email=bad`
- **Expected Result:** 422.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-004 — Age lower boundary
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /users. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `age=18`
- **Expected Result:** 201.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-005 — Age below boundary
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /users. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `age=17`
- **Expected Result:** 422.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-006 — Age upper boundary
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /users. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `age=100`
- **Expected Result:** 201.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-007 — Age above boundary
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /users. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `age=101`
- **Expected Result:** 422.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-008 — Reject short password
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /users. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `password=short`
- **Expected Result:** 422.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-009 — Read unknown user
- **Priority:** Medium
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. GET /users/999. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `id=999`
- **Expected Result:** 404.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-010 — Update user
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. PUT existing user. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `new valid fields`
- **Expected Result:** 200 and persisted fields.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-011 — Delete user
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. DELETE existing user. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `existing id`
- **Expected Result:** 204; subsequent GET is 404.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-012 — Create product
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /products. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `price=25.5, stock=10`
- **Expected Result:** 201.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-013 — Reject zero price
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /products. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `price=0`
- **Expected Result:** 422.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-014 — Reject negative price
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /products. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `price=-1`
- **Expected Result:** 422.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-015 — Accept zero stock
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /products. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `stock=0`
- **Expected Result:** 201.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-016 — Reject negative stock
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /products. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `stock=-1`
- **Expected Result:** 422.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-017 — Update product
- **Priority:** Medium
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. PUT existing product. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `stock=20`
- **Expected Result:** 200 and stock=20.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-018 — Delete product
- **Priority:** Medium
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. DELETE product. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `existing id`
- **Expected Result:** 204.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-019 — Read unknown product
- **Priority:** Medium
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. GET /products/999. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `id=999`
- **Expected Result:** 404.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-020 — Create order
- **Priority:** Critical
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /orders. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `valid IDs, quantity=2`
- **Expected Result:** 201 and status=created.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-021 — Calculate order total
- **Priority:** Critical
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. Order 3 units at 25.50. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `quantity=3`
- **Expected Result:** total_price=76.50.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-022 — Reduce product stock
- **Priority:** Critical
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. Create quantity-3 order. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `stock initially 10`
- **Expected Result:** product stock becomes 7.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-023 — Reject zero quantity
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /orders. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `quantity=0`
- **Expected Result:** 422.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-024 — Reject excess stock
- **Priority:** Critical
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /orders. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `quantity=11, stock=10`
- **Expected Result:** 400 Insufficient stock.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-025 — Reject unknown user in order
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /orders. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `user_id=999`
- **Expected Result:** 404.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-026 — Reject unknown product in order
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /orders. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `product_id=999`
- **Expected Result:** 404.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-027 — Delete order
- **Priority:** Medium
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. DELETE existing order. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `existing id`
- **Expected Result:** 204.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-028 — Successful login
- **Priority:** Critical
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /login. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `valid credentials`
- **Expected Result:** 200 bearer test-token.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-029 — Reject invalid password
- **Priority:** Critical
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /login. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `wrong password`
- **Expected Result:** 401.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed

## TC-030 — Reject missing login field
- **Priority:** High
- **Preconditions:** API is running; clean database; create prerequisite entities where stated.
- **Steps:** 1. POST /login without password. 2. Inspect status, JSON body, and persisted state.
- **Test Data:** `email only`
- **Expected Result:** 422.
- **Actual Result:** Matched expected result in automated regression.
- **Status:** Passed
