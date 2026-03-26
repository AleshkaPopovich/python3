"""Problem 06: SQLAlchemy ORM models + Alembic migration.

Goal:
- Add SQLAlchemy ORM models
- Add one related model
- Initialize Alembic and run migration
- Verify schema update in sqlite_web

Steps:
1. Install dependencies (once):
       pip install sqlalchemy alembic sqlite-web
2. Complete models in `problems/db_models.py`:
   - Student (existing table)
   - Assignment (new related table)
3. From lectures/06/exercises run:
       alembic init migrations
4. Update `alembic.ini`:
       sqlalchemy.url = sqlite:///school.db
5. Update `migrations/env.py` to load metadata:

       import os
       import sys
       sys.path.append(os.path.join(os.getcwd(), "problems"))
       from db_models import Base
       target_metadata = Base.metadata

6. Generate migration:
       alembic revision --autogenerate -m "add assignments table"
7. Apply migration:
       alembic upgrade head
8. Verify in UI:
       python -m sqlite_web school.db
   Confirm `assignments` table exists.
"""


#from sqlalchemy import Integer, String, ForeignKey
#from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    track: Mapped[str] = mapped_column(String, nullable=False)

    assignments: Mapped[list["Assignment"]] = relationship(
        back_populates="student"
    )


class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"),
        nullable=False
    )

    student: Mapped["Student"] = relationship(
        back_populates="assignments"
    )