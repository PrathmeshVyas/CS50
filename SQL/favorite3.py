# import csv

# open("shows.db", "w").close()
# db=SQL("sqlite:///shows.db")

# db.execute("CREATE TABLE shows(id INTEGER, title TEXT, PRIMARY KEY(id))")
# db.execute("CREATE TABLE genres(show_id INTEGER, genre TEXT, FOREIGN KEY(show_id) REFERENCES shows(id))")

# title = input("title: ").strip().upper()
 
# with open("FTVShows.csv", "r") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         title = row["title"].strip().upper()
        
#         id=db.execute("insert into shows (title) values(?)", title)
#         for genre in row["genres"].split(", "):
#             db.execute("insert into genres (show_id, genre) values(?, ?)", id, genre)
            



