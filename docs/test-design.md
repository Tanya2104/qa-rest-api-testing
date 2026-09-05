# Test Design

| Technique | Applied to | Partitions / values | Representative tests |
|---|---|---|---|
| Equivalence Partitioning | `POST /users` age | valid 18–100; invalid <18 and >100 | 30, 17, 101 |
| Equivalence Partitioning | email/password | valid email and ≥8 chars; malformed/short | `qa@example.com`, `bad`, `short` |
| Boundary Value Analysis | age | 17, **18**, **100**, 101 | automated parametrized boundary test |
| Boundary Value Analysis | product price/stock | price -1, 0, >0; stock -1, **0**, 1 | product negative tests |
| Boundary Value Analysis | order quantity | -1, 0, 1, stock, stock+1 | order validation and inventory tests |
| Decision Table | order creation | user exists? product exists? quantity valid? stock enough? | create only when all four conditions are true; otherwise 404/422/400 |
| Decision Table | login | email exists? password matches? fields present? | 200 only for both valid; 401 for bad credentials; 422 for missing fields |
| Positive Testing | CRUD and login | complete valid payloads | create/read/update/delete and successful login |
| Negative Testing | validation/business rules | duplicates, missing/malformed values, unknown IDs, excess stock | assert JSON errors and exact status category |

Order total and stock are checked together to expose integration failures, while resource tests isolate schema and CRUD behavior.
