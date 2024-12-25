import re
import csv

#task 1 
content = open('task1-en.txt').read()

words_with_hyphens = re.findall(r'\b\w+-\w+\b', content) # Find words with hyphens
text_in_parentheses = re.findall(r'\((.*?)\)', content)  # Find information in parentheses

# result's output
print("words with hyphens:", words_with_hyphens)
print("information in parentheses:", text_in_parentheses)


# task 2
content2 = open('task2.html', 'r', encoding='utf-8').read() # Reading HTML file

sites = re.findall(r'\bhttps?://[^\s/$.?#].[^\s]*\.com\b', content2) # Regular expression to find links with .com domain
print(sites)


# task 3
content3 = open('task3.txt').read()  # Reading file

# Regular expressions for data search
surname = re.findall(r'[A-Z][a-z]+', content3)
mail = re.findall(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]', content3)
date = re.findall(r'\d{4}-\d{2}-\d{2}', content3)
website = re.findall(r'https?://[a-zA-Z0-9.-]+/', content3)

id_list = []
id = 1
while True:
    if str(id) in content3:
        id_list.append(id)
        id+=1
    else:
        break

table = []

for i in range(len(id_list)):
    table.append([id_list[i], surname[i], mail[i], date[i],website[i]])

with open('lab5_task3.csv', 'w') as file4:
    written = csv.writer(file4)

    written.writerow(['id', 'surname', 'mail', 'date', 'website'])

    written.writerows(table)

print('The table was created in the file lab5_task3.csv.')
