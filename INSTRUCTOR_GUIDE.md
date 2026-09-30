# Instructor Guide

## Class purpose

Students should leave class able to translate a question about tabular data
into a sequence of pandas operations. They should identify the observational
unit, inspect an unfamiliar table, predict whether a selection returns a
Series or DataFrame, build row-level Boolean masks, select with `.loc[]`, and
sort by one or more columns.

The class follows the NumPy lesson directly. The score table reuses the NumPy
array from that class so students can see what labels add while retaining the
ideas of shape, vectorized operations, and Boolean masks.

## Before class

1. Upload this folder to the course GitHub organization.
2. Confirm that students can fork the repository.
3. Replace the placeholder clone URL on the `Repository activity` slide with
   the final repository URL.
4. Run `uv sync` from a fresh clone.
5. Run `uv run python src/pandas_demo.py` and confirm that all assertions pass.
6. Open `activity/pandas-foundations.qmd` in Positron and select the `.venv`
   interpreter.
7. Render `slides/pandas-foundations.qmd` and confirm that speaker view opens
   when you press `S`.

## Planned 70-minute pacing

| Time | Material |
|:---|:---|
| 0-8 | Opening request, discussion, and operation grammar |
| 8-18 | NumPy bridge, Series, DataFrames, and label alignment |
| 18-27 | Observational unit and inspection |
| 27-39 | Column selection, `.loc[]`, and `.iloc[]` |
| 39-50 | Boolean masks and combined conditions |
| 50-59 | One-column and multi-column sorting |
| 59-64 | Derived variables, summaries, and readable pipelines |
| 64-76 | Repository activity and debrief |
| 76-79 | Exit check and final takeaway |

The complete sequence runs closer to 75 minutes when students receive the
full activity time. The activity can continue at the start of the next class
if needed.

## Compressed 50-minute pacing

| Time | Material |
|:---|:---|
| 0-5 | Opening request and operation grammar |
| 5-12 | NumPy bridge and pandas objects |
| 12-18 | Observation unit and inspection |
| 18-28 | Selection with brackets, `.loc[]`, and `.iloc[]` |
| 28-38 | Boolean masks, combined conditions, and sorting |
| 38-47 | Repository activity final request |
| 47-50 | Debrief and exit check |

When time is short:

- Treat label alignment as a quick prediction rather than a full discussion.
- Show the answer to `Predict the result` after collecting two verbal answers.
- Mention `.isin()` without working through an additional example.
- Move directly from one-column sorting to multi-column sorting.
- Complete activity checkpoints 1 through 4 together, then let students solve
  the final request in pairs.
- Show the completed result table during the debrief.

## Activity flow

Students should work from:

```text
activity/pandas-foundations.qmd
```

The corresponding completed file is:

```text
activity/pandas-foundations-complete.qmd
```

Suggested checkpoints:

1. Everyone confirms that the full table has shape `(794, 14)`.
2. Pause after the one-column selections and compare object types and shapes.
3. Pause after `recent_mask` and ask what one `True` means.
4. Confirm that `recent_talks` has shape `(201, 5)`.
5. Ask students to explain why year has priority in the two-column sort.
6. Let pairs complete and check the final request.

## Key results

| Check | Expected result |
|:---|:---|
| Complete dataset shape | `(794, 14)` |
| Talks from 2018 through 2020 | 201 |
| `recent_talks` shape | `(201, 5)` before adding the new column |
| Median word count from 2018 through 2020 | 1,650 |
| Rows in the final request | 6 |
| Final ordering | 2020 before 2019, then descending word count within year |

The five largest word counts from 2018 through 2020 are:

| Talk | Speaker | Words |
|:--|:--|--:|
| Hear Him | Russell M. Nelson | 2591 |
| A Home Where the Spirit of the Lord Dwells | Henry B. Eyring | 2247 |
| Shall We Not Go On in So Great a Cause? | M. Russell Ballard | 2234 |
| Inspired Ministering | Henry B. Eyring | 2217 |
| Your Priesthood Playbook | Gary E. Stevenson | 2202 |

## Likely misconceptions

### A DataFrame has one data type

A DataFrame can contain columns with different data types. Each Series has a
data type. Avoid describing the entire table as one homogeneous NumPy array.

### One selected column always remains a DataFrame

`df["column"]` returns a Series. `df[["column"]]` returns a one-column
DataFrame. Ask students to predict dimensions whenever the distinction matters.

### `.loc[1]` means the second row

`.loc[]` interprets values as labels. `.iloc[]` interprets integers as
positions. Use the named score index to keep the difference visible.

### A Boolean condition immediately filters the table

A comparison first produces a Boolean Series. The mask can be inspected,
counted, combined, and then supplied to `.loc[]`.

### Python `and` and `or` combine row conditions

Pandas needs elementwise `&` and `|` so that it can combine one Boolean value
per row. Parenthesize every comparison.

### Sorting changes which rows qualify

Filtering controls membership. Sorting controls order. The row count should
stay the same after sorting.

### The largest value always appears first in a multi-column sort

The first sorting column has priority. Later columns order rows only within
ties on earlier columns.

### `head()` can come before sorting

Taking `head()` first discards all but the current first rows. Sort before
taking the first five when the request asks for the five largest values.

### Chained assignment updates the original table

With pandas 3 Copy-on-Write, chained assignment never updates the original
object. Use one `.loc[]` operation for conditional assignment. An explicit
`.copy()` can still communicate that a filtered result is an independent
working table.

## Speaker notes

Every slide includes a RevealJS notes block with timing, questions, expected
answers, and optional cuts. Press `S` during the rendered presentation to open
speaker view.

