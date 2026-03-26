"""Problem 04: Practice WHERE, ORDER BY, LIMIT.

Task:
1. Get students with age >= 22
2. Sort students by age DESC
3. Return only top 3 oldest students
4. Get backend students younger than 23

Use parameterized queries for filter values.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO 1: age >= 22
    cur.execute("SELECT * FROM students WHERE age >= ?", (22,))
    rows1 = cur.fetchall()
    print("Age <=22: ")
    for row in rows1:
        print(row)
        
    

    # TODO 2 + 3: order by age desc, limit 3
    cur.execute("SELECT * FROM students ORDER BY age DESC LIMIT 3")
    rows2 = cur.fetchall()
    print("\nTop 3 oldest people in dataset")
    for row in rows2:
        print(row)

    # TODO 4: track='backend' and age < 23
    cur.execute("SELECT * FROM students WHERE track  = ? AND age < ?",
    ("backend",23)           
    )
    rows3 = cur.fetchall()
    print("\nBackend students younger than 23:")
    for row in rows3:
        print(row)
    conn.close()


if __name__ == "__main__":
    main()
