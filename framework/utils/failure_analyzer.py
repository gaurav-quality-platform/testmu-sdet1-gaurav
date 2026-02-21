"""
TestMu AI Challenge – Task 3 Implementation

Chosen Option: A — Failure Explainer

Reason for choosing this option:
Failure explanation provides immediate debugging value during regression runs by 
analyzing test failures in real time and suggesting actionable fixes.

This approach reduces manual triage effort and helps engineers quickly identify
whether a failure is caused by a product bug, test issue, or environment problem.

Option B (Flaky Test Classifier) was considered, but Option A was prioritized
because root cause analysis and fix suggestions offer more direct value to fast-
moving engineering teams and better demonstrate AI-assisted debugging workflows.

This implementation sends real failure context to an LLM via OpenRouter API and
returns structured root cause analysis attached to the test report.
"""

import os
import re
import json
from datetime import datetime
from framework.core.llm_client import call_llm

def clean_json_response(text):
    # remove ```json or ``` wrappers
    text = re.sub(r"```json|```", "", text).strip()
    return text

def analyze_failure(test_name, error_message):

    prompt = f"""
You are a senior SDET analyzing a failed automated test.

Return ONLY valid JSON in this format:

{{
  "root_cause": "",
  "failure_category": "bug | test_issue | environment",
  "severity": "low | medium | high",
  "suggested_fix": ""
}}

Test Name: {test_name}
Error: {error_message}
"""

    response = call_llm(prompt)

    cleaned = clean_json_response(response)

    try:
        parsed = json.loads(cleaned)
    except:
        parsed = {
            "root_cause": cleaned,
            "failure_category": "unknown",
            "severity": "medium",
            "suggested_fix": "Manual review required"
        }

    report = {
        "test_name": test_name,
        "analysis": parsed,
        "timestamp": str(datetime.now())
    }

    os.makedirs("reports", exist_ok=True)

    with open("reports/failure_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\n===== AI FAILURE ANALYSIS =====\n")
    print(f"Root Cause      : {parsed['root_cause']}")
    print(f"Category        : {parsed['failure_category']}")
    print(f"Severity        : {parsed['severity']}")
    print(f"Suggested Fix   : {parsed['suggested_fix']}\n")