def display_menu():
    print("COMMAND MENU")
    print("List - list all employees")
    print("Add - Add an employee")
    print("Del - Delete an employee")
    print("exit - Exit program")
    print()

employee_list = [["James","Green",90001,3000],
                 ["Racheal","Lee",90002,3500],
                 ["Micheal","Chopinn",90002,3500]]
def list(x):
    if len(employee_list) == 0:
        print("There are no movies in the list. \n")
    else:
        for i in enumerate(employee_list, start=1):
            print(f"{i}")
        print()

def add(y):
    print('add an employee')
    firstname = input("Please enter the first name:")
    lastname = input("Please enter the last name:")
    employee_id = input("Please enter the employee ID:")
    salary = input("Please enter the salary:")
    employee_list.append([firstname,lastname,employee_id,salary])
    print(f"{firstname}f{lastname} was added.\n")
def dele(z):
    print('delete an employee')
    employee_id = int(input("Enter employee ID:"))
    found = False #不明白，回去看
    for i, employee in enumerate(employee_list):
        if employee[2]  == employee_id:
            del employee_list[i]
            print(f"{employee_id} was deleted.\n")
            found = True #不明白，回去看
            break #不明白，回去看
    if not found:
            print("Employee does not exist.\n")




def main():
    print("Welcome our payroll system")
    display_menu()

    while True:
        command = input("Command:")
        if command.lower() == 'list':
            list(employee_list)
        elif command.lower() == 'add':
            add(employee_list)
        elif command.lower() == 'del':
            dele(employee_list)
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()