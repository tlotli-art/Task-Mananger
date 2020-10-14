# import date
import datetime

# Task mananger application
# Login, Register, Add task, View all tasks, View assigned tasks and check stats

# Login
# Open user text, and make it that if user name and password are present in the text file, allow user to login  
user_file = open("user.txt","r+")

login = False

while login == False:
    username = input("Please enter your username: ").strip()
    password = input("Please enter your password: ").strip()

    for line in user_file:
        loginInfo = line.strip().split(", ")

        if loginInfo[0] == username and loginInfo[1] == password:
            login = True
        
    if login == False:
        print("Incorrect credentials! try again")
    user_file.seek(0)


# Admin menu
# If user loging in is the admin, show a menu thats unique to the administrator, else show a regular menu

back_to_menu = False
while not back_to_menu: 
    def main_menu():
        return(menu)
    if username == "admin":
        menu = input("""
Please select one of the following options:
r  - register user
a  - add task
va - view all tasks
vm - view my tasks
gr - generate reports
e  - exit
ds  - display statistics
""")
        back_to_menu = True

    else:
        menu = input("""
Please select one of the following options:
r  - register user
a  - add task
va - view all tasks
vm - view my tasks
e  - exit
""")
    options = main_menu()
    print(options)
    user_file.close()
    if menu != "vm":
        break



    # View my tasks
    # open task text file, if user selects 'vm' from the menu, read the lines only containing the username of the user and display them
    def view_mine():
        task_file = open("tasks.txt", "r+")
        if menu == "vm":
            count = 0
            for line in task_file:
                task_info = line.split(", ")
                if task_info[0] == username:
                    count += 1
                    print("Task " + str(count))
                    my_line = line
                    if my_line[0]:
                        print("User: " + task_info[0])
                    if my_line[1]:
                        print("Task: " + task_info[1])
                    if my_line[2]:
                        print("Task description: " + task_info[2])
                    if my_line[3]:
                        print("Date assigned: " + task_info[3])
                    if my_line[4]:
                        print("Due date: " + task_info[4])
                    if my_line[5]:
                        print("Task complete?: " + task_info[5])
                    
                    print("")
                        
            
                
                        
        task_file.close
    view_mine()

    
    vm_menu =  input('''Please enter the task number of the task you wish to enter or enter '-1' to go to the main menu: ''')
                
    if vm_menu == "-1":
        back_to_menu = False

    counting = 0
    task_file = open("tasks.txt", "r+")
    for line in task_file:
        tsk = line.split(", ")
        if tsk[0] == username:
            fsk = ", ".join(tsk)
            counting += 1
            all_ = fsk + ", " + str(counting)
            if vm_menu == str(counting):
                back_to_menu = True
                  


                task_select = input(""" Please select:
'm' to mark task as complete
or
'ed' to edit the task
""")
                if task_select == "m":
                    all_ = all_.split(", ")
                    a = all_[2]
                    b = all_[3]
                    replacements = {"no":"yes"}
                    with open("tasks.txt", "r+") as infile, open("tasks.txt", "r+") as outfile:

                        for line in infile:
                            for src, target in replacements.items():
                                if a in line and b in line:
                                    line = line.replace(src, target)
                            outfile.write(line)

                
                    

                elif task_select == "ed":
                    all_ = all_.split(", ")
                    a = all_[2]
                    b = all_[3]

                    c = line.split(", ")

                    if c[-1] in line:
                        print("Task alredy complete")
                        break

                    ud = input("enter 'username' or 'due date': ")

                    if ud == "username":
                        replacements = {username:input("Enter new username: ")}
                    if ud == "due date":
                        dat = line.split(", ")
                        date = dat[4]
                        replacements = {date:input("Enter new due date: ")}
                    with open("tasks.txt", "r+") as infile, open("tasks.txt", "r+") as outfile:

                        for line in infile:
                            for src, target in replacements.items():
                                if a in line and b in line:
                                    line = line.replace(src, target)
                                    
                                    
                
                    
                    
                            outfile.write(line)
        

    task_file.close()

                    
