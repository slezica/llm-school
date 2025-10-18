---
topic: Tackling Projects
trigger: Read at the beginning of the implementation of a project, before anything else, or when instructed to "start work on a project".
version: 1.0.0
---

# Tackling Projects

## Overview

Complex projects can't be tackled in one go, and require methodical workflows to progressively develop them in cycles that lead from one milestone to the next. This is true both of fresh projects that just started, and of existing projects that are being continued.

Learning this skill empowers agents to tackle big projects with a highly effective development cycle, leveraging guides, agents and tools.

### Requirements

To apply this guide, you must also learn from the `brainstorming` and `implementing-features` guides.


## Workflow

Projects are sequences of feature implementations. The project-level workflow orchestrates multiple features:

1. **Brainstorming.** Follow the `brainstorming` guide to establish project requirements and scope. Output: requirements document.

2. **Feature cycle.** For each feature, follow the `implementing-features` guide (which handles planning, implementation, and review internally). Output: working feature.

3. **Checkpoint.** After each feature is complete, overseer and user decide: continue to next feature, adjust scope, or conclude project.

The overseer monitors progress and adapts. If requirements change or fundamental issues emerge, return to brainstorming. Refer to the `implementing-features` guide for how to deploy agents within each feature cycle.


## Adaptation and Improvisation

Projects present special cases. Deploy other agents (like `researcher` for information gathering) as needed outside the main workflow.

When the workflow requires adaptation, inform the user with your rationale and collaborate on the path forward.

