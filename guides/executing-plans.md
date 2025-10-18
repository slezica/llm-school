---
topic: Executing Plans
trigger: Read before executing an implementation plan.
version: 1.0.0
---

# Executing Plans

## Overview

Plans are divided in phases, and must be tackled on phase at a time. This workflow captures the implementation cycle of a plan, phase by phase.


## Required Reading

You MUST IMMEDIATELY read these guides as well:

- {{ ref('implementing-complex-features') }}


## Workflow

The overseer executes plans are executed in 3 steps that may repeat.

1. Execution. The `implementing-complex-features` workflow is used to execute the NEXT PHASE of the plan, starting from the current state.

2. Oversight. The overseer examines the result and stops to notify the user if something is wrong.

3. Cycle. The overseer repeats this workflow until ALL PHASES of the plan have been executed.

