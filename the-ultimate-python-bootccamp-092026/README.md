# The Ultimate Python Bootcamp

This folder contains my notes, exercises, experiments, and other practice code
from the **The Ultimate Python Bootcamp** online course.

## Course workspace

The course workspace currently contains:

- A local Python virtual environment in `.venv/`.
- A `src/` directory for executable Python exercises.
- `requirements.txt` for course dependencies. It is currently empty because no
  third-party packages are required by the exercises in this folder yet.
- `resources.txt` for links and other supporting course material.

The course work is intentionally incremental. New lessons and exercises should
be added under `src/` using descriptive filenames, while course-specific links,
setup notes, and other references should be added to the appropriate supporting
file in this folder.

## Folder structure

```text
the-ultimate-python-bootccamp-092026/
├── README.md
├── requirements.txt
├── resources.txt
├── src/
│   ├── 01_version_check.py
│   └── 01_zen_of_python.py
└── .venv/                 # Local virtual environment; generated, not source
```

The course folder name is kept as created in the repository. The numeric suffix (Timestamp when the course was started in MMYYYY format)
helps distinguish this course workspace from future course folders and other
passes through the material.

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
recreating the virtual environment.

## Course resources

The current external course resource is recorded in [`resources.txt`](resources.txt):

- [Course whiteboard](https://app.eraser.io/workspace/xltiZYV3fLYZuUEtfUal)

Additional links should be added to `resources.txt` rather than mixed into the
exercise files.

## Working conventions

- Keep all code written for this course inside this course folder.
- Place runnable Python exercises in `src/`.
- Use numbered filenames when the order of the lessons or exercises matters.
- Keep each exercise focused on the concept being practiced.
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
