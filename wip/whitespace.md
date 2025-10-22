# Visual Patterns

Code is text. Text is meant to be read.

The visual structure of code makes a huge difference in the ability of a reader to quickly identify concepts, related sections, similarities and differences, points of complexity.

Code is also ideas. Ideas are meant to be reasoned about.

When code is visually structured in a comfortable manner, so are the underlying ideas. Good code reveals the structure and relation of the concepts themselves, not just the implementation.


# Techniques

There are a number of techniques to improve visual structure.

## Brevity

## Naming

Techniques to apply when deciding the names of concepts in code.

### Prefix and Suffix

When multiple concepts share a common kind, relate to the same object or are parts of a whole, their names should convey the relationship.

Same kind:
```
KEY_USER
KEY_REGION
KEY_PERMISSIONS
```

Parts of a whole:
```
taskTitle
taskBody
taskPriority
```

Prefixes are better than suffixes because they align visually. Names with the same prefix written in consecutive lines create a column structure that visually separates the shared part from the unique part of each name. Compare:

```
borderTop
borderBottom

topBorder
bottomBorder
```

1. Naming
- Prefix
- Suffix

2. Whitespace
- Alignment
- Sectioning
