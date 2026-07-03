# Contributing Guide

Thank you for your interest in contributing to **Random PDF/TXT Document Generator**.

This project is a lightweight Python tool that generates random placeholder documents in PDF or TXT format. It is intended for development, testing, demos, QA workflows, and local automation. Please keep all contributions aligned with responsible and lawful use.

## Responsible Use

This project must not be used to mislead readers, create fake academic work, spam document-sharing platforms, bypass moderation systems, or violate the terms of service of platforms such as Scribd, Studocu, or similar services.

Contributions that add or encourage the following will not be accepted:

- automated mass-upload workflows,
- platform abuse or spam features,
- fake academic submission workflows,
- bypassing upload limits, detection, or moderation,
- misleading metadata intended to impersonate real authors, schools, or institutions,
- monetization fraud or deceptive content distribution.

Good use cases include:

- testing PDF/TXT upload flows,
- checking document parsing pipelines,
- creating placeholder files for demos,
- validating storage systems,
- testing Unicode text rendering,
- internal QA and development workflows.

## Ways to Contribute

You can contribute by improving:

- documentation and usage examples,
- code readability and structure,
- PDF formatting and layout,
- TXT output quality,
- configuration options,
- error handling,
- cross-platform font support,
- tests and validation scripts,
- packaging and installation instructions.

## Development Setup

1. Fork the repository.
2. Clone your fork:

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment:

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

5. Install the PDF dependency:

```bash
pip install reportlab
```

TXT generation does not require third-party packages.

## Running the Project

Run the script with Python:

```bash
python generate_documents.py
```

Generated files will be saved in the configured output directory, usually:

```text
output/
```

Before submitting changes, test both output formats:

```python
OUTPUT_FORMAT = "pdf"
```

and:

```python
OUTPUT_FORMAT = "txt"
```

Also test both single-file and multi-file generation:

```python
FILE_COUNT = 1
OUTPUT_NAME = "sample_document.pdf"
```

and:

```python
FILE_COUNT = 10
OUTPUT_NAME = None
```

## Code Style Guidelines

Please keep the code simple and beginner-friendly.

Recommended style:

- Use clear function names.
- Keep configuration options easy to edit.
- Avoid unnecessary dependencies.
- Preserve compatibility with Python 3.8 or later when possible.
- Keep generated output files out of version control.
- Add comments only where they make the logic easier to understand.
- Avoid hard-coded local paths unless they are platform checks for fonts.

## Documentation Guidelines

When updating documentation:

- Write in clear English.
- Include short examples where useful.
- Explain configuration options clearly.
- Mention whether a feature affects PDF output, TXT output, or both.
- Keep responsible-use notes visible.

## Testing Checklist

Before opening a pull request, please check that:

- PDF generation works when `reportlab` is installed.
- TXT generation works without extra dependencies.
- Output files are created in the configured output directory.
- Vietnamese text renders correctly where supported by system fonts.
- Multiple files generate without filename conflicts.
- A single custom output name works when `FILE_COUNT = 1`.
- No generated PDF/TXT files are committed accidentally.

## Pull Request Process

1. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

2. Make your changes.
3. Test the project locally.
4. Commit your changes with a clear message:

```bash
git commit -m "Improve PDF table formatting"
```

5. Push your branch:

```bash
git push origin feature/your-feature-name
```

6. Open a pull request and describe:

- what changed,
- why the change is useful,
- how you tested it,
- any limitations or follow-up work.

## Commit Message Examples

Good commit messages:

```text
Add TXT table formatting tests
Improve Unicode font fallback
Update README usage examples
Refactor document generation functions
```

Avoid vague messages such as:

```text
update
fix stuff
changes
final version
```

## Reporting Issues

When opening an issue, please include:

- your operating system,
- Python version,
- whether you are generating PDF or TXT files,
- the configuration values you used,
- the error message or unexpected behavior,
- steps to reproduce the problem.

Example:

```text
OS: Windows 11
Python: 3.11
Output format: PDF
FILE_COUNT: 10
PAGES: None
Issue: Vietnamese characters do not render correctly in the generated PDF.
```

## Security and Abuse Reports

If you notice a feature, issue, or workflow that could enable abuse, spam, deception, or platform-policy violations, please report it clearly. Contributions that improve safeguards, transparency, or responsible-use messaging are welcome.

## License

By contributing, you agree that your contributions will be released under the same license as the project. If the project does not have a license yet, add one before publishing the repository publicly.
