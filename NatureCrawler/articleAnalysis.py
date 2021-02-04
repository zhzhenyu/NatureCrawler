import json
import collections

f = open('article.json')
data = json.load(f)

titles = []
authors = []
subjects = []

minLenTitle, maxLenTitle = float('inf'), float('-inf')
shortTitle, longTitle = "", ""

for entry in data:
    titles.append(entry['title'])
    if len(entry['title']) < minLenTitle:
        minLenTitle = len(entry['title'])
        shortTitle = entry['title']
    if len(entry['title']) > maxLenTitle:
        maxLenTitle = len(entry['title'])
        longTitle = entry['title']

    authors.append(entry['author'])
    if entry['author'] is None:
        print(entry['title'])

    subjects += entry['subject']

# print("The shortest title is: " + shortTitle + "\n")
# print("The longest title is: " + longTitle + "\n")

# count author
cnt_authors = collections.Counter(authors)
del cnt_authors[None]
print("The top 10 most common corresponding authors: " + str(cnt_authors.most_common(10)) + "\n")

# count subjects
cnt_subjects = collections.Counter(subjects)
del cnt_subjects[None]
print("The top 10 most common subjects: " + str(cnt_subjects.most_common(10)) + "\n")


