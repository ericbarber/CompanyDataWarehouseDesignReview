# Function Documentation Template

## FUN-nnnnn — `function_name`

**Status:** Unknown  
**Location:** `repository/path.py`  
**Category:** Ingestion | Transformation | Security | Utility | Observability

### Purpose

Describe the responsibility in plain language and state what is explicitly outside its responsibility.

### Signature

```python
def function_name(parameter: type) -> return_type:
    ...
```

### Inputs and outputs

| Name | Type | Required | Default | Meaning |
|---|---|---:|---|---|
|  |  |  |  |  |

### Processing behavior

1. State validation and setup.
2. Describe reads and decisions.
3. Describe transformations.
4. Describe writes and returned values.

### Data and side effects

- Reads:
- Writes:
- Permission changes:
- External calls:
- Logs and metrics:

### Failure and recovery

Document raised exceptions, partial-write behavior, retry safety, idempotency, and replay procedure.

### Security behavior

Document identities, secrets, PII/CUI handling, dynamic SQL, trust-boundary crossings, and audit events.

### Relationships

- Called by:
- Calls:
- Produces movements:
- Relevant diagrams:

### Modernization assessment

**Disposition:** Retain | Refactor | Replace | Retire  
**Rationale:**  
**Target capability:**  
**Required tests:**

