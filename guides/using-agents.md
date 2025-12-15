---
topic: Using Agents
trigger: Read when instructed to use agents for tasks.
version: 1.1.0
---

# Using Agents

## Overview

You can deploy agents for different tasks, acting as their overseer. Learning from this guide empowers you to orchestrate agents to achieve results in an effective manner.
    

## Implementation Tasks

Agents can assist with implementation tasks using a 3-phase workflow. The overseer goes through these phases deploying the various agents with appropriate instructions.

1. **Implementation**. The `implementer` is deployed to write code according to a plan. The output is an updated project ready for review.

2. **Review**. The `reviewer` is deployed to check the work of the `implementer` and discover bugs, identify design failures and find opportunities for improvement. The output is a detailed report.

3. **Feedback**. The `implementer` is deployed again and given the report from the `reviewer`, in order to address it.

When the workflow is complete (or aborted in exceptional circumstances), the overseer presents a report to the user.


## Research Tasks

Agents can take care of in-depth research when required. You can deploy the `researcher` agent and give it a clear discovery mission, expecting back a detailed report.


## Agent Instructions

Instructions to deployed agents must be precise, and include:

- A thorough description of the task.
- The scope of the task, with criteria to determine when it's done.
- Abort conditions, situations to watch out for that require stopping the work.
