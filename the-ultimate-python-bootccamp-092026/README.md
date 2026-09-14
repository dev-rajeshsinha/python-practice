# The Ultimate Python Bootcamp

This folder contains my notes, exercises, experiments, and other practice code
from **The Ultimate Python Bootcamp** online course.

## Course workspace

The course workspace currently contains:

- A local Python virtual environment in `.venv/`.
- A `src/` directory for executable Python exercises.
- `requirements.txt` for course dependencies. It is currently empty because no
  third-party packages are required by the exercises in this folder yet.
- `resources.txt` for links and other supporting course material.

The course work is intentionally incremental. New lessons and exercises should
be added under `src/` using descriptive, lesson-oriented filenames, while
course-specific links, setup notes, and other references should be added to the
appropriate supporting file in this folder. |

### Concepts covered so far

- **Strings:** Strings support indexing and slicing, but string methods return
  transformed values because strings cannot be changed in place. The exercise
  also compares formatting, search, classification, and case-related methods.
- **Lists:** Lists are ordered and mutable. The exercise contrasts slicing and
  list-building expressions with methods such as `insert()`, `pop()`,
  `append()`, `remove()`, `extend()`, and `clear()`.
- **Tuples:** Tuples are ordered collections that support indexing and slicing.
  The current exercise focuses on reading and deriving values from a tuple.
- **Sets:** Sets store unique values and support mathematical operations such as
  union, intersection, difference, and symmetric difference. They also support
  relationship checks including subset, superset, equality, and disjointness.
- **Frozensets:** Frozensets provide the set operations shown above while being
  immutable. The current exercise therefore focuses on operations that produce
  values rather than mutating methods.
- **Dictionaries:** Dictionaries map keys to values. The exercise covers both
  direct access and the safer `get()` method with fallback values, followed by
  common update and removal operations.
- **Object identity:** Several exercises print `id()` values to make it easier
  to observe whether an operation creates a new object or changes an existing
  one.
- **Boolean and numeric values in collections:** The examples intentionally use
  mixed values such as integers, floats, booleans, strings, and `None` to
  explore how Python represents common built-in data types together.

## Folder structure

```text
the-ultimate-python-bootccamp-092026/
├── README.md
├── requirements.txt
├── resources.txt
├── src/
│   ├── 01_version_check.py
│   ├── 01_zen_of_python.py
│   ├── 02_dictionary_operations.py
│   ├── 02_frozensets.py
│   ├── 02_list_operations.py
│   ├── 02_mutability.py
│   ├── 02_set_operations.py
│   ├── 02_string_operations.py
│   └── 02_tuple_operations.py
└── .venv/                 # Local virtual environment; generated, not source
```

The course folder name is kept as created in the repository. The numeric suffix
is a timestamp identifying when this course workspace was started, using the
`MMYYYY` format. It helps distinguish this workspace from future course folders
and other passes through the material.

## Getting started

From this directory, create or activate the local virtual environment before
running exercises:

```bash
cd the-ultimate-python-bootccamp-092026

# Create the environment if it does not already exist.
python3 -m venv .venv

# Activate it on Linux or macOS.
source .venv/bin/activate

# Install dependencies when requirements.txt contains packages.
python -m pip install -r requirements.txt
```

On Windows PowerShell, the activation command is:

```powershell
.venv\Scripts\Activate.ps1
```

Because the current requirements file is empty, the exercises presently use
only Python's standard library. The virtual environment still provides an
isolated interpreter for this course workspace.

## Running the exercises

Run the scripts from the course folder with the active environment:

```bash
python src/01_version_check.py
python src/01_zen_of_python.py
```

The first command reports the interpreter being used. This is a useful quick
check when returning to the course after switching Python installations or
recreating the virtual environment. The remaining commands print examples and
observations for the corresponding Python data type or language concept.

To run every exercise in the current workspace from Linux or macOS:

```bash
for exercise in src/*.py; do
  python "$exercise"
done
```

The output order from set and frozenset examples can vary because these
collections are unordered. The exact object IDs also vary between runs and
Python processes; they are included to illustrate identity, not as fixed
expected values.

## Working conventions

- Keep all code written for this course inside this course folder.
- Place runnable Python exercises in `src/`.
- Use numbered filenames when the order of the lessons or exercises matters.
- Keep each exercise focused on the concept being practiced.
- Add every new exercise to the current progress table and folder tree.
- Add a short explanation here when a new group of exercises introduces an
  important Python concept.
- Add third-party packages to `requirements.txt` as the course begins to use
  them.
- Keep external links and course references in `resources.txt`.
- Do not treat `.venv/` as course source code; it is a locally generated
  environment used to run the exercises.

## Next steps

As I continue through the course, this README should grow with the workspace.
Useful updates include:

- Updating `requirements.txt` when external packages are introduced.
- Adding new course notes and references to `resources.txt`.
- Documenting any commands or environment details needed to reproduce the
  exercises.
