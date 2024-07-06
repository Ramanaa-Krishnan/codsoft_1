#TO-DO LIST TASK 1 - CODSOFT
#to do list create, update, and track their to-do lists

todo={} #dictionary initialization
tasknum=1
def addtask(todo,task):
    global tasknum     #make a change to a global variable inside a function     
    todo[tasknum]={}   #to avoid 'Task' KeyError because we need to initialze nested dicitonary as value
    
    todo[tasknum]["Task"]=task
    todo[tasknum]["Status"]="Pending"   #pending for new task
    tasknum+=1


def viewtask(todo):
    serial=1
    q=int(input("Enter 1 to view all tasks and 0 to view only pending tasks : "))
    if q==1:   #to view all tasks in todo
        for a in todo:
           print(serial,".Task is {} and Status at {} with position {}.".format(todo[a]["Task"],todo[a]["Status"],a))
           serial+=1
    elif q==0: #to view only pending tasks
        for a in todo:
            if todo[a]["Status"]=="Pending":
                print(serial,".Task is {} and Status at {}.".format(todo[a]["Task"],todo[a]["Status"]))
                serial+=1
            else:
                pass
    else:
        print("Enter appropriate option to proceed..!!")
           
        
def updatetask(todo,task,user_tasknum):
    if user_tasknum in todo:
        todo[user_tasknum]["Task"]=task   #updation
    else:
        print("Entered Task Number {} do not exist in your To-Do List..!!".format(user_tasknum))

def marktask(todo,user_tasknum):  

    if user_tasknum in todo:
        todo[user_tasknum]["Status"]="Completed"    #status as completed
    else:
        print("Entered Task Number {} do not exist in your To-Do List..!!".format(user_tasknum))

def deletetask(todo,user_tasknum):
    if user_tasknum in todo:   #to remove required task from todo
        del todo[user_tasknum]
    else:
        print("Entered Task Number {} do not exist in your To-Do List..!!".format(user_tasknum))


while True:
    print("""

1.ADD
2.VIEW TASKS
3.UPDATE
4.MARKING STATUS
5.DELETE
ANY - EXIT
""")
    ch=int(input("Enter your choice to perform task manipulation in To-Do List :"))
    if ch==1:
        task=input("Enter your New Task : ")
        addtask(todo,task)
        print("Task added to To-Do List..!!")
    elif ch==2:
        viewtask(todo)
    elif ch==3:
        viewtask(todo)   #viewtask() to know appropriate task number for hassle-free manipulation
        task=input("Enter Updated Task : ")
        user_tasknum=int(input("Enter Task number or serial Number based on above displayes tasks : "))
        updatetask(todo,task,user_tasknum)
    elif ch==4:
        viewtask(todo)   #viewtask() to know appropriate task number for hassle-free markings
        user_tasknum=int(input("Enter Task number or serial Number to change task status : "))
        marktask(todo,user_tasknum)
    elif ch==5:
        viewtask(todo)   #viewtask() to know appropriate task number for hassle-free deletion
        user_tasknum=int(input("Enter Task number or serial Number to delete required task : "))
        deletetask(todo,user_tasknum)
    else:
        break  #end


