import sqlite3
import requests
import json

id = "9e3f7ce4-b9a7-4244-b709-dae5c1f1d4a8"  #ჰარი პოტერის პერსონაჟების unique id (ამ შემთხვევაში ეს არის მთავარი გმირის ჰარი პოტერის id)
resp = requests.get(f'https://hp-api.onrender.com/api/character/{id}')
print(resp.status_code)
print(resp.headers)
print(resp)
result = resp.json()
characters = result[0]
with open('chatacters.json','w') as file:
    json.dump(result, file, indent=4)

print("Name:", characters["name"])
print("House:", characters["house"])
print("Species:", characters["species"])


conn = sqlite3.connect("characters.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE character_table
(name VARCHAR(50),
gender VARCHAR(50),
house VARCHAR(100)
)
''')

cursor.execute("INSERT INTO character_table VALUES (?,?,?)", (characters["name"], characters["house"], characters["species"]))
conn.commit()
conn.close()       #ეს ცხრილი დაამატებს მონაცემებს ჰარი პოტერის პერსონაჟებზე, მე ამ შემთხვევაში მხოლოდ ჰარი პოტერი დავამატე