def final():         
    write_task = open("task_overview.txt",  "w+")
    write_user = open("user_overview.txt",  "w+")
    task_file = open("tasks.txt","r+")
    count = 0
    con = task_file.read()
    a = con.split("\n")
    for i in a:
        if i:
            count += 1
    total_tasks = count
    write_task.write("Total number of tasks is: " + str(total_tasks))

    task_file.close()



    task_file = open("tasks.txt","r+")
    count = 0
    for line in task_file:
        line = line.split(", ")
        if "yes" in line[5]:
            count += 1
    complete_tasks = count
    # total complete 

    write_task.write("\nTotal number of complete tasks is: " + str(complete_tasks)) 
    task_file.close()


    task_file = open("tasks.txt","r+")
    count = 0
    for line in task_file:
        line = line.split(", ")
        if "o" in line[5]:
            count += 1
    uncomplete_tasks = count
    write_task.write("\nTotal number of uncomplete tasks is: " + str(uncomplete_tasks))
    # total uncompleted       
    task_file.close()

    task_file = open("tasks.txt","r+")
    t1 = datetime.date.today()
    for uncomplete in task_file:
        uncomplete = uncomplete.split(", ")
        if "o" in line[5]:
            count_date = 0
            for line in task_file:
                line = line.split(", ")
                date_str = datetime.datetime.strptime(line[4], "%d-%m-%Y").date()

                if t1 > date_str:
                    count_date += 1

            over_due = count_date
    # total overdue
            write_task.write("\nTotal overdue tasks is: " + str(over_due))
    task_file.close()
    # Percentage of incomplete tasks
    percentage_incomplete = (uncomplete_tasks/total_tasks)*100
    write_task.write("\nPercentage of incomplete tasks is: " + str(percentage_incomplete)) 
    # Persentage of tasks overdue
    percentage_overdue = (over_due/total_tasks)*100
    write_task.write("\nPercentage of overdue tasks is: " + str(percentage_overdue))

    # Percentage of total tasks to user
    user_file = open("user.txt","r+")
    count = 0
    con = user_file.read()
    a = con.split("\n")
    for i in a:
        if i:
            count += 1
    total_users = count
    write_user.write("\nTotal number of users is: " + str(total_users))
    user_file.close()


    task_file = open("tasks.txt","r+")


    freq = []
    for line in task_file:
        line = line.split(", ")
        line = line[0]
        freq.append(line)
    task_file.close()

    so = ", ".join(freq)




    def word_count(so):
        counts = dict()
        words = so.split(", ")

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        return counts
    taskUser = (word_count(so))
    tog = []
    for key, value in taskUser.items():
        tog.append(value)
        write_user.write("\npercentage of the total number of tasks assigned to " + key + ": " + str(round((value/total_tasks)*100,2)))
        
        
    task_file = open("tasks.txt","r+")
    freq7 = []
    freq2 = []
    freq9 = []
    for line in task_file:
        line = line.strip("\n")
        line = line.split(", ")
        line2 = line[5]
        line = line[0]
        line3 = line[4]
        freq7.append(line)
        freq2.append(line2)
        freq9.append(line3)
    task_file.close()



    lala = []
    task_file = open("tasks.txt","r+")
    for line in task_file:
        line = line.split(", ")
        date_str = datetime.datetime.strptime(line[4], "%d-%m-%Y").date()


        hello = 0
        t1 = datetime.date.today()
        if t1 > date_str:
            hello += 1
        if t1 < date_str:
            hello -= 1

        lala.append(hello)
        
        boka3 = list(zip(freq7, lala))
        

    finalvalue = []   
    tota = {}
    for key, valuex in boka3:
        tota[key] = tota.get(key, 0) + valuex


    bokatog = []
    for key, valuex in tota.items():
        bokatog.append(valuex)

    boka4 = list(zip(tog, bokatog))
    final1 = []
    for key, value in tota.items():
        final1.append(key)
    final2 = []
    for line in boka4:
        final = (line[1]/line[0])*100
        final2.append(str(final))
    boka5 = list(zip(final1, final2))
    fly  = []
    fly2 = []
    for line in boka5:
        fly.append(line[0])
    for line2 in boka5:
        fly2.append(line[1])


    freq21 = []
    for a in freq2:
        freq31 = a.replace("no", "0")
        freq21.append(freq31)


    freq_ = []
    for b in freq21:
        freq41 = b.replace("yes", "1")
        freq_.append(freq41)

    for i in range(0, len(freq_)):
        freq_[i] = int(freq_[i])




    ba = list(zip(freq, freq_))

    total = {}
    for key, value1 in ba:
        total[key] = total.get(key, 0) + value1

        

    # Percentage of tasks that must be completed by user            
    yog = []    
    for key, value1 in total.items():
        yog.append(value1)

    boka = list(zip(tog, yog))

    vava = []
    for line in boka:
        boka2 = (line[1]/ line[0])* 100
        vava.append(str(boka2))
    boka6 = list(zip(final1,vava))
    car  = []
    car2 = []
    for line in boka6:
        car.append(line[0])
    for line2 in boka6:
        car2.append(line[1])

    write_user.write("\npercentage of the total number of tasks for " + str(car) + " completed is " + str(car2) + " respectively")





    freq21 = []
    for a in freq2:
        freq31 = a.replace("yes", "0")
        freq21.append(freq31)


    freq_ = []
    for b in freq21:
        freq41 = b.replace("no", "1")
        freq_.append(freq41)

    for i in range(0, len(freq_)):
        freq_[i] = int(freq_[i])




    ba = list(zip(freq, freq_))

    total = {}
    for key, value1 in ba:
        total[key] = total.get(key, 0) + value1

    # Percentage of completed by user            
    yog = []    
    for key, value1 in total.items():
        yog.append(value1)

    boka = list(zip(tog, yog))
    dee = []
    for line in boka:
        boka2 = (line[1]/ line[0])* 100
        dee.append(str(boka2))
    boka7 = list(zip(final1, dee))
    bus  = []
    bus2 = []
    for line in boka7:
        bus.append(line[0])
    for line2 in boka7:
        bus2.append(line[1])
    write_user.write("\npercentage of the total number of tasks for " + str(bus) + "has not completed is " + str(bus2) + " respectively")      

    write_user.write("\npercentage of the total number of tasks for " + str(fly) + "has not completed and are overdue is " + str(fly2) + " respectively")


    write_task.close()
    write_user.close()
    print("Report Generated")
