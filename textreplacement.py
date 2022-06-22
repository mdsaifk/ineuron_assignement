# Create one example.txt file 
search_text = "Placement"
replace_text = "Screening"

with open(r'example.txt', 'r') as file:
	data = file.read()
	data = data.replace(search_text, replace_text)
with open(r'example.txt', 'w') as file:
    file.write(data)

# Printing Text replaced
print("Text is replaced")
