#Project two TODO-APP 
tasks = []

def add_task(task):
     tasks.append(task)
     
def edit_task(index, new_task):
     if 0 <= index < len(tasks):
          tasks[index] = new_task
     else:
          print("invalid task index")

def delet_task(index):
     if 0 <= index < len(tasks):
          tasks.pop(index)
     else:
          print("invalid task index")
          
def show_task():
     if not tasks:
          print("No tasks yet")
     else:
          for i, task in enumerate(tasks):
               print(f"{i}, {task}")
add_task("study Python")  
add_task("complete DBMS assignment")
show_task()

edit_task(0, "Study python oop")
delet_task(1)
show_task()