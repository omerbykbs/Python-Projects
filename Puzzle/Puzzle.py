import shutil
import re
import os

# Unzipping the zip file
shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')

# Reading the instructions content
with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

# Designing pattern for searched number
pattern = r'\d{3}-\d{3}-\d{4}'

# Function for searching designed pattern in files
def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''

# Getting the complete path for searching files
path_for_search = os.getcwd()+'/extracted_content'

# Defining a result list for adding found items while searching
results = []

# Searching into folders and files
for folder, subfolder, files in os.walk(path_for_search):

    for file in files:
        if (file == '.DS_Store'):
            continue
        else:
            path = folder + f"/{file}"
            results.append(search(path))

# Variable for decoded number
decoded = ''

# Getting decoded number from results list
for r in results:
    if r != '':
        decoded = r.group()

print(f"Searched number is: {decoded}")