import sqlite3

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age TEXT NOT NULL,
            grade TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_student():
    student_id = input("Enter unique Student ID: ").strip()
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if cursor.fetchone():
        print("Error: Student ID already exists!")
        conn.close()
        return
    
    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    grade = input("Enter Student Grade/Class: ").strip()
    
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (student_id, name, age, grade))
    conn.commit()
    conn.close()
    print(f"Success: {name} added successfully!")

def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("No student records found.")
        return
    
    print("\n--- Student List ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Grade: {row[3]}")
    print("--------------------")

def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    
    if row:
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        print(f"Success: Removed {row[0]} from database.")
    else:
        print("Error: Student ID not found.")
    conn.close()

def main():
    init_db()
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
            print("Invalid choice!")

if __name__ == "__main__":
    main()
    
