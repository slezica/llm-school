---
topic: Test-driven Development
trigger: Read before writing non-trivial code, or when explicitly instructed to.
version: 1.0.0
---

# Test-driven Development

## Overview

The core philosophy of test-driven development is to write tests first, behavior second. The preferred approach is called RED-GREEN-REFACTOR and follows the following cycle:

1. RED: Write a failing test that captures the next requirement.
2. GREEN: Write the minimal code to make the test pass.
3. REFACTOR: Clean up the implementation while keeping tests passing.
4. Repeat for the next requirement.

## Limits

Sometimes TDD isn't appropriate. This could be the case during exploratory work, prototyping, UI-heavy work that can't be tested automatically, etc. In these cases, change or adapt the approach as needed, including in your final report the decision you made and the rationale.

You may be instructed to avoid TDD too. If so, prioritize your instructions.


## Reporting to Overseer

When complete, report:
- What was implemented and test coverage achieved
- Any deviations from TDD approach and why
- Test results and any remaining issues
- Recommendation for next steps

