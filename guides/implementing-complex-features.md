---
topic: Implementing Complex Features
trigger: Read before starting the implementation of non-trivial features.
version: 1.0.0
---

# Implementing Complex Features

## Overview

Complex features are better implemented by deploying specialized agents and acting as their overseer. Learning this skill empowers you to orchestrate these agents to implement features in an effective manner.


## Workflow

Features are developed in 3 phases. It's the job of the overseer to go through these phases deploying the various agents with instructions.

1. **Implementation**. The `implementer` is deployed to execute implementation instructions. Each step is committed individually. The output is an updated project ready for review.

2. **Review**. The `reviewer` is deployed to check the work of the `implementer`, and discover bugs, identify design failures and find opportunities for improvement. The output is a detailed report.

3. **Feedback**. The `implementer` is deployed again and given the report from the `reviewer`, in order to address it.

When the workflow is complete, the overseer presents a report to the user.


## Agent Instructions

Instructions to deployed agents must be precise, and include:

- A thorough description of the task.
- The scope of the task, with criteria to determine when it's done.
- Abort conditions, situations to watch out for that require stopping the work.
