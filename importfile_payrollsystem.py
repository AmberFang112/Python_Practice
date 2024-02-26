def display_menu():
    print("COMMAND MENU")
    print("List - list all employees")
    print("Add - Add an employee")
    print("Del - Delete an employee")
    print("exit - Exit program")
    print()

def read_employee_data(filename):
    employee_list = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            employee_list.append([data[0], data[1], int(data[2]), float(data[3])])
    return employee_list

def list_employees(employee_list):
    if len(employee_list) == 0:
        print("There are no employee in the list. \n")
    else:
        for i in enumerate(employee_list, start=1):
            print(f"{i}")
        print()

def add_employees(employee_list):
    print('add an employee')
    firstname = input("Please enter the first name:")
    lastname = input("Please enter the last name:")
    employee_id = input("Please enter the employee ID:")
    salary = input("Please enter the salary:")
    employee_list.append([firstname,lastname,employee_id,salary])
    print(f"{firstname} {lastname} was added.\n")

def delete_employee(employee_list):
    print('delete an employee')
    employee_id = int(input("Enter employee ID:"))
    found = False
    for i, employee in enumerate(employee_list):
        if employee[2]  == employee_id:
            deleted_employee = employee_list.pop(i)
            print(f"{deleted_employee[0]} {deleted_employee[1]} with ID {employee_id} was deleted.\n")
            found = True
            break
    if not found:
            print("Employee does not exist.\n")




def main():
    print("Welcome our payroll system")
    display_menu()

    filename = "payroll.txt"
    employee_list = read_employee_data(filename)

    while True:
        command = input("Command:")
        if command.lower() == 'list':
            list_employees(employee_list)
        elif command.lower() == 'add':
            add_employees(employee_list)
        elif command.lower() == 'del':
            delete_employee(employee_list)
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()