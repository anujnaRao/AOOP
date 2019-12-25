import MySQLdb as my


class EmployeeDB:
    db = my.connect('localhost', 'root', 'root@123', 'empdb')
    cur = db.cursor()

    def insert(self, slno, name, age):
        self.cur.execute('''insert into Employee(%d,"%s",%d)''' % (int(slno), name, int(age)))
        print("Record inserted!")

    def update(self, slno, age):
        self.cur.execute('''update Employee set age=%d where slno=%d''' % (int(age), int(slno)))
        print("Records updated!")

    def display(self):
        self.cur.execute('''select * from Employee''')
        print(self.cur.fetchall())
        print("Records displayed!")

    def delete(self, slno):
        self.cur.execute('''delete fromEmployee where slno=%d''' % (int(slno)))
        print("Record deleted!")


emp = EmployeeDB
while True:
    print("1. Insert\n2. Update\n3. Display\n4. Delete\n5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        slno = int(input("SLno "))
        name = input("Name ")
        age = int(input("Age "))
        emp.insert(slno, name, age)
    elif ch == 2:
        slno = int(input("SLno"))
        age = int(input("Age"))
        emp.update(slno, age)
    elif ch == 3:
        emp.display()
    elif ch == 4:
        slno = int(input("SLno"))
        emp.delete(slno)
    elif ch == 5:
        emp.cur.close()
        emp.db.close()
        break
    else:
        print("Invalid")
