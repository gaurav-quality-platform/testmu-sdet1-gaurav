# Prompt Engineering Log – TestMu AI Challenge

## Approach
All prompts were executed programmatically through the framework using OpenRouter LLM integration.
The goal was to reduce manual test design effort and simulate an AI-assisted QA workflow.

---

## LOGIN MODULE

### Prompt v1
Generate regression test cases for LOGIN module covering valid login, invalid login and forgot password.

### Issue
Initial output lacked security and session edge cases.

### Prompt v2 (refined)
Generate comprehensive regression test cases for Login module covering:
- valid login
- invalid credentials
- forgot password
- session expiry
- brute-force lockout
- security edge cases

Return structured JSON with priority tags.

### Improvement
Received structured regression-ready scenarios with better coverage and prioritization.

---

## DASHBOARD MODULE

### Prompt used
Generate dashboard test cases covering widgets, filters, permissions, responsiveness and API failures.

### Issue
Initial output missed permission-based edge scenarios.

### Refinement
Explicitly added role-based and empty-state scenarios.

### Result
Improved coverage across functional and UI validation cases.

---

## API MODULE

### Prompt used
Generate REST API regression tests covering auth validation, CRUD, schema validation, rate limiting and error handling.

### Improvement
Refined prompt to enforce structured JSON output and include boundary conditions.