from setuptools import setup, find_packages

setup(
    name="PySnapCode",
    version="0.1.1",
    author="Free Python Code",
    description="Convert source code into beautiful syntax-highlighted and auto-cropped images",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'pdfkit',
        'pdf2image',
        'Pillow'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)