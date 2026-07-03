# Random PDF/TXT Document Generator

A lightweight Python tool for generating random document files in PDF or TXT format. It creates pseudo-academic or report-style documents with randomized titles, sections, paragraphs, connector phrases, filler phrases, and optional tables.

This project is useful for testing document upload flows, checking PDF/TXT handling, validating storage pipelines, and creating placeholder files for development environments.

> **Responsible use:** This tool is intended for testing, development, demo, and personal automation workflows only. Do not use generated documents to mislead readers, impersonate real academic work, spam document-sharing platforms, bypass moderation systems, or violate the terms of services of platforms such as Scribd, Studocu, or similar websites.

## Features

- Generate multiple files in one run.
- Output as PDF or TXT.
- Randomize document length between 5 and 10 pages by default.
- Create report-style content with:
  - document titles,
  - section headings,
  - paragraphs,
  - Vietnamese and English connector phrases,
  - filler phrases,
  - optional tables.
- Automatically generate safe, lowercase filenames from document titles.
- Add random suffixes to filenames to reduce name collisions.
- Use Unicode-friendly fonts when available for PDF output.
- Save all generated files into a configurable output directory.

## Requirements

Python 3.8 or later is recommended.

For PDF output, install `reportlab`:

```bash
pip install reportlab
```

TXT output does not require additional third-party packages.

## Installation

Clone or download this project, then place the Python script in your working directory.

```bash
git clone https://github.com/Mashirochi/Random-PDF-TXT-Document-Generator
cd Random-PDF-TXT-Document-Generator
pip install reportlab
```

If you are not using Git, simply copy the Python file into a folder and run it directly.

## Configuration

Edit the configuration section at the top of the script:

```python
FILE_COUNT = 10        # Number of files to generate
PAGES = None           # None = random 5-10 pages, or set a fixed number
OUTPUT_FORMAT = "pdf"  # "pdf" or "txt"
OUTPUT_NAME = None     # Example: "report.pdf" when generating one file
OUTPUT_DIR = "output"  # Output folder
```

### Options

| Option          | Description                                             | Example               |
| --------------- | ------------------------------------------------------- | --------------------- |
| `FILE_COUNT`    | Number of files to generate                             | `10`                  |
| `PAGES`         | Fixed number of pages. Use `None` for random 5-10 pages | `7`                   |
| `OUTPUT_FORMAT` | Output format                                           | `"pdf"` or `"txt"`    |
| `OUTPUT_NAME`   | Custom filename when generating a single file           | `"sample_report.pdf"` |
| `OUTPUT_DIR`    | Folder where generated files will be saved              | `"output"`            |

## Usage

Run the script with Python:

```bash
python main.py
```

The generated files will be saved in the configured output directory, for example:

```text
output/
├── bao_cao_phan_tich_du_lieu_ban_hang_a1b2.pdf
├── tong_quan_cong_nghe_dien_toan_dam_may_c3d4.pdf
└── tai_lieu_hoc_tap_lap_trinh_python_nang_cao_e5f6.pdf
```

## Generate PDF Files

Set:

```python
OUTPUT_FORMAT = "pdf"
```

Then run:

```bash
python main.py
```

PDF output requires `reportlab`.

## Generate TXT Files

Set:

```python
OUTPUT_FORMAT = "txt"
```

Then run:

```bash
python main.py
```

The TXT files will contain section headings, paragraphs, and plain-text tables when tables are generated.

## Generate a Single File With a Custom Name

Set:

```python
FILE_COUNT = 1
OUTPUT_NAME = "demo_document.pdf"
OUTPUT_FORMAT = "pdf"
```

Then run:

```bash
python main.py
```

When `FILE_COUNT` is greater than `1`, `OUTPUT_NAME` is ignored and filenames are generated automatically.

## Output Structure

Each generated document may include:

1. A random document title.
2. Multiple numbered sections.
3. Several random paragraphs per section.
4. Optional tables with randomized headers and rows.
5. Auto-generated metadata such as page count, section count, and unique word count internally.

## Example Console Output

```text
[OK] [1/10] Đã lưu: output/tong_quan_cong_nghe_dien_toan_dam_may_a1b2.pdf (8 trang)
[OK] [2/10] Đã lưu: output/bao_cao_kiem_thu_bao_mat_web_c3d4.pdf (6 trang)
[OK] [3/10] Đã lưu: output/tai_lieu_docker_cho_nguoi_moi_e5f6.pdf (10 trang)
```

## Project Structure

```text
.
├── main.py
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── output/
```

## Notes

- Generated content is random and does not represent real research, real academic work, or verified information.
- PDF generation uses available system fonts when possible to improve Unicode support.
- The script creates the output directory automatically if it does not already exist.
- Random filenames include a short hash suffix to reduce duplicate filename issues.

## Ethical and Platform Compliance Notice

Before uploading generated files to any third-party platform, make sure your use case follows that platform's rules and policies. Some platforms may prohibit automatically generated, low-quality, duplicate, misleading, or non-original content.

Use this tool for legitimate purposes such as:

- testing upload features,
- testing PDF parsers,
- creating placeholder documents,
- internal QA workflows,
- demo environments,
- local development.

Do not use it for:

- fake academic submissions,
- misleading study materials,
- SEO spam,
- mass-upload abuse,
- monetization fraud,
- violating platform terms.

## Troubleshooting

### `ModuleNotFoundError: No module named 'reportlab'`

Install ReportLab:

```bash
pip install reportlab
```

### PDF text does not display Vietnamese characters correctly

Make sure your system has a Unicode-compatible font installed, such as DejaVu Sans, Liberation Sans, FreeSans, Ubuntu, Arial, or another font that supports Vietnamese characters.

### Output folder is empty

Check that:

- the script ran without errors,
- `OUTPUT_DIR` is set correctly,
- you have write permission in the target directory,
- `OUTPUT_FORMAT` is either `"pdf"` or `"txt"`.

## License

This project is provided for educational, testing, and development purposes. Add your preferred license before publishing it publicly.
