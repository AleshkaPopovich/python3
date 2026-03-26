"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    rows1 = cur.fetchall()
    print("The total number of students: ")
    for row in rows1:
        print(row)

    cur.execute("SELECT AVG(age) FROM students")
    rows2 = cur.fetchall()
    print("\nThe average number of students: ")
    for row in rows2:
        print(row)
    

    cur.execute("SELECT MIN(age), MAX(age) FROM students")
    rows3 = cur.fetchall()
    print("\nMIN and MAX age of students: ")
    for row in rows3:
        print(row)
    

    cur.execute("SELECT track, COUNT(*) FROM students GROUP BY track")
    rows4 = cur.fetchall()
    print("The number of studets there are per track: ")
    for row in rows4:
        print(row)

    conn.close()


if __name__ == "__main__":
    main()
