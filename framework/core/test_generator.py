from framework.core.llm_client import call_llm
import json
import os

def generate_tests(module_name, base_prompt):
    print(f"\nGenerating tests for {module_name}...\n")

    # Step 1: initial generation
    initial_output = call_llm(base_prompt)

    # Step 2: self-refinement (agentic loop)
    refinement_prompt = f"""
You are a senior QA architect reviewing generated test cases.

Refine and improve the following test cases:
- remove duplicates
- add missing edge cases
- ensure regression completeness
- structure properly in JSON format

Return STRICT JSON only.

Test Cases:
{initial_output}
"""

    improved_output = call_llm(refinement_prompt)

    try:
        parsed = json.loads(improved_output)
    except:
        parsed = {"raw_output": improved_output}

    file_path = f"framework/tests/generated_{module_name}_tests.json"

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=4)

    print(f"Saved → {file_path}")
    return parsed