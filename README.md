# PySnapCode

PySnapCode is a lightweight Python library designed to transform your source code into beautiful, syntax-highlighted, and auto-cropped images. It is the perfect tool for sharing code snippets on social media, technical blogs, or project documentation.

---

## Prerequisites (Mandatory)

To ensure this library functions correctly, you must install the following two external dependencies.

### Installation Guide
If you need help setting up these dependencies, follow this step-by-step video tutorial:
**[View Tutorial on YouTube](https://youtu.be/PyF1Vh9040Y)**

### 1. Poppler (Required for Image Generation)
* **Windows:** Download the latest version from the [Poppler for Windows Releases](https://github.com/oschwartz10612/poppler-windows/releases/).
* **Setup:** Extract the ZIP file and copy the path to the `bin` folder. You will need to provide this path in your Python script.

### 2. wkhtmltopdf (Required for PDF Rendering)
* **Download:** Get the installer from the [official wkhtmltopdf website](https://wkhtmltopdf.org/downloads.html).
* **Setup:** Run the installer. It is highly recommended to add it to your system PATH during the installation process.

---

## Installation

You can install PySnapCode directly from PyPI using pip:

```bash
pip install PySnapCode


### Usage
Basic Example
This example shows how to convert a Python file using the default dark theme.

```python
from py_snap_code import CodeConverter

# Initialize the converter with your Poppler bin path
conv = CodeConverter(poppler_path=r'C:\path\to\your\poppler\bin')

# Convert your python file to a cropped image
conv.convert('main.py', output_name='my_code_snap')
```


### Advanced Customization
You can fully customize the colors and font size to match your personal style or brand.

```python
from py_snap_code import CodeConverter

# Define a custom theme (e.g., Dracula-inspired)
my_theme = {
    'bg': '#282a36',        # Background color
    'text': '#f8f8f2',      # Primary text color
    'keywords': '#ff79c6',  # Python keywords
    'numbers': '#bd93f9',   # Numbers
    'line_num': '#6272a4'   # Line numbers color
}

conv = CodeConverter(
    poppler_path=r'C:\poppler\bin',
    custom_colors=my_theme,
    font_size="18px"
)

conv.convert('script.py', output_name='pro_snippet')

```
### Key Features
Auto-Crop: Automatically detects the code area and trims excess white space.

Syntax Highlighting: Built-in support for standard Python keywords and operators.

Theming Engine: Full control over background, text, and highlighting color palettes.

Professional Padding: Adds clean, consistent padding around your code for a better visual look.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Support & Donations
If you find this library helpful and want to support its development, you can buy me a coffee here:

[![Support me on Ko-fi](https://img.shields.io/badge/Support%20Me-Ko--fi-F16061?style=flat-square&logo=ko-fi)](https://ko-fi.com/freepythoncode)

**[Donate via Ko-fi](https://ko-fi.com/freepythoncode)**