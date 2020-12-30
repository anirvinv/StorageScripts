import sqlite3 as sql
import random

conn = sql.connect('files.db')

try:
    conn.execute("""CREATE TABLE files 
            (ID INT NOT NULL,
            VALUE BLOB NOT NULL,
            TYPE TEXT NOT NULL
            )
    """)
except:
    pass

cursor = conn.cursor()

def get_extension(path):
    ext = ""
    for i in range(len(path) -1 , -1, -1):
        if not path[i] == ".": 
            ext = path[i] + ext
        else:
            break
    return ext

def write_files(path):
    with open(path, 'rb') as file:
        binary_data = file.read()
        data_tuple = (random.randint(10000, 99999), binary_data.strip(), get_extension(path))

    blob_query = f"""INSERT INTO files (ID, VALUE, TYPE) VALUES (?, ?, ?)"""
    cursor.execute(blob_query, data_tuple)
    
def retrieve_files():
    m = cursor.execute("""SELECT * FROM files """)
    for x in m:
        data = x[1]
        with open('bruh.' + x[2], 'wb') as file:
            file.write(data)


while True:
    print("________________________________")
    store = input("Do you want to store files?(y/n)\n>")
    if store == "y":
        path = input("\nPaste the absolute path of the file you want to store:\n>")
        write_files(path)
        break
    elif store == "n":
        retrieve = input("Would you like to retrieve files?(y/n)\n>")
        if retrieve == "y":
            retrieve_files()
            break
        elif retrieve == "n":
            print("Well, that's all I can do for you.")
            break
    else:
        print("Please enter one of the listed options 'y' or 'n'")

conn.commit()

