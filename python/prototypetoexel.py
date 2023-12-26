import re
from openpyxl import Workbook

def parse_header_file(header_file):
    with open(header_file, 'r') as file:
        content = file.read()

        # Regular expression pattern to match function prototypes
        pattern = r'\b([\w*]+)\s+([\w]+)\s*\([^)]*\)\s*;'

        # Find all function prototypes in the header file
        function_prototypes = re.findall(pattern, content)

        return function_prototypes

def write_to_excel(function_prototypes):
    # Create a new workbook
    wb = Workbook()
    sheet = wb.active

    # Add headers to the Excel sheet
    sheet.append(['Unique ID', 'Return Type', 'Function Name'])

    # Write function prototypes to the Excel sheet with unique IDs
    for idx, (return_type, function_name) in enumerate(function_prototypes, start=1):
        unique_id = f'IDX{idx}'
        sheet.append([unique_id, return_type, function_name])

    # Save the workbook to a file
    wb.save('function_prototypes.xlsx')
    print("Function prototypes written to function_prototypes.xlsx")

if __name__ == "__main__":
    header_file_path = '/home/mustafa_mohamed/Downloads/Telegram/DIO_interface.h'  # Replace with the path to your header file
    prototypes = parse_header_file(header_file_path)
    if prototypes:
        write_to_excel(prototypes)
    else:
        print("No function prototypes found in the header file.")