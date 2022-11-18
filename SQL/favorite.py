import csv

titles = {}

with open("FTVShows.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        title = row[1].strip().upper()
        if title not in titles:
            titles[title]=0
        titles[title]+=1
            
def f(title):
    return titles[title]

for title in sorted(titles, key=lambda title: titles[title], reverse=True): 
    print(title, titles[title])


