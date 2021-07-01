import sqlite3

# Connect to SQLite3 module and use cursor to create a new table
conn = sqlite3.connect('files.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fileNames TEXT)")
    conn.commit()

conn = sqlite3.connect('files.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')

# Loop through objects in the tuple to find .txt files
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one file out of the tuple therefore (x,)
        # will denote a one element tuple for each .txt file
            cur.execute("INSERT INTO tbl_files (col_fileNames) VALUES (?)", (x, ))
            print(x)
conn.close()
