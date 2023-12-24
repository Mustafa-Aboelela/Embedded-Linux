from openpyxl import Workbook

# Create a new workbook
workbook = Workbook()

# Select the active sheet
sheet = workbook.active

# Writing data to specific cells
sheet['A1'] = 'Hello'
sheet['B1'] = 'mannnnnnn'


# Writing data in a loop
data = [
    ['Name', 'Age', 'Country'],
    ['Ahmed', 25, 'fayoum'],
    ['diaa', 30, 'cairo'],
    ['mustafa', 28, 'giza']
]

for row in data:
    sheet.append(row)

# Save the workbook
workbook.save('hello.xlsx')  # Save the workbook with the name 'hello.xlsx'

# Close the workbook
workbook.close()
