"""Problem 07: Create and read data with SQLAlchemy.

Task:
1. Open a SQLAlchemy Session on `school.db`.
2. Create one Assignment for an existing student.
3. Read all students.
4. Read students with age >= 22 sorted by age descending.
5. Read assignments with joined student names.

Starter:
- Reuse `Student` and `Assignment` from `db_models.py`.
- Use `select(...)` queries.
"""

#from sqlalchemy import create_engine, select
#from sqlalchemy.orm import Session

from db_models import Assignment, Student

DB_URL = "sqlite:///school.db"


def main() -> None:
    engine = create_engine(DB_URL, echo=False)

    with Session(engine) as session:
        student = session.scalars(select(Student).order_by(Student.id)).first()
        if student is None:
            print("No students found. Add students before creating assignments.")
            return

        assignment = session.scalars(
            select(Assignment).where(
                Assignment.student_id == student.id,
                Assignment.title == "SQLAlchemy intro",
            )
        ).first()
        if assignment is None:
            assignment = Assignment(
                title="SQLAlchemy intro",
                score=95,
                student=student,
            )
            session.add(assignment)
            session.flush()
            print(f"Added assignment for {student.name}: {assignment.title} ({assignment.score})")
        else:
            print(
                f"Assignment already exists for {student.name}: "
                f"{assignment.title} ({assignment.score})"
            )

        all_students = session.scalars(select(Student).order_by(Student.id)).all()
        print("\nAll students:")
        for current_student in all_students:
            print(
                current_student.id,
                current_student.name,
                current_student.age,
                current_student.email,
                current_student.track,
            )

        filtered_students = session.scalars(
            select(Student)
            .where(Student.age >= 22)
            .order_by(Student.age.desc(), Student.id)
        ).all()
        print("\nStudents age >= 22 (oldest first):")
        for current_student in filtered_students:
            print(current_student.id, current_student.name, current_student.age)

        assignment_rows = session.execute(
            select(Assignment.title, Assignment.score, Student.name)
            .join(Assignment.student)
            .order_by(Assignment.id)
        ).all()
        print("\nAssignments with student names:")
        for title, score, student_name in assignment_rows:
            print(title, score, student_name)

        session.commit()


if __name__ == "__main__":
    main()
