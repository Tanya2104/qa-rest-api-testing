# API Test Checklist

ID | Area | Check | Expected Result | Status
---|---|---|---|---
CHK-001 | Users | Create valid user | Requirement is satisfied without unexpected side effects | Passed
CHK-002 | Users | List users | Requirement is satisfied without unexpected side effects | Passed
CHK-003 | Users | Get existing user | Requirement is satisfied without unexpected side effects | Passed
CHK-004 | Users | Update all fields | Requirement is satisfied without unexpected side effects | Passed
CHK-005 | Users | Delete user | Requirement is satisfied without unexpected side effects | Passed
CHK-006 | Users | Reject duplicate email | Requirement is satisfied without unexpected side effects | Passed
CHK-007 | Users | Reject malformed email | Requirement is satisfied without unexpected side effects | Passed
CHK-008 | Users | Reject blank name | Requirement is satisfied without unexpected side effects | Passed
CHK-009 | Users | Reject short password | Requirement is satisfied without unexpected side effects | Passed
CHK-010 | Users | Return 404 for unknown ID | Requirement is satisfied without unexpected side effects | Passed
CHK-011 | Products | Create valid product | Requirement is satisfied without unexpected side effects | Passed
CHK-012 | Products | List products | Requirement is satisfied without unexpected side effects | Passed
CHK-013 | Products | Get product | Requirement is satisfied without unexpected side effects | Passed
CHK-014 | Products | Update product | Requirement is satisfied without unexpected side effects | Passed
CHK-015 | Products | Delete product | Requirement is satisfied without unexpected side effects | Passed
CHK-016 | Products | Reject zero price | Requirement is satisfied without unexpected side effects | Passed
CHK-017 | Products | Reject negative price | Requirement is satisfied without unexpected side effects | Passed
CHK-018 | Products | Accept zero stock | Requirement is satisfied without unexpected side effects | Passed
CHK-019 | Products | Reject negative stock | Requirement is satisfied without unexpected side effects | Passed
CHK-020 | Products | Return 404 for unknown ID | Requirement is satisfied without unexpected side effects | Passed
CHK-021 | Orders | Create valid order | Requirement is satisfied without unexpected side effects | Passed
CHK-022 | Orders | List orders | Requirement is satisfied without unexpected side effects | Passed
CHK-023 | Orders | Get order | Requirement is satisfied without unexpected side effects | Passed
CHK-024 | Orders | Delete order | Requirement is satisfied without unexpected side effects | Passed
CHK-025 | Orders | Default status created | Requirement is satisfied without unexpected side effects | Passed
CHK-026 | Orders | Calculate total | Requirement is satisfied without unexpected side effects | Passed
CHK-027 | Orders | Reduce stock | Requirement is satisfied without unexpected side effects | Passed
CHK-028 | Orders | Reject zero quantity | Requirement is satisfied without unexpected side effects | Passed
CHK-029 | Orders | Reject excess quantity | Requirement is satisfied without unexpected side effects | Passed
CHK-030 | Orders | Reject unknown user | Requirement is satisfied without unexpected side effects | Passed
CHK-031 | Authentication | Login with valid credentials | Requirement is satisfied without unexpected side effects | Passed
CHK-032 | Authentication | Reject wrong password | Requirement is satisfied without unexpected side effects | Passed
CHK-033 | Authentication | Reject unknown email | Requirement is satisfied without unexpected side effects | Passed
CHK-034 | Authentication | Reject missing email | Requirement is satisfied without unexpected side effects | Passed
CHK-035 | Authentication | Reject missing password | Requirement is satisfied without unexpected side effects | Passed
CHK-036 | Authentication | Return bearer token | Requirement is satisfied without unexpected side effects | Passed
CHK-037 | Validation | Accept age 18 | Requirement is satisfied without unexpected side effects | Passed
CHK-038 | Validation | Accept age 100 | Requirement is satisfied without unexpected side effects | Passed
CHK-039 | Validation | Reject age 17 | Requirement is satisfied without unexpected side effects | Passed
CHK-040 | Validation | Reject age 101 | Requirement is satisfied without unexpected side effects | Passed
CHK-041 | Validation | Reject malformed JSON | Requirement is satisfied without unexpected side effects | Passed
CHK-042 | Validation | Trim valid names | Requirement is satisfied without unexpected side effects | Passed
CHK-043 | HTTP Status Codes | POST returns 201 | Requirement is satisfied without unexpected side effects | Passed
CHK-044 | HTTP Status Codes | GET/PUT/login return 200 | Requirement is satisfied without unexpected side effects | Passed
CHK-045 | HTTP Status Codes | DELETE returns 204 | Requirement is satisfied without unexpected side effects | Passed
CHK-046 | HTTP Status Codes | Business error returns 400 | Requirement is satisfied without unexpected side effects | Passed
CHK-047 | HTTP Status Codes | Auth failure returns 401 | Requirement is satisfied without unexpected side effects | Passed
CHK-048 | HTTP Status Codes | Unknown resource returns 404 | Requirement is satisfied without unexpected side effects | Passed
CHK-049 | HTTP Status Codes | Duplicate returns 409 | Requirement is satisfied without unexpected side effects | Passed
CHK-050 | HTTP Status Codes | Schema error returns 422 | Requirement is satisfied without unexpected side effects | Passed
CHK-051 | Error Handling | Errors are JSON | Requirement is satisfied without unexpected side effects | Passed
CHK-052 | Error Handling | Error has detail | Requirement is satisfied without unexpected side effects | Passed
CHK-053 | Error Handling | No stack trace exposed | Requirement is satisfied without unexpected side effects | Passed
CHK-054 | Database | Records persist | Requirement is satisfied without unexpected side effects | Passed
CHK-055 | Database | Email is unique | Requirement is satisfied without unexpected side effects | Passed
CHK-056 | Database | Order references entities | Requirement is satisfied without unexpected side effects | Passed
CHK-057 | Database | Stock update persists | Requirement is satisfied without unexpected side effects | Passed
CHK-058 | Swagger | Docs page loads | Requirement is satisfied without unexpected side effects | Passed
CHK-059 | Swagger | Schemas are shown | Requirement is satisfied without unexpected side effects | Passed
CHK-060 | Swagger | Endpoints are tagged | Requirement is satisfied without unexpected side effects | Passed
