---
topic: Writing Plans
trigger: Read before creating an implementation plan, or when instructed to write "a roadmap".
version: 2.0.0
---

# Writing Plans

## Overview

Solid implementation plans facilitate the task of implementers by providing a clear roadmap for them to follow. It's the job of architects to write these plans with the implementers in mind.

Always assume the implementer reading your plan is a capable developer, but has zero context for the codebase and questionable taste. Document everything they need to know: which files to touch for each task, code, testing, docs they might need to check, how to test it. Give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.


## Dividing Plans

Good plans are divided in phases, which in turn are divided in steps.

Phases encompass the path between one milestone and the next. At the end of each phase, the project is in a usable state, all tests are passing, and something well-defined has been accomplished. Phases must be clear enough to be described in one sentence.

Steps are more granular tasks within each phase that progressively advance to the next milestone. Individual steps are allowed to break tests, create temporal inconsistencies and employ ad-hoc code that will later be removed or replaced.

Phases often map to feature branches, while steps often map to commits.

It's possible that plans for low-complexity features are composed of a single phase. Don't add phases or steps to the plan in order to make it seem more extensive or complete when it's not necessary.


## Proportional Complexity

An implementation plan should never be more complex than the feature it's implementing. Don't try to create extensive plans when smaller ones will do. There's nothing wrong with a single-phase plan without examples or snippets when the taskl is straightforward.


## Preserving Plans

You MUST save your plans to a markdown file when done, located in the project `docs/` directory. Create the directory if missing, and name the file according to its topic.


## Implementation Strategy

Implementers prefer to work with the RED-GREEN-REFACTOR strategy for test-driven development. Bear this in mind when dividing phases into steps. The steps taken must correlate with tests that the implementers can write as they move along.


## Decisions Included

Decisions such as library and framework choices, project directory structure, location of files, names of components and modules, etc. are made by the architect and included in the plan.

Only leave for implementers the decisions around how to write the code and tests that fulfill each step. Provide precise requirements.


## Plan Document Structure

Plans are markdown files that follow this structure:

1. Header naming the plan.
2. Overview of the plan's context, goals and decisions made ahead of time.
3. Introductory instructions (if any)
4. For each phase:
    1. Header naming the phase.
    2. Expected end-state of the phase, its milestone.
    3. Bullet-points describing each internal step.
    4. Additional instructions (if any), which can be general or for specific steps, including any examples or directions for the implementer.
5. Additional instructions (if any) for the implementer's final report.


## Writing Tips

- Be concise. Specific and detailed, yes, but without excessive prose.
- Provide context. The implementer doesn't have the larger context of the project.
- Take care of naming and architecture. Choose the concepts and relations that make up the code yourself.
- Refer to files by their exact location. Don't risk confusion or misalignment.
- Don't micromanage. These are medium-to-high level concerns. The implementer is capable of covering the gaps.


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

**End state:** All code blocks have a copy button. Tests passing.

**Steps:**

1. Write failing test for copy button visibility and click behavior
2. Add button to `CodeBlock` with clipboard functionality
3. Add hover state styling and success feedback
4. Verify in docs viewer
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

## Phases

1. **Basic Search** - Users can search products and see results
2. **Filters & Pagination** - Users can filter and navigate pages

## Instructions

Follow TDD: write failing test, implement to pass, refactor. Commit after each step.

---

## Phase 1: Basic Search

**End state:** Users can type a query and see matching products. All tests passing.

**Steps:**

1. Create search feature structure and route
2. Write failing test for `SearchBar`, then implement with debounced input (300ms)
3. Write failing test for API hook, then implement `useProductSearch`
4. Write failing test for `SearchResults`, then implement display with empty state
5. Wire components together and verify end-to-end

**Instructions:**

For step 1, create:
- `src/features/search/components/SearchBar.tsx`
- `src/features/search/components/SearchResults.tsx`
- `src/features/search/hooks/useProductSearch.ts`
- `src/features/search/__tests__/` (test files)

Add route `/search` to `src/App.tsx`.

For step 3, implement `useProductSearch` with this interface:
```typescript
interface SearchResult {
  products: Product[];
  totalResults: number;
  loading: boolean;
  error: Error | null;
}

function useProductSearch(query: string): SearchResult
```

Reuse `ProductCard` from `src/features/products/components/ProductCard.tsx`.

---

## Phase 2: Filters & Pagination

**End state:** Users can filter by category/price and navigate pages. All tests passing.

**Steps:**

1. Write failing test for `FilterPanel`, then implement with category checkboxes and price inputs
2. Update `useProductSearch` to accept filters and page number
3. Write failing test for `Pagination`, then implement with prev/next and page numbers
4. Sync all params to URL using `useSearchParams`

**Instructions:**

Create `src/features/search/components/FilterPanel.tsx` and `Pagination.tsx`.

Define filter types in `src/features/search/types.ts`:
```typescript
interface FilterOptions {
  categories: string[];
  minPrice?: number;
  maxPrice?: number;
}

interface SearchParams {
  query: string;
  filters: FilterOptions;
  page: number;
}
```

Update hook signature:
```typescript
function useProductSearch(params: SearchParams): SearchResult
```

URL params: `q`, `categories`, `minPrice`, `maxPrice`, `page`.

## Report

Provide: summary of task completion, test coverage report, any deviations in methodology or in details of the plan you were forced to adapt.
~~~

