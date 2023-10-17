import csv
import re
import PyPDF2

# Puzzle 1: Extracting the hidden Google Drive link from the find_the_link.csv file

data = open('find_the_link.csv')
csv_reader = csv.reader(data)
data_lines = list(csv_reader)

link = ''

for i in range(len(data_lines)):
    link += data_lines[i][i]

print(f"Hidden link is: {link}")
data.close()

# Puzzle 2: Finding hidden phone number in Find_the_Phone_Number.pdf file

pdf_reader = PyPDF2.PdfFileReader(f)

pdf_text = ''

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text = pdf_text + " " + page.extract_text()

## First finding out how the format of phone number is
pattern = r"\d{3}"
re.findall(pattern,pdf_text)

## Getting the numbers location and printing some text to see how the format is
for match in re.finditer(pattern,pdf_text):
    print(match)

pdf_text[42919:42922+17]

## Using the format as new pattern and getting the phone number
new_pattern = r"\d{3}.\d{3}.\d{4}" 
phone = re.search(pattern,pdf_text)
phone = phone.group()
phone = phone.replace('.',' ')
print(f"Hidden phone number is: {phone}")