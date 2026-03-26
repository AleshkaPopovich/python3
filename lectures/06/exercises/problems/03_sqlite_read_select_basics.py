"""Problem 03: Read data from `students` (SELECT basics).

Task:
1. Select all columns from all rows
2. Select only `name` and `email`
3. Select one row by email (`ana@example.com`) using parameterized query
4. Print query results in readable form
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO SELECT * FROM students
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    print("All rows:")
    for row in rows:
        print(row)

    # TODO SELECT name, email FROM students
    cur.execute("SELECT name, email FROM students")
    name_email_rows = cur.fetchall()

    print("\nName and email only:")
    for row in name_email_rows:
        print(row)

    # TODO SELECT one row for ana@example.com
    cur.execute("SELECT * FROM students WHERE email = ?", ("ana@example.com",))
    one_row = cur.fetchone()

    print("\nOne row for ana@example.com:")
    print(one_row)

    conn.close()


if __name__ == "__main__":
    main()
