import psycopg2

connection = psycopg2.connect(
    database="labs"
)

def show_menu():
    print("\n--- CRM Menu ---")
    print("1. Add Company")
    print("2. View Companies")
    print("3. Update Company")
    print("4. Delete Company")
    print("5. Add Employee")
    print("6. View Employees")
    print("7. Update Employee")
    print("8. Delete Employee")
    print("9. Exit")

def add_company():
    name = input("Enter company name: ")
    industry = input("Enter company industry: ")
    phone = input("Enter company phone number: ")

    cursor = connection.cursor()
    cursor.execute("INSERT INTO companies (name, industry, phone) VALUES (%s, %s, %s)", (name, industry, phone))

    connection.commit()
    cursor.close()
    print("Company added successfully.")

def view_companies():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM companies")
    companies = cursor.fetchall()

    print("\n--- Companies ---")
    for company in companies:
        print(f"ID: {company[0]}, Name: {company[1]}, Industry: {company[2]}, Phone: {company[3]}")

def update_company():
    company_id = input("Enter company ID to update: ")
    name = input("Enter new company name: ")
    industry = input("Enter new company industry: ")
    phone = input("Enter new company phone number: ")

    cursor = connection.cursor()
    cursor.execute("UPDATE companies SET name=%s, industry=%s, phone=%s WHERE id=%s", (name, industry, phone, company_id))

    connection.commit()
    cursor.close()
    print("Company updated successfully.")

def delete_company():
    company_id = input("Enter company ID to delete: ")

    cursor = connection.cursor()
    cursor.execute("DELETE FROM companies WHERE id=%s", (company_id,))

    connection.commit()
    cursor.close()
    print("Company deleted successfully.")

def add_employee():
    first_name = input("Enter employee first name: ")
    last_name = input("Enter employee last name: ")
    email = input("Enter employee email: ")
    company_id = input("Enter company ID for the employee: ")

    cursor = connection.cursor()
    cursor.execute("INSERT INTO employees (first_name, last_name, email, company_id) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, company_id))

    connection.commit()
    cursor.close()
    print("Employee added successfully.")

def view_employees():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    print("\n--- Employees ---")
    for employee in employees:
        print(f"ID: {employee[0]}, Name: {employee[1]} {employee[2]}, Email: {employee[3]}, Company ID: {employee[4]}")

def update_employee():
    employee_id = input("Enter employee ID to update: ")
    first_name = input("Enter new employee first name: ")
    last_name = input("Enter new employee last name: ")
    email = input("Enter new employee email: ")
    company_id = input("Enter new company ID for the employee: ")

    cursor = connection.cursor()
    cursor.execute("UPDATE employees SET first_name=%s, last_name=%s, email=%s, company_id=%s WHERE id=%s", (first_name, last_name, email, company_id, employee_id))

    connection.commit()
    cursor.close()
    print("Employee updated successfully.")

def delete_employee():
    employee_id = input("Enter employee ID to delete: ")

    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (employee_id,))

    connection.commit()
    cursor.close()
    print("Employee deleted successfully.")

while True:
    show_menu()
    choice = input("Select an option: ")

    if choice == '1':
        add_company()
    elif choice == '2':
        view_companies()
    elif choice == '3':
        update_company()
    elif choice == '4':
        delete_company()
    elif choice == '5':
        add_employee()
    elif choice == '6':
        view_employees()
    elif choice == '7':
        update_employee()
    elif choice == '8':
        delete_employee()
    elif choice == '9':
        print("Exiting CRM. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
