---
topic: Design Philosophy
trigger: Read before designing, specifying or writing code. This is a fundamental guide.
version: 1.0.0
---

# Design Philosophy

The first and foremost principle of good design is minimalism.

Minimalism takes many forms. At a high level, it means reducing the amount of moving parts in a codebase: the amount of concepts, of dependencies, of entities, of responsibilities, of layers. At a low level, it means avoiding unnecessary variables, functions, classes, state. It's an all-encompasing consideration.

Some aspects of minimalism are part of the collective language of software. Don't Repeat Yourself. You Aren't Gonna Need It. Early Optimization is the Root of All Evil. Simpler is Always Better.

All of these sayings and acronyms capture portions of the overarching philosophy of minimalism. A broader way to express the concept is perhaps:

> If less is sufficient, less should be added.


## Staying Away from Complexity

When minimalistic principles are abandoned, complexity quickly grows. Clarity, brevity, readability, maintainability -- all the desirable features of good code start to degrade. The philosophy must be upholded in all but the most exceptional circumstances.

Complexity can grow for many reasons. The philosophy of minimalism requires you to constantly ask yourself questions such as:

- Is this dependency necessary?
- Is this abstraction layer necessary?
- Is this optimization necessary?
- Is this mutable state necessary?
- Is this directory structure necessary?
- Is this scalability ever going to be necessary?

When the answer is 'no', or even 'perhaps later', complexity is usually not warranted.

When the answer is 'yes', then complexity is necessary for the system to fulfill its requirements. This is also part of minimalism: it doesn't seek _nothing_, it seeks _the minimum_. Systems have essential complexities that can only be handled with complex design.


## Keeping Doors Open

Another aspect of minimalism is that, when correctly applied, it leaves the door open for necessary complexity to be added later. It seeks to add less, yes, but doesn't preclude adding more in the future if the essential complexity of the system grows, and thus the implementation must become more complex to accomodate its requirements.

Designers must strike a balance. Seek the minimum, but don't be so ruthless as to sabotage future growth. The second set of questions that a minimalist must consider includes, for example:

- Is this likely to change its internal behavior?
- Is this likely to change its external interface?
- Will this require an inevitable refactor soon?
- Is that library better than anything we could reasonably do ourselves?

When the answer to these questions is 'yes', or even 'highly likely', complexity is usually warranted.


## Specifications and Roadmaps

The strong minimalist also applies these principles to the things that surround the code. Specifications can be simplified, documents can be written more concisely, roadmaps can be shortened -- but not to the point of sabotage, as already explored.

A good rule of thumb is that specifications and roadmaps should never be more complex than their actual implementations. If the roadmap has 20 steps and the code has 10 lines, it was unreasonably complex. If the specification calls for 3 types but only 1 is actually important, it was unreasonably complex.


