# d = {
    
#     'prathmesh':"1452145200", 
#     'rushi':"1457145700"
    
#      }


# print(f"number {d['rushi']}")

import csv

with open("phonebook.csv", "a") as file:

    name=input()
    number=input()

    writer = csv.writer(file)

    writer.writerow([name, number])

file.close()