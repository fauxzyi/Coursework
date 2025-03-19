import sqlite3

def authenticateLogin(username, password):
    # Takes paramaters of username and password given by the user
    username = str(username)
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT password FROM users WHERE username = ?;", [username])
    # Gets the password of the given username from the database
    userPass = cur.fetchall()
    con.close()
    if len(userPass) == 0:
        return False
    # If there is no password for that username, return False
    else:
        userPass = userPass[0][0]
    if userPass == password:
        return True
    else:
        return False
    # If there is a password, check if it matches, if it does, return True

def checkPerms(username):
    # Takes username as a parameter, checks value of permissions
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT permissions FROM users WHERE username = ?;", [username])
    perms = cur.fetchall()
    return perms[0][0]

def accountExists(username):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT password FROM users WHERE username = ?;", [username])
    # Gets the password for the user from the database
    exist = cur.fetchall()
    if len(exist) > 0:
        return True
    else:
        return False
    # If there is a password, the account exists so return True, else return False

def createAccount(username, password, permissions):
    # Takes parameters of username, password and permissions for the new account
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("INSERT INTO users (username, password, permissions) VALUES (?, ?, ?)", [username, password, permissions])
    # Creates a new database entry for the new account
    con.commit()
    cur.close()
    return True

def getPassword(username):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT password FROM users WHERE username = ?;", [username])
    password = cur.fetchall()
    return password[0][0]

def getID(username):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT id FROM users WHERE username = ?;", [username])
    userID = cur.fetchall()
    return userID[0][0]

def getName(userID):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT username FROM users WHERE id = ?;", [userID])
    names = cur.fetchall()
    return names

def getUsers():
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT username, permissions FROM users")
    users = cur.fetchall()
    return users

def deleteAccount(username):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    userid = getID(username)
    cur.execute("DELETE FROM users WHERE username = ?;", [username])
    cur.execute("DELETE FROM orders WHERE userID = ?;", [userid])
    con.commit()
    cur.close()
    return True