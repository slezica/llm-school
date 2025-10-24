---
topic: Following Plans
trigger: Read before executing a detailed implementation plan.
version: 1.0.0
---

# Following Plans

## Overview

Detailed implementation plans, often made up of multiple phases, need a methodical workflow to be executed successfully. This workflow relies on deploying agents to take care of individual tasks.

### Requirements

To apply this guide, you must also learn from the `implementing-complex-features` guides.

## Workflow

Plans are sequence of phases, each of which can be treated as a feature implementation. To progressively implement a plan, follow this workflow:

1. **Select phase.** If you don't know the current phase of the plan, examine the project state to decide. If you already know, move on.

1. **Implement phase.** Follow the `implementing-complex-features` workflow (which handles implementation, and review of each phase internally).

3. **Checkpoint.** After the phase is implemented, review the newly added commits and ponder what to do next: continue to the next phase, or modify plans. Give your recommendation to the user.

When the workflow requires adaptation, inform the user with your rationale.

