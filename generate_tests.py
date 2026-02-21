from framework.core.test_generator import generate_tests

login_prompt = """
Generate regression test cases for LOGIN module.

Cover:
- valid login
- invalid login
- forgot password
- session expiry
- brute force protection
- security edge cases

Return JSON format:
{
 "module": "login",
 "tests": [
   {
     "id": "",
     "title": "",
     "priority": "P0/P1/P2",
     "steps": [],
     "expected_result": ""
   }
 ]
}
"""

dashboard_prompt = """
Generate regression test cases for DASHBOARD module.

Cover:
- widget loading
- filters and sorting
- permission visibility
- responsive layout
- data accuracy
- API failures

Return structured JSON test cases.
"""

api_prompt = """
Generate REST API test cases covering:
- auth token validation
- CRUD
- schema validation
- rate limiting
- error handling

Return JSON structured test cases.
"""

generate_tests("login", login_prompt)
generate_tests("dashboard", dashboard_prompt)
generate_tests("api", api_prompt)