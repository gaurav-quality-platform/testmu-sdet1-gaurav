# AI Usage Log – TestMu AI Challenge

## Objective
The goal was to demonstrate how AI can reduce manual effort in regression test design and debugging by integrating LLM capabilities directly into the test framework.

---

## Tools Used

### ChatGPT
Used for:
- Designing modular AI-native test framework structure
- Structuring prompt engineering approach
- Planning LLM integration for test generation and failure analysis
- Designing self-refining test generation workflow

Output:
- Framework architecture plan
- Prompt engineering structure
- Failure analysis workflow design

---

### OpenRouter LLM (GPT model)
Used for:

#### 1. Automated Test Generation
- Generated regression test cases for Login, Dashboard and API modules
- Produced structured JSON test scenarios
- Refined generated tests through self-evaluation prompt loop

#### 2. Prompt Engineering Iteration
- Improved coverage for security, edge cases and error scenarios
- Ensured structured and reusable output format

#### 3. Failure Analysis
On test failure:
- Test name and error context sent to LLM
- LLM returned:
  - Root cause
  - Failure category
  - Severity
  - Suggested fix

Output saved as structured JSON report.

---

## AI-Assisted Workflow Demonstrated

This project simulates an AI-assisted QA lifecycle:

1. AI generates regression tests
2. Tests are refined automatically
3. Tests execute via pytest
4. Failures trigger AI root cause analysis
5. Structured debugging insights produced

This demonstrates how AI can support QA engineers by:
- Reducing manual test design effort
- Accelerating debugging
- Improving regression coverage

---

## Transparency
All prompts used for generation are included exactly as executed in:
```
prompts.md
```

No outputs were manually edited after generation.