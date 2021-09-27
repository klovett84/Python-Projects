## Classes
Project demonstrating classes and class inheritance.

```python
#Create Pet class
class Pet:
    name = ""
    sex = ""
    age = 0

#Create new Dog class inherited from Pet class
class Dog(Pet):
    breed = ""
    size = ""
```

## File Transfer
A program that transfers any files modified within the last 24 hours from a selected source folder to a selected destination folder. Uses tkinter for UI.

![screenshotFileTransfer](https://user-images.githubusercontent.com/84836870/134845049-323c8e9d-485d-4b15-86a5-020971959079.png)

```python
# transfer files from source to destination if modified within last 24 hours
def transferFiles():
  # set current time and the time 24 hours ago
  now = datetime.datetime.now()
  last24hours = now - timedelta(hours = 24)

  sourceFolder = sourceBox.get() + "/"
  destinationFolder = destinationBox.get()
  # create a tuple of filepaths from source
  files = os.listdir(sourceFolder)

  for i in files:
    modificationTime = datetime.datetime.utcfromtimestamp(os.path.getmtime(sourceFolder+i))
    if modificationTime > last24hours:
      shutil.move(sourceFolder+i, destinationFolder)
```

## NiceMean
A simple text game demonstrating if statements and loops. Player chooses whether to be kind or rude to a stranger and is asked to play again after winning or losing.

```python
def nice_mean (nice,mean,name):
  stop = True
  while stop:
    show_score(nice,mean,name)
    pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
    if pick == "n":
        print("\nThe stranger walks away smiling...")
        nice = (nice + 1)
        stop = False
    if pick == "m":
        print ("\nThe stranger bursts into \ntears and flees...")
        mean = (mean + 1)
        stop = False
  score(nice, mean, name) # pass the 3 variables to the score()

def show_score(nice,mean,name):
  print("\nCurrent total: \n{} Nice | {} Mean".format(nice,mean))

def score(nice,mean,name):
  # score function is being passed the values stored within the 3 variables
  if nice > 2: #if condition is valid, call win function passing in the variables so it an use them
      win(nice,mean,name)
  if mean > 2: #if condition is valid, call lose function passing in the variables so it can use them
      lose(nice,mean,name)
  else: #else, call nice_mean function passing in the variables so it can use them
      nice_mean(nice,mean,name)
```

## Practice Projects
### Database
Create table and add items to it using SQLite3.

```python
with sqlite3.connect(':memory:') as connection:
  c = connection.cursor()
  c.execute("DROP TABLE IF EXISTS Roster")
  c.execute("CREATE TABLE Roster (Name TEXT, Species TEXT, IQ INT)")
  c.executemany("INSERT INTO Roster VALUES(?, ?, ?)",
                rosterValues)
  c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
            ('Human', 'Korben Dallas', 100))

  c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
```

### Date
Check current time across different timezones to determine if business is open.

```python
portlandTime =(datetime.datetime.now(pytz.timezone('US/Pacific')))
newYorkTime = (datetime.datetime.now(pytz.timezone('US/Eastern')))
```

```python
def openOrClosed():
  print("Portland: {}".format(portlandTime.strftime("{}:{}{}".format("%I", "%M", "%p"))))
  if portlandTime.hour > businessOpen and portlandTime.hour < businessClose:
    print("The Portland branch is open!\n")
  else:
    print("The Portland branch is closed.\n")

  print("New York: {}".format(newYorkTime.strftime("{}:{}{}".format("%I", "%M", "%p"))))
  if newYorkTime.hour > businessOpen and newYorkTime.hour < businessClose:
    print("The New York branch is open!\n")
  else:
    print("The New York branch is closed.\n")
```

### GUI
A basic GUI using tkinter.

![image](https://user-images.githubusercontent.com/84836870/134846123-3cd774ba-0f1f-4447-a247-a9b33ffdacd4.png)

## SQL
Create and add people to a database and make a selection.

``` python
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName Text, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)",
                  peopleValues)

# select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
```

## Student Tracking
A program for tracking information about students. Uses tkinter GUI and SQLite3.

![image](https://user-images.githubusercontent.com/84836870/134846449-7b9e141e-6bbc-46bc-a200-3c29bbf5ca50.png)

```python
def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() # This will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip() # This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) # combine our normailzed names into a fullname
    var_course = self.txt_course.get().strip()
    var_course = self.txt_course.get().title()
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email: # will use this soon
        print("Incorrect email format.")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_course) > 0) and (len(var_phone) > 0) and(len(var_email) > 0): # enforce the user to provide both names
        conn = sqlite3.connect('db_students.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))#,(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_course,col_phone,col_email) VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_course,var_phone,var_email))
                self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database. Please choose a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all five fields.")
```

## Web Page Generator
A simple program that takes text input and generates a webpage with that input as a header. Uses tkinter and webbrowser.

![screenshotWebPageGen](https://user-images.githubusercontent.com/84836870/134846690-5a39fc4a-d742-427c-a941-653418591d21.png)

```python
def createPage():
    bodyText = enterText.get()
    
    page = open("page.html", "w")
    page.write("""<html>
                    <head>
                        <title>Web Page Generator</title>
                    </head>
                    <body>
                        <h1>{}</h1>
                    </body>
                  </html>""".format(bodyText))
    page.close()
    webbrowser.open("page.html")
```

## abstraction.py
Project demonstrating abstract methods.

```python
from abc import ABC, abstractmethod
class recipe(ABC):
    def description(self, food):
        print("This recipe is for: ",food)
    @abstractmethod
    def prep(self, food):
        pass

class Rye(recipe):
    def prep(self, food):
        print("To make this {}, carry out the following steps...".format(food))

obj = Rye()
obj.description("rye bread")
obj.prep("rye bread")
```

## protectPrivate.py
Project demonstrating private and protected variables.

```python
class ProtectPrivate:
    def __init__(self):
        self._protectedVar = True #Protecte variable
        self.__privateVar = 0 #Private variable

    #Two functions to print and change the value of privateVar
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

#Instantiate ProtectPrivate object and print protectedVar
ProtectObj = ProtectPrivate()
print(ProtectObj._protectedVar)

#Print privateVar, change its value, and print it again
ProtectObj.getPrivate()
ProtectObj.setPrivate(42)
ProtectObj.getPrivate()
```
