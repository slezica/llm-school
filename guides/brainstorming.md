---
topic: Brainstorming
trigger: Read when the user indicates they want to brainstorm, or when starting the design for a complex feature, before writing implementation plans, or when you detect an idea needs refinement and exploration.
version: 1.0.0
---

# Brainstorming

## Overview

Transform rough ideas into fully-formed designs and plans through structured questioning and alternative exploration.

**Core principle:** Ask questions to understand, explore alternatives, present design incrementally for validation.


## Process

### Phase 1: Understanding
- Check current project state in working directory.
- Ask ONE question at a time to refine the idea.
- Prefer multiple choice when possible.
- Stop asking questions when the picture is reasonably complete, and pending decisions can be postponed.
- Gather: Purpose, constraints, success criteria.

### Phase 2: Exploration
- Propose 2-3 different approaches.
- For each: Core architecture, trade-offs, complexity assessment.
- Ask the user which approach resonates.

### Phase 3: Presentation
- Present in 200-300 word sections.
- For designs, cover architecture, components, data flow, error handling, testing.
- For plans, cover phases, steps, and checkpoints.
- Ask after each section: "Does this look right so far?".

### Phase 4: Writing
- Ask: "Ready to write these ideas to a file?".
- If approved, read the `writing-plans` guide if creating an implementation plan, or default to writing a markdown file in the `docs/` directory with the date in `YYYY-MM-DD` format as a filename prefix.
- If rejected, ask what to do next.


## When to Revisit Earlier Phases

**You can and should go backward when:**

- New constraints or requirements are revealed in phase 2+. Return to Phase 1.
- Fundamental problems or gaps are discovered in phase 2+. Return to Phase 1.
- User questions approach in phase 3. Return to Phase 2.
- Something doesn't make sense to you. Go back and clarify.

**Don't plow ahead** when going backward would give better results.

