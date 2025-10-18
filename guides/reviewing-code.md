---
topic: Reviewing Code
trigger: Read before reviewing code, or when instructed to "do a code review".
version: 1.0.0
---

# Reviewing Code

## Overview

Code review is a quality gate that catches bugs, identifies design issues, and ensures maintainability. Be thorough yet collaborative: block on correctness, be flexible on style.

**Core principle:** Correctness first, design second, quality third. Clear feedback over pedantry.


## Review Checklist

Examine code in priority order:

### Correctness (Blocking)
- Tests pass and cover critical paths
- Error handling covers failure modes
- Boundary conditions and edge cases handled
- No race conditions, memory leaks, or security issues
- Resource cleanup (files, connections, memory)
- Type safety and null handling

### Design (Usually Blocking)
- Meets stated requirements
- Integrates cleanly with existing architecture
- Appropriate abstractions for the problem
- Complexity is justified or can be simplified
- Testability and modularity

### Quality (Rarely Blocking)
- Clear, self-documenting code
- Consistent formatting and naming
- Adequate logging for debugging
- Appropriate comments for complex logic
- No obvious refactoring opportunities

**Be honest about severity**: Don't inflate opinions to recommendations or recommendations to blocking issues.

When in doubt about severity, err on the side of being more lenient. The goal is to help ship quality code, not to be a perfectionist gatekeeper.


## Feedback Types

Categorize every piece of feedback:

### Blocking Issues

Must be fixed before proceeding. Acknowledge good work, then provide clear, actionable feedback with examples:

- Correctness bugs or wrong behavior
- Security vulnerabilities or data loss risks
- Missing critical requirements
- Test failures or inadequate coverage
- Design contradicts architectural plan

### Non-Blocking Suggestions

Enhance quality but don't block. Consider suggesting follow-up work instead:

- Refactoring for clarity
- Additional edge case tests
- Documentation improvements
- Non-critical performance optimizations
- Style and naming preferences


## Review Output Format

You MUST output a concise report of your findings.

```markdown
## Review Summary
[One paragraph: what was reviewed, overall assessment]

## Blocking Issues
- [Issue with file:line reference and concrete fix suggestion]

## Suggestions
- [Non-blocking improvement with rationale]

## Positive Observations
- [What was done well]

## Recommendation
[APPROVE | REQUEST CHANGES | NEEDS REDESIGN]
```


## Red Flags - Stop and Escalate

**Escalate to overseer when:**
- Code fundamentally contradicts architectural plan
- Critical security or safety issues present
- Major breaking changes without discussion
- Implementation marked complete but isn't
- Tests failing or not run

**Escalation means:** Report findings, recommend returning to previous phase or architect consultation.


