import keyword
import pdfkit
import pdf2image
import os
from PIL import Image, ImageChops

class CodeConverter:
    def __init__(self, poppler_path=None, custom_colors=None, font_size="14px"):
        """
        Initialize the PySnapCode converter.
        :param poppler_path: Path to the 'bin' folder of Poppler.
        :param custom_colors: Dictionary to customize theme colors.
        :param font_size: CSS font size (e.g., '16px').
        """
        # Default Theme (Dark)
        self.colors = {
            'bg': '#1e1e1e',
            'text': '#d4d4d4',
            'keywords': '#569cd6',
            'operators': '#d4d4d4',
            'numbers': '#b5cea8',
            'else': '#ce9178',
            'line_num': '#858585'
        }
        
        if custom_colors:
            self.colors.update(custom_colors)
            
        self.font_size = font_size
        self.keywords = keyword.kwlist
        self.operators = ['+', '-', '=', '*', '/', '%', '(', ')', '[', ']', ':', ',']
        self.poppler_path = poppler_path

    def _line_process(self, line):
        """Wraps code elements in HTML spans with inline styles."""
        line = line.replace('\t', '&nbsp; &nbsp; ')
        line_words = line.replace('\n', '').split(' ')
        words = []
        
        for word in line_words:
            if not word: 
                words.append('&nbsp;')
                continue
            
            clean_word = word.strip('():,[]') 
            
            if clean_word in self.keywords:
                words.append(f'<span style="color:{self.colors["keywords"]}; font-weight:bold;">{word}</span>')
            elif any(op in word for op in self.operators):
                words.append(f'<span style="color:{self.colors["operators"]};">{word}</span>')
            elif word.isdigit():
                words.append(f'<span style="color:{self.colors["numbers"]};">{word}</span>')
            else:
                words.append(f'<span style="color:{self.colors["else"]};">{word}</span>')
        return words

    def _trim_image(self, img):
        """Crops the image to the code content and adds padding."""
        bg = Image.new(img.mode, img.size, img.getpixel((0,0)))
        diff = ImageChops.difference(img, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            cropped = img.crop(bbox)
            # Create a new image with padding using the background color
            final_img = Image.new(img.mode, (cropped.width + 40, cropped.height + 40), self.colors['bg'])
            final_img.paste(cropped, (20, 20))
            return final_img
        return img

    def convert(self, file_path, output_name='PySnap_Shot'):
        """Main method to convert .py file to auto-cropped image."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Source file '{file_path}' not found.")

        # Read the source code
        with open(file_path, 'r', encoding='utf-8') as f:
            code_lines = f.readlines()

        # Process lines into HTML
        processed_lines = [' '.join(self._line_process(line)) for line in code_lines]

        # Build HTML Structure
        html_content = f"""
        <html><head><style>
            body {{ 
                background-color: {self.colors['bg']}; 
                color: {self.colors['text']}; 
                font-family: 'Courier New', monospace; 
                font-size: {self.font_size};
                padding: 20px; 
                line-height: 1.5;
                display: inline-block;
            }}
            .line-num {{ 
                color: {self.colors['line_num']}; 
                margin-right: 15px; 
                display: inline-block; 
                width: 35px; 
                text-align: right; 
                border-right: 1px solid {self.colors['line_num']};
                padding-right: 10px;
                user-select: none;
            }}
            div {{ white-space: nowrap; }}
        </style></head><body>
        """
        for i, line in enumerate(processed_lines):
            html_content += f'<div><span class="line-num">{i + 1}</span>{line}</div>'
        html_content += "</body></html>"

        temp_html = "temp_snap.html"
        temp_pdf = "temp_snap.pdf"
        
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(html_content)

        try:
            # Generate PDF using PDFkit
            options = {
                'margin-top': '0', 'margin-right': '0', 'margin-bottom': '0', 'margin-left': '0',
                'encoding': "UTF-8", 'quiet': ''
            }
            pdfkit.from_file(temp_html, temp_pdf, options=options)
            
            # Convert PDF to Images
            images = pdf2image.convert_from_path(
                temp_pdf, 
                poppler_path=self.poppler_path
            )
            
            for i, img in enumerate(images):
                final_result = self._trim_image(img)
                final_result.save(f"{output_name}_{i}.jpg")
                
            print(f"Successfully generated images with prefix: {output_name}")
            
        except Exception as e:
            # Check for common Poppler errors
            if "poppler" in str(e).lower() or "pdf2image" in str(e).lower():
                print("\n" + "="*60)
                print("[!] Error: Poppler not found or incorrectly configured.")
                print("To fix this, please follow the setup guide in this video:")
                print("👉 https://youtu.be/PyF1Vh9040Y") # Your YouTube link
                print("="*60 + "\n")
            else:
                print(f"An unexpected error occurred: {e}")
        finally:
            # Cleanup temporary files
            if os.path.exists(temp_html): os.remove(temp_html)
            if os.path.exists(temp_pdf): os.remove(temp_pdf)


