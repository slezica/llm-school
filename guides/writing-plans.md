---
topic: Writing Plans
trigger: Read before creating a complex implementation plan, or when instructed to write "a roadmap".
version: 2.0.0
---

# Writing Plans

## Overview

Solid implementation plans facilitate the task of implementers by providing a clear roadmap for them to follow. It's the job of architects to write these plans with the implementers in mind.

Always assume the implementer reading your plan is a capable developer, but has zero context for the codebase. Document the architectural decisions and integration points they need to know. Trust implementers to determine implementation details. Give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.


## Dividing Plans

Good plans are divided into phases based on meaningful milestones. Each phase should deliver something complete and usable.

Phases encompass the path between one milestone and the next. At the end of each phase, the project is in a usable state, all tests are passing, and something well-defined has been accomplished. Phases must be clear enough to be described in one sentence.

**When to include steps:** Only when the implementation approach requires specific ordering or when there are non-obvious dependencies. Most phases don't need step-by-step breakdowns—trust implementers to determine their own path to the end state.

It's possible that plans for low-complexity features are composed of a single phase. Don't add phases or steps to the plan in order to make it seem more extensive or complete when it's not necessary.


## Proportional Complexity

An implementation plan should never be more complex than the feature it's implementing. Don't try to create extensive plans when smaller ones will do. There's nothing wrong with a single-phase plan without examples or snippets when the task is straightforward.


## Plan Granularity

Distinguish between architectural decisions and implementation details:

**Architectural decisions** (include in plans):
- Component hierarchy and data flow patterns
- Library and framework choices
- Module boundaries and integration contracts
- File structure when it affects multiple phases

**Implementation details** (leave to implementer):
- Which specific hooks or utilities to use
- Exact function signatures and interfaces (unless they're integration points between phases)
- Internal component state management
- Specific parameter names, debounce timings, page sizes, etc.

Include code snippets and exact file paths only when they represent architectural decisions or integration contracts that multiple components depend on. Otherwise, describe what needs to happen and trust the implementer to determine how.

**Example:** If Phase 1 creates an API hook that Phase 2 will extend, showing the hook's interface is architectural guidance—it's the contract between phases. But specifying every component's internal props or state shape is micromanagement (see the Complex Plan Example below).


## Preserving Plans

You MUST save your plans to a markdown file when done, located in the project `docs/` directory. Create the directory if missing, and name the file according to its topic.


## Implementation Strategy

Implementers prefer to work with the RED-GREEN-REFACTOR strategy for test-driven development. Focus on defining clear end states and integration contracts—implementers will determine the test sequence that gets them there.


## Decisions Included

Decisions such as library and framework choices, project directory structure, location of files, names of components and modules, etc. are made by the architect and included in the plan.

Also specify tooling used to manage dependencies, build, install the project, test it, etc.

Only leave for implementers the decisions around how to write the code and tests that fulfill each step. Provide precise requirements.


## Plan Document Structure

Plans are markdown files that follow this structure:

1. Header naming the plan.
2. Overview of the plan's context, goals and decisions made ahead of time.
3. Introductory instructions (if any)
4. For each phase:
    1. Header naming the phase.
    2. Expected end-state of the phase, its milestone.
    3. Key requirements and constraints.
    4. Integration contracts (message flows, interfaces, data structures that other phases depend on).
    5. Steps (only if ordering is critical or dependencies are non-obvious).
5. Additional instructions (if any) for the implementer's final report.

**Focus on contracts, not tasks.** Define what components need to agree on (APIs, message formats, interfaces), not how implementers should structure their work.


## Writing Tips

- Be concise. Specific and detailed for architecture, yes, but without excessive prose.
- Provide context. The implementer doesn't have the larger context of the project.
- Take care of naming and architecture. Choose the concepts and relations that make up the code yourself.
- Reference specific files only when architectural integration requires it, not for every step.
- Don't micromanage. Don't specify which hooks to use, exact interface shapes, debounce timings, or other implementation details unless they're integration contracts between components or phases. The implementer is capable and will make good choices.


# Simple Plan Example

Below is a minimal single-phase plan for a straightforward feature.

~~~markdown
# Add Copy Button to Code Blocks

## Overview

Add a "Copy" button to all code blocks in the documentation viewer. Currently users must manually select and copy code.

**Context:** Code blocks are rendered by `CodeBlock` component in `src/components/CodeBlock.tsx`.

**Decisions:**
- Use browser's Clipboard API
- Button appears on hover in top-right corner
- Show "Copied!" feedback for 2 seconds

## Phase 1: Copy Button Implementation

**End state:** All code blocks have a copy button with working clipboard functionality. Tests passing.

**Key requirements:**
- Button visible on hover only
- Success feedback displays for 2 seconds after copy
- Works with all existing code block variants
~~~


# Complex Plan Example

Below is a sample complex plan following the structure and principles outlined in this guide.

~~~markdown
# Product Search Implementation

## Overview

We're adding search functionality to the product catalog. Currently users can only browse by category. This feature adds full-text search with filters and pagination.

**Context:** Product catalog lives in `src/features/products/`. Backend exposes `/api/products/search` endpoint.

**Decisions:**
- New feature directory at `src/features/search/`
- Store search state in URL params for shareable links
- Results per page: 20 items
- Reuse existing `ProductCard` component and `useApiQuery` hook

**Testing:** Follow TDD throughout. All tests passing at end of each phase.

## Phases

### Phase 1: Basic Search
Users can search products and see results.

**Key requirements:**
- Search input with debounced queries
- Results display using existing `ProductCard` component
- Loading and empty states
- Route at `/search`

**Integration contract for Phase 2:**
```typescript
interface SearchResult {
  products: Product[];
  totalResults: number;
  loading: boolean;
  error: Error | null;
}

function useProductSearch(query: string): SearchResult
```

---

### Phase 2: Filters & Pagination
Users can filter by category/price and navigate result pages.

**Key requirements:**
- Filter panel with category checkboxes and price range
- Pagination with prev/next and page numbers
- All parameters (query, filters, page) synced to URL for shareable links

**Contract changes:**
Extend `useProductSearch` to accept object parameter with `query`, `filters`, and `page` fields. The `SearchResult` interface remains unchanged.

**Error handling:** Handle empty results, API failures, and invalid filter combinations.
~~~

