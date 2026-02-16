import os
from py_snap_code import CodeConverter

def run_test():
    """
    A simple test script to verify that PySnapCode is working correctly.
    It creates a dummy Python file, converts it to an image, and then cleans up.
    """
    
    # 1. Create a dummy Python file for testing
    test_file_name = 'demo_script.py'
    test_code = """# This is a test file for PySnapCode
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("World")
    x = 42
    operators = [+, -, *, /]
"""
    
    with open(test_file_name, 'w', encoding='utf-8') as f:
        f.write(test_code)

    print(f"[*] Created temporary file: {test_file_name}")

    # 2. Initialize the converter
    # Note: Replace the poppler_path with your actual path if it's not in your System PATH
    # conv = CodeConverter(poppler_path=r'C:\path\to\your\poppler\bin')
    conv = CodeConverter() 

    print("[*] Starting conversion...")

    try:
        # 3. Perform the conversion
        output_base_name = 'test_output'
        conv.convert(test_file_name, output_name=output_base_name)
        
        # Check if the output image was created
        expected_output = f"{output_base_name}_0.jpg"
        if os.path.exists(expected_output):
            print(f"[SUCCESS] Image generated: {expected_output}")
        else:
            print("[FAILED] Conversion finished but no image was found.")

    except Exception as e:
        print(f"[ERROR] An error occurred during test: {e}")
        print("Make sure Poppler and wkhtmltopdf are installed correctly.")
        print("Check: https://youtu.be/PyF1Vh9040Y for help.")

    finally:
        # 4. Cleanup temporary test file
        if os.path.exists(test_file_name):
            os.remove(test_file_name)
            print(f"[*] Cleaned up: {test_file_name}")

if __name__ == "__main__":
    run_test()