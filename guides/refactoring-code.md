---
topic: Refactoring Code
trigger: Read before refactoring tasks, when code review identifies structural improvements, when technical debt needs addressing, or when explicitly instructed to.
version: 1.0.0
---

# Refactoring Code

## Overview

Refactoring improves code structure without changing external behavior. Done well, it makes code more maintainable, testable, and understandable. Done poorly, it introduces bugs and waste.

**Core principle:** Small steps. Tests green. Preserve behavior. Commit frequently.


## When to Refactor

**Refactor when:**
- Code works but is hard to understand or modify
- Duplication makes changes error-prone
- Tests exist and pass (or can be added first)
- You're about to add a feature and current structure fights you
- Code review reveals design issues

**Don't refactor when:**
- Tests are failing (fix first, then refactor)
- Requirements are unclear (clarify first)
- Code doesn't work yet (make it work, then clean)
- Rewrite would be cheaper (see Red Flags)
- No tests exist and code is too complex to test safely


## Workflow

### Phase 1: Preparation

1. Ensure all tests pass. If no tests exist, write characterization tests first.
2. Identify specific problems: duplication, unclear naming, tangled responsibilities, excessive complexity.
3. Define scope: which files, functions, or modules will change.
4. Choose refactoring pattern(s) from Common Patterns below.
5. Plan sequence of small, safe transformations.

### Phase 2: Execution

For each transformation:

1. Make one focused change (rename, extract, inline, etc.)
2. Run tests immediately
3. If tests fail, revert and try smaller step
4. If tests pass, commit with descriptive message
5. Repeat until refactoring complete

**Critical:** Never mix refactoring with behavior changes. If you discover bugs while refactoring, finish refactoring first unless the bugs make it impossible.

### Phase 3: Verification

1. Run full test suite including integration tests
2. Review changes: is code clearer, simpler, more maintainable?
3. Check performance if relevant (refactoring shouldn't degrade it)
4. Verify no behavior changes: edge cases, error handling, outputs unchanged


## Common Patterns

### Extract Function
**When:** Code block does one thing that can be named
**How:** Move block to new function, replace with call
**Example:** Extract validation logic scattered across a handler

### Inline Function
**When:** Function body is clearer than the name
**How:** Replace calls with function body
**Example:** Remove one-line wrappers that add no clarity

### Rename
**When:** Names mislead or obscure intent
**How:** Rename systematically across codebase
**Example:** `getData()` → `fetchUserProfile()`

### Extract Variable
**When:** Complex expression obscures meaning
**How:** Assign to well-named variable
**Example:** `if (user.age > 18 && user.verified)` → `if (isEligible)`

### Move Function/Class
**When:** Function belongs with related code elsewhere
**How:** Relocate to appropriate module
**Example:** Move validation to data model

### Replace Conditional with Polymorphism
**When:** Type-checking logic scattered across functions
**How:** Use inheritance or strategy pattern
**Example:** `if type == "A"` branches → separate classes

### Consolidate Duplicate Code
**When:** Same logic in multiple places
**How:** Extract to shared function/module
**Example:** Repeated validation → single validator

### Simplify Conditional
**When:** Nested conditions hard to follow
**How:** Extract to named functions, invert conditions, use guard clauses
**Example:** Early returns instead of deep nesting

### Break Up Large Function
**When:** Function does too many things
**How:** Extract cohesive pieces to separate functions
**Example:** 200-line handler → orchestrator + helpers


## Red Flags - Stop and Reconsider

**Stop refactoring when:**
- Tests keep breaking despite small changes (design might be fundamentally flawed)
- Refactoring reveals deep architectural problems (escalate to architect)
- Changes cascade uncontrollably across codebase (scope too large)
- You're rewriting >30% of the code (consider explicit rewrite instead)
- Each change requires more changes to maintain consistency (rabbit hole)

**Escalation means:** Report findings, recommend architectural redesign or scoped rewrite.


## Refactor vs Rewrite

**Refactor when:**
- Core design is sound
- Tests provide safety net
- Incremental improvement is valuable
- Risk of regression is manageable

**Rewrite when:**
- Architecture is fundamentally wrong
- No tests and code too complex to test
- Technology is obsolete
- Cost of incremental changes exceeds cost of rebuild


## Reporting to Overseer

When complete, report:

```markdown
## Refactoring Summary

**Scope:** [Files/modules refactored]

**Problems Addressed:**
- [What was wrong with the original code]

**Changes Made:**
- [Patterns applied with file:line references]

**Testing:** [Test coverage, all tests passing]

**Metrics:** [Lines changed, complexity reduced, duplication eliminated]

**Status:** [COMPLETE | BLOCKED | NEEDS ARCHITECTURAL REVIEW]
```


## Tips

- Commit after every green test run. Small commits are revert insurance.
- Use IDE refactoring tools when available (safer than manual edits)
- Read existing tests to understand intended behavior
- If uncertain about behavior, add tests before refactoring
- Refactor in one commit, behavior changes in another (never mix)
- When stuck, revert and try smaller steps
