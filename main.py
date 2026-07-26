import sqlite3

DB_NAME = "students.db"

def get_db_connection():
    """Establishes and returns a secure database connection."""
    return sqlite3.connect(DB_NAME)

def init_db():
    """Initializes the database and creates the students table if it doesn't exist."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL
                )
            """)
            print("[INFO] Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"[ERROR] Database initialization failed: {e}")

def add_student():
    """Validates input and safely inserts a new student record into the database."""
    student_id = input("Enter unique Student ID: ").strip()
    if not student_id:
        print("[WARN] Student ID cannot be empty.")
        return

    name = input("Enter Student Name: ").strip()
    
    try:
        age = int(input("Enter Age: ").strip())
    except ValueError:
        print("[WARN] Age must be a valid integer number.")
        return

    grade = input("Enter Grade (e.g., A, B, C): ").strip()

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Check if Student ID already exists
            cursor.execute("SELECT id FROM students WHERE id = ?", (student_id,))
            if cursor.fetchone():
                print(f"[ERROR] Student ID '{student_id}' already exists!")
                return

            # Insert new student record
            cursor.execute(
                "INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)",
                (student_id, name, age, grade)
            )
            print(f"[SUCCESS] Student '{name}' added successfully!")
            
    except sqlite3.Error as e:
        print(f"[ERROR] Database operation failed: {e}")

if _name_ == "_main_":
    init_db()
    print("\n--- Student Registration System ---")
    add_student()
