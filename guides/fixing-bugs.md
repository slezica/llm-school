---
topic: Fixing Bugs
trigger: Read before starting bug-hunting or big-fixing tasks, or when instructed to "fix" or "diagnose" a bug.
version: 1.0.0
---

# Fixing Bugs

## Overview

Finding and fixing bugs is a combination of methodical discovery, testing and analysis in order to find the root cause of a problem and propose solutions. The result is a thorough and expertly crafted report.

## Methodology

Bug-fixing happens in steps.

1. Discovery. Information is gathered about the problem.
2. Testing. Hypotheses are proposed and tested to discover the causes for the problem.
3. Fixing. Code is written to address the problem and tests are added to detect regressions.


### Step 1: Discovery

Information about the problem is obtained by reproducing it, generating logs, stack traces, or writing ad-hoc tests intended to provide insight.

If able to reproduce the error, verify consistent reproduction and take note of the conditions under which it happens. The ability to reproduce the error is enormously helpful.

Search the code for potential culprits. Add strategic logging, write additional test cases or generate ad-hoc scripts when they help isolate the problem.


### Step 2: Testing

Generate hypothesis about the causes of the bug.

For each hypothesis, design a test that can validate or invalidate it. This can be an actual test case, or an ad-hoc construction for the case at hand.

Discover whether each hypothesis is correct (and contributes or causes the problem) or incorrect (and is unrelated to the problem).

Work in this manner until you find the root cause of the problem.


### Step 3: Fixing

Implement a minimal fix that eliminates the problem and restores correct behavior. Don't deviate from the goal, don't engage in refactors, don't change unrelated code.

Verify the fix resolves the issue by repeating tests that previously failed. Add test cases to the automated test suite to prevent regressions, guards and validations that make failures more obvious, plus whatever measures apply to the specific case.


## Common Bug Patterns

### Type-Related Bugs

- None/null handling
- Type mismatches
- Undefined variables
- Wrong argument counts

### State-Related Bugs

- Race conditions
- Stale data
- Initialization order
- Memory leaks

### Logic Bugs

- Off-by-one errors
- Boundary conditions
- Boolean logic errors
- Wrong assumptions

### Integration Bugs

- API contract violations
- Version incompatibilities
- Configuration issues
- Environment differences


## Reporting to Overseer

When complete, report:

```markdown
## Bug Report

**Problem:** [Description of the bug and how it manifests]

**Root Cause:** [What was causing the bug]

**Fix Applied:** [What was changed to fix it, with file:line references]

**Testing:** [How the fix was verified, tests added]

**Status:** [FIXED | BLOCKED | NEEDS DISCUSSION]
```


