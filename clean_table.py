from bs4 import BeautifulSoup

# Open the input HTML file and read its contents
with open('input.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all <a> tags in the HTML file
for a in soup.find_all('a'):
    # Replace the <a> tag with its inner text
    a.replace_with(a.text)

# Find all the <tbody> elements in the HTML file
tbodies = soup.find_all('tbody')

# Create a new <tbody> element to hold the combined table rows
combined_tbody = soup.new_tag('tbody')

# Loop through each <tbody> element and append its contents to the combined <tbody> element
for tbody in tbodies:
    for tr in tbody.find_all('tr'):
        combined_tbody.append(tr)

# Remove the original <tbody> elements from the HTML file
for tbody in tbodies:
    tbody.decompose()

# Add the combined <tbody> element to the first <table> element in the HTML file
table = soup.find('table')
table.append(combined_tbody)

# Get the updated HTML string
updated_html = str(soup)

# Open the output file and write the updated HTML to it
with open('output.html', 'w') as file:
    file.write(updated_html)
