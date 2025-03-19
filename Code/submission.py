import sqlite3

def submitOrder(date, time, main, side, drink, userID):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("INSERT INTO orders (date, time, main, side, drink, userid) VALUES (?, ?, ?, ?, ?, ?)", [date, time, main, side, drink, userID])
    con.commit()
    cur.close()
    return True

def submitSuggestion(content, userID):
    # Takes suggestion text and userID as parameters
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("INSERT INTO suggestions (suggestion, userid) VALUES (?, ?)", [content, userID])
    # Creates a new database entry
    con.commit()
    cur.close()
    return True

def getOrders():
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT date, time, main, side, drink, userid FROM ORDERS")
    data = cur.fetchall()
    return data

def getSuggestions():
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT suggestion FROM SUGGESTIONS")
    data = cur.fetchall()
    return data

def getYourOrders(userID):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT date, time, main, side, drink FROM ORDERS where userid = ?;", [userID])
    data = cur.fetchall()
    return data

def clearSuggestions():
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("DELETE FROM suggestions")
    con.commit()
    return True

def getMains():
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT name FROM mains")
    data = cur.fetchall()
    return data
    # Returns the names of all the mains available

def getSides():
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT name FROM sides")
    data = cur.fetchall()
    return data
    # Returns the names of all the sides available

def getDrinks():
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("SELECT name FROM drinks")
    data = cur.fetchall()
    return data
    # Returns the names of all the drinks available

def newMain(name):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("INSERT INTO mains (name) values (?)", [name])
    con.commit()
    cur.close()
    return True

def newSide(name):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("INSERT INTO sides (name) values (?)", [name])
    con.commit()
    cur.close()
    return True

def newDrink(name):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("INSERT INTO drinks (name) values (?)", [name])
    con.commit()
    cur.close()
    return True

def removeOldOrders(date):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("DELETE FROM orders WHERE date < ?", [date])
    con.commit()
    cur.close()
    return True

def deleteMain(name):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("DELETE FROM mains WHERE name = ?", [name])
    con.commit()
    cur.close()
    return True

def deleteSide(name):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("DELETE FROM sides WHERE name = ?", [name])
    con.commit()
    cur.close()
    return True

def deleteDrink(name):
    con = sqlite3.connect('SystemDatabase.db')
    cur = con.cursor()
    cur.execute("DELETE FROM drinks WHERE name = ?", [name])
    con.commit()
    cur.close()
    return True