final()


# Admin statistics
# If administrator selects 's' in the menu, print total number of users and tasks within the files





if username == "admin":
    if menu == "gr":
        final()
            
      

if username == "admin":
    if menu == "ds":
        write_task = open("task_overview.txt",  "r")
        write_user = open("user_overview.txt",  "r")
        y = write_task.read()
        z = write_user.read()
        print(y)
        print(z)

                 
# Register user
# Open user text file and if user is the administrator, and selects 'r', they will add a new user and password. If regular user selects 'r', access wi be denied

def reg_user():
    user_file = open("user.txt","r+")
    if menu == "r":

        while username == "admin":
            new_user = input("Please enter new username: ")
            for line in user_file:
                check = line.strip().split(", ")
                not_same = False
                while not_same == False:
                    if new_user == check[0]:
                        not_same = False
                        new_user = input('''Error! Username alredy exists
Please enter new username: ''')

                    
                    if new_user != check[0]:
                        not_same = True
                    if not_same == True:
                        break
            new_password = input("Please enter your new password: ")
            user_file = open("user.txt","r+")
            for line in user_file:
                user_file.write("\n" + new_user + ", " + new_password)
            break
        
    return(statement)
            
if menu == "r":
    if username == "admin":
        statement = "Succesfully added user!"
    if username != "admin":
        statement ="access denied!"
    register = reg_user()
    print(register)


user_file.close()


# add task
# Open tasks text file, if user selects 'a' from menu, write the new task within the tasks text file
def add_task():
    task_file = open("tasks.txt", "r+")
    if menu == "a":
        if username == "admin" or username != "admin":
            user_task = input("Please enter username of the person the task is assigned to: ")
            task = input("Please enter the title of the task: ")
            task_discription = input("Please enter discription of the task: ")
            date = date.today()
            due_date = input("Please enter the due date (dd-mm-yyyy): ")
            completion = input("Is the task complete?(yes/no): ")

        for line in task_file:
            task_file.write("\n" + user_task + ", " + task + ", " + task_discription + ", " + str(date) + ", " + due_date + ", " + completion )
        return("succesfully added a new task")

    task_file.close()
add_task()



# View all tasks
# open task text file, if user selects 'va' from the menu, read the total tasks available within the file
def view_all():
    task_file = open("tasks.txt", "r+")
    if menu == "va":
        for line in task_file:
            display = line.split(", ")
            if display[0]:
                print("User: " + display[0])
            if display[1]:
                print("Task: " + display[1])
            if display[2]:
                print("Task description: " + display[2])
            if display[3]:
                print("Date assigned: " + display[3])
            if display[4]:
                print("Due date: " + display[4])
            if display[5]:
                print("Task complete?: " + display[5])
    task_file.close()    

view_all()

    



# Exit
# If user selects 'e', exit the program
if menu == "e":
    print("Goodbye!")
    exit(0)

    
        
        
