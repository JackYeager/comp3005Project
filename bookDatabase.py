import psycopg2

def addNewBook():
    print("\n\nEnter ISBN, Title, Price, Stock")
    isbn = input()
    title = input()
    price = input()
    stock = input()

    insertScript = 'INSERT INTO "Book" ("ISBN", "Title", "Price", "Stock", "Total Sales") VALUES (%s, %s, %s, %s, %s)'
    insertValues = (int(isbn), title, int(price), int(stock), 0)

    cur.execute(insertScript, insertValues)

    print("Enter number of Authors and then the names of the Authors")
    num = input()

    for i in range(int(num)):
        name = input()
        insertScript = 'INSERT INTO "Authors" ("ISBN", "Author Name") VALUES (%s, %s)'
        insertValues = (int(isbn), name)   
        cur.execute(insertScript, insertValues) 

    print("Enter number of genres and then the genres")
    num = input()

    for i in range(int(num)):
        name = input()
        insertScript = 'INSERT INTO "Genre" ("ISBN", "Genre") VALUES (%s, %s)'
        insertValues = (int(isbn), name)  
        cur.execute(insertScript, insertValues)

    while True:
        print("Is this a new publisher?")
        print("1. Yes")
        print("2. No")

        choice = input()

        if int(choice) == 1:
            print("Enter Publisher email, name, address, phone number and banking")
            email = input()
            pname = input()
            addr = input()
            pnum = input()
            banking = input()

            insertScript = 'INSERT INTO "Publisher" ("Publisher Email", "Name", "Address", "Phone Number", "Banking") VALUES (%s, %s, %s, %s, %s)'
            insertValues = (email, pname, addr, int(pnum), banking)
            cur.execute(insertScript, insertValues)

            print("Enter Sales Percentage")
            salesPercent = input()

            insertScript = 'INSERT INTO "Publishes" ("ISBN", "Sales Percentage", "Publisher Email") VALUES (%s, %s, %s)'
            insertValues = (isbn, salesPercent, email)
            cur.execute(insertScript, insertValues)
            break

        elif int(choice) == 2:
            print("Enter Publisher email and Sales Percentage")

            email = input()
            salesPercent = input()

            insertScript = 'INSERT INTO "Publishes" ("ISBN", "Sales Percentage", "Publisher Email") VALUES (%s, %s, %s)'
            insertValues = (isbn, salesPercent, email)
            cur.execute(insertScript, insertValues)
            break
        else:
            print("invalid selection")

def registerNewUser():
    print("Enter email, name, phone number, shipping info and then billing info")

    email = input()
    name = input()
    phoneNum = input()
    sInfo = input()
    bInfo = input()

    insertScript = 'INSERT INTO "User" ("Email", "Name", "Phone Number", "Shipping Info", "Billing Info") VALUES (%s, %s, %s, %s, %s)'
    insertValues = (email, name, int(phoneNum), sInfo, bInfo)

    cur.execute(insertScript, insertValues)

    return email

def printTables():
    print("    Enter which table you would like to view")
    print("    1. Book")
    print("    2. Authors")
    print("    3. Publisher")
    print("    4. User")
    print("    5. Orders")
    print("    6. Publishes")
    print("    7. Items")
    print("    8. Genre")
    print("    9. Quit")

