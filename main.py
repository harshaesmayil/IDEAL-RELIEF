from tabulate import tabulate

def add_med():
    import mysql.connector as m
    mydb = m.connect(host="localhost", user="root", password="Mesqatar@1357", database="pharmacy")
    mycursor = mydb.cursor()
    print("\n" + "="*40)
    print("         ADD MEDICINE")
    print("="*40)
    no = int(input("Enter Medicine Number: "))
    name = input("Enter Medicine Name: ")
    purpose = input("Enter Purpose/Problem: ")
    stock = int(input("Enter Stock: "))
    exp_date = input("Enter Expiry Date (YYYY-MM-DD): ")
    price = input("Enter Price: ")
    q = "insert into ideal(sno, med_name, purpose,quantity, expiry_date, price) values ({},'{}','{}',{},'{}','{}')".format(no, name, purpose, stock, exp_date, price)
    mycursor.execute(q)
    mydb.commit()
    print("Medicine added successfully!\n")

def update_med():
    import mysql.connector as m
    mydb = m.connect(host="localhost", user="root", password="Mesqatar@1357", database="pharmacy")
    mycursor = mydb.cursor()
    print("\n" + "="*40)
    print("         UPDATE MEDICINE STOCK")
    print("="*40)
    sno = int(input("Enter Medicine Number (S.No): "))
    stock = int(input("Enter New Stock: "))
    z = (stock, sno)
    q = "update ideal set quantity=%s where sno=%s"
    mycursor.execute(q, z)
    mydb.commit()
    print("Stock updated successfully!\n")

def search_med():
    import mysql.connector as m
    from tabulate import tabulate
    mydb = m.connect(host="localhost", user="root", password="Mesqatar@1357", database="pharmacy")
    mycursor = mydb.cursor()
    print("\n" + "="*40)
    print("         SEARCH MEDICINE")
    print("="*40)
    x = input("Enter Purpose/Problem: ")
    q = "SELECT * FROM ideal WHERE purpose=%s"
    mycursor.execute(q, (x,))
    rs = mycursor.fetchall()
    headers = ["S.No", "Medicine Name", "Purpose", "Quantity", "Expiry Date", "Price"]
    if rs:
        print("\n--- Medicine Details ---")
        print(tabulate(rs, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No medicines found for this problem.\n")

def delete_med():
    import mysql.connector as m
    mydb = m.connect(host="localhost", user="root", password="Mesqatar@1357", database="pharmacy")
    mycursor = mydb.cursor()
    print("\n" + "="*40)
    print("         DELETE MEDICINE")
    print("="*40)
    sno = int(input("Enter Medicine Number (S.No) to delete: "))
    q = "delete from ideal where sno=%s"
    mycursor.execute(q, (sno,))
    mydb.commit()
    print("Medicine deleted successfully!\n")

def comi():
    print("\n" + "="*40)
    print("         ADMIN MENU")
    print("="*40)
    print("1. Add Medicine")
    print("2. Update Medicine Stock")
    print("3. Search Medicine")
    print("4. Delete Medicine")
    print("5. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        add_med()
        x = input("Do you want to run again (y/n)? ")
        if x.lower() == "y":
            comi()
        else:
            print("Thank you for visiting us!")
    elif ch == 2:
        update_med()
        x = input("Do you want to run again (y/n)? ")
        if x.lower() == "y":
            comi()
        else:
            print("Thank you for visiting us!")
    elif ch == 3:
        search_med()
        x = input("Do you want to run again (y/n)? ")
        if x.lower() == "y":
            comi()
        else:
            print("Thank you for visiting us!")
    elif ch == 4:
        delete_med()
        x = input("Do you want to run again (y/n)? ")
        if x.lower() == "y":
            comi()
        else:
            print("Thank you for visiting us!")
    elif ch == 5:
        print("Logging out of admin menu. Goodbye!")
    else:
        print("Invalid choice. Try again.")
        comi()

def login_admin():
    username = "iesadmin"
    password = "ies123"
    print("\n" + "="*40)
    print("         ADMIN LOGIN")
    print("="*40)
    user = input("Enter username: ")
    pas = input("Enter password: ")
    if user == username and pas == password:
        print("Login successful!\n")
        comi()
    else:
        print("Login failed.\n")

def view():
    print("\n" + "="*40)
    print("         STUDENT MENU")
    print("="*40)
    print("1. Search Medicine")
    print("2. Billing")
    print("3. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        search_med()
        x = input("Do you want to run again (y/n)? ")
        if x.lower() == "y":
            view()
        else:
            print("Thank you for visiting us!")
    elif ch == 2:
        name = input("Enter Name: ")
        clss = input("Enter Class: ")
        time = input("Enter Time: ")
        date = input("Enter Date: ")
        print("\n" + "="*20 + " BILL " + "="*20)
        print(f"NAME: {name}")
        print(f"CLASS: {clss}")
        print(f"TIME: {time}")
        print(f"DATE: {date}")
        print("="*47)
        search_med()
    elif ch == 3:
        print("Thank you for visiting us!")
    else:
        print("Invalid choice. Try again.")
        view()

print("="*47)
print("      PHARMACY MANAGEMENT SYSTEM")
print("="*47)
print("1. Admin Login")
print("2. Student Login")
print("3. Exit")
ch = int(input("Enter choice: "))
if ch == 1:
    login_admin()
elif ch == 2:
    view()
elif ch == 3:
    print("Thank you for using the Pharmacy Management System!")
else:
    print("Invalid choice. Exiting.")
