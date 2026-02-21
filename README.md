# TestMu AI – SDET AI-Native Quality Engineering Challenge

## Overview
This project demonstrates an AI-native approach to reducing manual regression testing effort by integrating LLM capabilities directly into the automation framework.

The goal was to simulate an early **agentic QA workflow** where:
- Regression tests are generated via LLM
- Generated tests are refined automatically
- Test failures trigger AI-driven root cause analysis
- Structured debugging insights and fix suggestions are produced

This reflects how AI can assist QA teams in reducing manual test design and debugging time.

---

## Architecture

framework/core → LLM client, configuration, AI test generator  
framework/tests → generated and executable tests  
framework/utils → AI failure analysis engine  
reports/ → structured AI failure reports  

### Workflow

1. LLM generates regression test cases (Login, Dashboard, API)
2. Generated tests are refined via self-evaluation loop
3. Tests are executed using pytest
4. On failure → error context sent to LLM
5. LLM returns root cause, severity and fix suggestion
6. Structured failure report generated automatically

This creates a minimal **AI-assisted regression + debugging loop**.

---

## Task 2 — Prompt Engineering for Test Generation

LLM prompts were executed programmatically to generate regression scenarios for:

- Login module  
- Dashboard module  
- REST API module  

Outputs are stored as structured JSON inside:
```
framework/tests/
```

Prompts used and refinement iterations are documented in:
```
prompts.md
```

Each module includes:
- Raw prompts used
- Iteration improvements
- Generated structured test cases

---

## Task 3 — LLM Integration in Test Framework (Failure Explainer)

Chosen Option: **Failure Explainer**

When a test fails:
- Failure context is automatically captured
- Sent to LLM via OpenRouter API
- LLM returns structured JSON analysis:
  - Root cause
  - Failure category
  - Severity
  - Suggested fix
- Report saved to:
```
reports/failure_report.json
```

This demonstrates how AI can reduce debugging and manual triage effort.

---

## How to Run

### 1. Install dependencies
```
pip install -r requirements.txt
playwright install
```

### 2. Add OpenRouter API key
Create `.env` file in root:
```
OPENROUTER_API_KEY=your_key_here
```

### 3. Generate AI test cases
```
python generate_tests.py
```

### 4. Run tests
```
pytest -s
```

On failure, AI analysis will be printed and saved to:
```
reports/failure_report.json
```

---

## AI Usage

LLMs were used for:
- Structured regression test generation
- Prompt refinement and coverage expansion
- Automated failure root cause analysis
- Severity classification and fix suggestions

All AI usage is logged in:
```
ai-usage-log.md
```

---

## If Given More Time

- Self-healing locator engine using DOM diff + LLM  
- Autonomous regression expansion agent  
- CI/CD integration for automatic failure triage  
- Flaky test clustering using embeddings  
- Test impact analysis using AI  

---

## Author
Gaurav Marothia