def displayTable():
    while True:
        printTables()
        choice = input()

        if int(choice) < 1 or int(choice) > 9:
            print("    Invalid selection")

        elif int(choice) == 1:
            cur.execute('SELECT * FROM "Book" ORDER BY "ISBN"')
            records = cur.fetchall()

            print("    Printing \"Book\"...\n\n")
            for row in records:
                print("    ISBN:", row[0], "Title:", row[1], "Price:", row[2], "Stock:", row[3], "Total Sales:", row[4], "\n")
        
        elif int(choice) == 2:
            cur.execute('SELECT * FROM "Authors"')
            records = cur.fetchall()

            print("    Printing \"Authors\"...\n\n")
            for row in records:
                print("    ISBN:", row[0], "Author Name:", row[1], "\n")
        
        elif int(choice) == 3:
            cur.execute('SELECT * FROM "Publisher"')
            records = cur.fetchall()

            print("    Printing \"Publisher\"...\n\n")
            for row in records:
                print("    P. Email:", row[0], "Name:", row[1], "Addr:", row[2], "Phone Num.:", row[3], "Banking:", row[4], "\n")

        elif int(choice) == 4:
            cur.execute('SELECT * FROM "User"')
            records = cur.fetchall()

            print("    Printing \"User\"...\n\n")
            for row in records:
                print("    Email:", row[0], "Name:", row[1], "Phone Num.:", row[2], "Ship Info:", row[3], "Bill Info:", row[4], "\n")

        elif int(choice) == 5:
            cur.execute('SELECT * FROM "Orders"')
            records = cur.fetchall()

            print("    Printing \"Orders\"...\n\n")
            for row in records:
                print("    Order Num.:", row[0], "Contact Email:", row[1], "Shipping:", row[2], "Progress:", row[3], "\n")

        elif int(choice) == 6:
            cur.execute('SELECT * FROM "Publishes"')
            records = cur.fetchall()

            print("    Printing \"Publishes\"...\n\n")
            for row in records:
                print("    ISBN:", row[0], "Sales Percentage:", row[1], "P. Email:", row[2], "\n")

        elif int(choice) == 7:
            cur.execute('SELECT * FROM "Items"')
            records = cur.fetchall()

            print("    Printing \"Items\"...\n\n")
            for row in records:
                print("    Order Num.:", row[0], "ISBN:", row[1], "\n")

        elif int(choice) == 8:
            cur.execute('SELECT * FROM "Genre"')
            records = cur.fetchall()

            print("    Printing \"Genre\"...\n\n")
            for row in records:
                print("    ISBN:", row[0], "Genre:", row[1], "\n")
        else:
            break 

def printMenu():
    print("1. Manager/Admin")
    print("2. User Login")
    print("3. Quit")

def printManagerMenu():
    print("Manager Menu")
    print()
    print("1. Display Sales")
    print("2. Sales by Author")
    print("3. Sales by Genre")
    print("4. Add Stock")
    print("5. Remove Stock")
    print("6. Display Table")
    print("7. Quit")

def printUserMenu():
    print("User Menu")
    print("1. Place Order")
    print("2. View available books")
    print("3. Search for book by Title")
    print("4. Track Order")
    print("5. Sign Out (Quit)")

def managerMode():
    while True:
        printManagerMenu()
        choice = input()

        if int(choice) < 1 or int(choice) > 7:
            print("Invalid selection")
            

        elif int(choice) == 1: # Display Sales
            print("Displaying Sales \n\n")
            cur.execute('SELECT "ISBN", "Title", "Total Sales", "Stock" FROM "Book" ORDER BY "ISBN"')
            records = cur.fetchall()

            for row in records:
                print("ISBN:", row[0], "Title:", row[1], " Sales:", row[2], " Stock:", row[3], "\n")
              
        elif int(choice) == 2: # Display Sales by Author
            print("Displaying Sales by Author \n\n")
            cur.execute('SELECT "Author Name", SUM("Total Sales") AS sales FROM "Authors" INNER JOIN "Book" ON "Book"."ISBN"="Authors"."ISBN" GROUP BY "Author Name"')
            records = cur.fetchall()

            for row in records:
                print("Author Name:", row[0], " Sales:", row[1], "\n") 

        elif int(choice) == 3: # Display Sales by Genre
            print("Displaying Sales by Genre \n\n")
            cur.execute('SELECT "Genre", SUM("Total Sales") AS sales FROM "Genre" INNER JOIN "Book" ON "Book"."ISBN"="Genre"."ISBN" GROUP BY "Genre"')
            records = cur.fetchall()

            for row in records:
                print("Genre:", row[0], " Sales:", row[1], "\n") 

        elif int(choice) == 4: # Add Stock
            print("    1. Add stock to existing book")
            print("    2. Add new book")
            
            choice = input()

            if int(choice) == 1: # Adds to existing book
                print("Enter ISBN and then amount of books to add")
                isbn = input()
                numBooks = input()

                updateScript = 'UPDATE "Book" SET "Stock" = "Stock" + %s WHERE "ISBN" = %s'
                updateValues = (int(numBooks), int(isbn))

                cur.execute(updateScript, updateValues)

            elif int(choice) == 2: #Adds new book
                addNewBook()
            else:
                print("invald selection, returning to Manager Menu")    

        elif int(choice) == 5: # Remove Stock
            print("Enter ISBN to take away from and amount of stock to take out")
            isbn = input()
            numBooks = input()

            updateScript = 'UPDATE "Book" SET "Stock" = "Stock" - %s WHERE "ISBN" = %s'
            updateValues = (int(numBooks), int(isbn))

            cur.execute(updateScript, updateValues)
            
        elif int(choice) == 6: # display table
            displayTable()

        else:
            # Quit
            break
    
