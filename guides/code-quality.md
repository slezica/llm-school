---
topic: Code Quality
trigger: Read before writing any code. This is a fundamental guide.
version: 1.0.0
---

# Code Quality

Writing code that readers will thank you for requires attention to naming, visual structure, simplicity, and consistency. These principles apply across all programming tasks.


## Naming

- Use clear, descriptive names that reveal intent and make comments unnecessary
- Follow project naming conventions strictly
- Prefer short contextual names when meaning is clear in their scope


## Visual Structure

- Make code scannable and easy to navigate
- Use empty lines to separate conceptual blocks
- Group related declarations and operations together
- Add whitespace before complex blocks for visual breathing room
- Align similar lines to help readers scan quickly


## File Structure

- Organize code top-down, high-level first, details later
- Separate top-level declarations with two empty lines
- Place related functionality in proximity


## Simplicity

Minimize accidental complexity:

- Prefer short-circuit conditions over deep nesting
- Extract complex logic into well-named functions
- Keep functions focused on single responsibilities
- Favor straightforward solutions over unnecessary abstraction or cleverness
- Prefer verbosity over brevity when clarity demands it


## Consistency

- Follow established patterns and match the style of surrounding code
- Adhere to project-specific standards from CLAUDE.md
- Use the same approach for similar problems
