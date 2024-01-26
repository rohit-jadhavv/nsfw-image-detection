

file_name = "urls_example.txt"

# Chaining replace() to remove both '.txt' and 'urls_'
new_name = file_name.replace('.txt', '').replace('urls_', '')

print(new_name)