def userMode(email):
    acc = email

    while True:
        printUserMenu()
        choice = input()

        if int(choice) < 1 or int(choice) > 5:
            print("Invalid selection")
        elif int(choice) == 1: # Place Order
            #Adding new Order
            string = 'SELECT * FROM "Orders"' 
            cur.execute(string)
            orderNum = len(cur.fetchall()) + 1

            print("Enter shipping address used for the order")
            addr = input()
            insertScript = 'INSERT INTO "Orders" ("Contact Email", "Order Number", "Shipping", "Progress") VALUES (%s, %s, %s, %s)'
            insertValues = (acc, orderNum, addr, 'Being Processed...')
            cur.execute(insertScript, insertValues)

            print("Enter how many books you would like to order and then the ISBN of books you would like to order")
            num = input()
            
            #Modifying "Book" table while inserting values into "Items"
            for i in range(int(num)):
                isbn = input()

                updateScript = 'UPDATE "Book" SET "Stock" = "Stock" - 1, "Total Sales" = "Total Sales" + 1 WHERE "ISBN" = %s'
                updateValues = (int(isbn),)
                cur.execute(updateScript, updateValues)

                insertScript = 'INSERT INTO "Items" ("Order Number", "ISBN") VALUES (%s, %s)'
                insertValues = (orderNum, isbn)
                cur.execute(insertScript, insertValues)
                
        elif int(choice) == 2: # View available books
            cur.execute('SELECT "Book"."ISBN", "Title", "Authors"."Author Name", "Stock" FROM "Authors" INNER JOIN "Book" ON "Authors"."ISBN" = "Book"."ISBN"')
            records = cur.fetchall()

            for row in records:
                if row[3] > 0:
                    print("ISBN:", row[0], " ", row[1], "By", row[2], " ", row[3], "remaining", "\n") 

        elif int(choice) == 3: # Search for book by Title
            print("Enter book title to search")
            title = input()

            searchScript = 'SELECT "Book"."ISBN", "Title", "Authors"."Author Name", "Stock" FROM "Authors" INNER JOIN "Book" ON "Authors"."ISBN" = "Book"."ISBN" WHERE "Book"."Title"  = %s'
            searchValues = (title,)
            try:
                cur.execute(searchScript, searchValues)
                records = cur.fetchall()

                for row in records:
                     print("ISBN:", row[0], " ", row[1], "By", row[2], " ", row[3], "remaining", "\n") 
            except:
                print("Title not found...")

        elif int(choice) == 4: # Track Order
            print("Enter the order number")
            orderNum = input()

            searchScript = 'SELECT "Progress" FROM "Orders" WHERE "Order Number" = %s'
            searchValues = (orderNum,)
            cur.execute(searchScript, searchValues)

            records = cur.fetchall()
            if len(records) == 0:
                print("Order number not found")
            else:
                for row in records:
                    print("Progress:", row[0], "\n") 

        else: # Quit
            break

if __name__ == "__main__":
    db = 'Bookstore'
    port_id = 5432
    hostname = 'localhost'
    username = 'postgres'
    pwd = 'password'

    conn = psycopg2.connect(host = hostname, dbname = db, user = username, password = pwd, port = port_id)
    cur = conn.cursor()

    userLogged = False

    while True:
        print("Welcome to Book Ordering System. Please make a selection")
        printMenu()
        choice = input()
        
        if int(choice) < 1 or int(choice) > 3:
            print("print 1, 2 or 3")
        else:
            if int(choice) == 1:
                # Manager/Admin
                managerMode()
            elif int(choice) == 2:
                # User
                while True:
                    print("    1. Log in")
                    print("    2. Sign up")
                    print("    3. Quit")
                    choice = input()

                    if int(choice) < 1 or int(choice) > 3:
                        print("Invalid selection")

                    elif int(choice) == 1:
                        print("Enter login email")
                        email = input()
                        string = 'SELECT "Email" FROM "User" WHERE "User"."Email" = \'' + email + '\'' 
                        cur.execute(string)
                        records = cur.fetchall()

                        if len(records) > 0:
                            userMode(email)
                        else:
                            print("Email not found. Returning to menu")
                            break

                    elif int(choice) == 2:
                        email = registerNewUser()
                        userMode(email)

                    else:
                        break
                
            else:
                # Quit
                break
        
    conn.commit()

    cur.close()
    conn.close()