# STAT 386: pandas Foundations

This repository contains the materials for the STAT 386 class on pandas
foundations. It follows the NumPy lesson and carries forward shape,
vectorization, indexing, and Boolean masks into labeled tabular data.

The class uses a condensed General Conference dataset that students encounter
again in Lab 3. The in-class activity moves from inspection and object type
predictions to filtering, column selection, derived variables, and
multi-column sorting.

## Repository contents

```text
stat-386-pandas-foundations/
├── activity/
│   ├── pandas-foundations.qmd
│   └── pandas-foundations-complete.qmd
├── data/
│   └── talks.csv
├── docs/
│   └── rendered website published by GitHub Pages
├── slides/
│   ├── pandas-foundations.qmd
│   └── theme.scss
├── src/
│   └── pandas_demo.py
├── .gitignore
├── .python-version
├── _quarto.yml
├── INSTRUCTOR_GUIDE.md
├── index.qmd
├── pyproject.toml
└── README.md
```

- `slides/pandas-foundations.qmd` contains the RevealJS lecture and speaker
  notes.
- `activity/pandas-foundations.qmd` is the student walkthrough used in class.
- `activity/pandas-foundations-complete.qmd` contains a completed walkthrough.
- `src/pandas_demo.py` runs the completed analysis and verifies key results.
- `INSTRUCTOR_GUIDE.md` contains pacing, checkpoints, expected results, and
  likely misconceptions.

## Student setup

### 1. Fork and clone the repository

Fork the repository on GitHub, then clone your fork:

```bash
git clone https://github.com/YOUR-USERNAME/stat-386-pandas-foundations.git
cd stat-386-pandas-foundations
```

### 2. Create the environment

```bash
uv sync
```

This creates a `.venv` directory and installs the packages listed in
`pyproject.toml`.

### 3. Open the walkthrough

Open `activity/pandas-foundations.qmd` in Positron. Select the Python
interpreter from `.venv` if Positron does not select it automatically.

Run the cells as the class works through the activity. Each unfinished cell
contains a `TODO` comment. The completed file is available for recovery or for
students who miss class.

## Running the completed Python demonstration

```bash
uv run python src/pandas_demo.py
```

The script prints the two main ordered results and checks their shapes and
filtering conditions.

## Rendering the Quarto website

The repository is a Quarto website project. Quarto must be installed
separately. Render the whole site into `docs/`:

```bash
quarto render
```

Quarto automatically uses the project `.venv` created by `uv sync` to execute
the activity code cells. To preview while editing:

```bash
quarto preview
```

## Publishing to GitHub Pages

GitHub Pages serves the site from the `docs/` folder on the default branch.
After editing the materials, re-render and push:

```bash
quarto render
git add docs
git commit -m "Render site"
git push
```

## Instructor guidance

The lecture deck contains speaker notes in RevealJS notes blocks. Press `S`
while presenting the rendered deck to open speaker view.

The planned deck contains about 70 minutes of material. A compressed pacing
option appears in `INSTRUCTOR_GUIDE.md`.

