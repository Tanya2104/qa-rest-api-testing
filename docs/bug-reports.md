# Bug Reports (Resolved Regression History)

## BUG-001 — Age 18 rejected
**Environment:** Local FastAPI/SQLite · **Severity:** Major · **Priority:** High  
**Preconditions:** API running. **Steps to Reproduce:** POST `/users` with age 18 and otherwise valid data.  
**Actual Result:** 422 due to `age > 18`. **Expected Result:** 201 because 18 is inclusive. **Status:** Fixed; BVA regression added.

## BUG-002 — Duplicate email returns server error
**Environment:** Local API · **Severity:** Major · **Priority:** High  
**Preconditions:** Existing user. **Steps to Reproduce:** Create another user with the same email.  
**Actual Result:** 500 database exception. **Expected Result:** 409 JSON `Email already exists`. **Status:** Fixed; pre-insert uniqueness check added.

## BUG-003 — Order total ignores quantity
**Environment:** Local API · **Severity:** Critical · **Priority:** High  
**Preconditions:** Product price 25.50, stock 10. **Steps to Reproduce:** Order quantity 3.  
**Actual Result:** total_price 25.50. **Expected Result:** 76.50. **Status:** Fixed; multiplication/rounding regression added.

## BUG-004 — Stock not reduced after order
**Environment:** Local API · **Severity:** Critical · **Priority:** High  
**Preconditions:** Stock 10. **Steps to Reproduce:** Create quantity-3 order; GET product.  
**Actual Result:** Stock remains 10. **Expected Result:** Stock is 7. **Status:** Fixed in the order transaction.

## BUG-005 — Missing order returned 200/null
**Environment:** Local API · **Severity:** Minor · **Priority:** Medium  
**Preconditions:** ID 999 does not exist. **Steps to Reproduce:** GET `/orders/999`.  
**Actual Result:** 200 with null body. **Expected Result:** 404 JSON `Order not found`. **Status:** Fixed; regression added.
