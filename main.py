# Student Management System

# Dictionary to store student records (Key: Student ID, Value: Details)
students = {}

def add_student():
    student_id = input("Enter unique Student ID: ").strip()
    if student_id in students:
        print("Error: Student ID already exists!")
        return
    
    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    grade = input("Enter Student Grade/Class: ").strip()
    
    students[student_id] = {
        "name": name,
        "age": age,
        "grade": grade
    }
    print(f"Success: {name} added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return
    
    print("\n--- Student List ---")
    for s_id, info in students.items():
        print(f"ID: {s_id} | Name: {info['name']} | Age: {info['age']} | Grade: {info['grade']}")
    print("--------------------")

def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    if student_id in students:
        removed = students.pop(student_id)
        print(f"Success: Removed {removed['name']} from records.")
    else:
        print("Error: Student ID not found.")

def main():
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
      
