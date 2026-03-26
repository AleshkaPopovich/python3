"""Lecture 02 exercises (classes) - implement from scratch.
Any 14 / 16 problems solved count as 100%
"""
from __future__ import annotations

from collections.abc import Iterator
from math import hypot
from typing import Any


class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def say_hi(self) -> None:
        print(f"Hello, I am {self.name}")


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance if balance >= 0 else 0.0

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount


class Team:
    def __init__(self) -> None:
        self.members: list[str] = []

    def add(self, name: str) -> None:
        self.members.append(name)

    def __len__(self) -> int:
        return len(self.members)


class QueueState:
    def __init__(self) -> None:
        self.items: list[str] = []

    def push(self, item: str) -> None:
        self.items.append(item)

    def pop(self) -> str | None:
        if not self.items:
            return None
        return self.items.pop(0)


class PaymentError(Exception):
    pass


class InsufficientFunds(PaymentError):
    pass


class Wallet:
    def __init__(self, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("balance must be non-negative")
        self.balance = balance

    def top_up(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount

    def pay(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise InsufficientFunds("not enough balance")
        self.balance -= amount


class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[dict[str, Any]] = []

    def add_item(self, name: str, price: float, qty: int = 1) -> None:
        if price < 0 or qty <= 0:
            return
        self.items.append({"name": name, "price": price, "qty": qty})

    def total_items(self) -> int:
        return sum(item["qty"] for item in self.items)

    def total_price(self) -> float:
        return sum(item["price"] * item["qty"] for item in self.items)

    def __repr__(self) -> str:
        return f"ShoppingCart(items={self.items!r})"


class Classroom:
    school_name = "Harbour Space"

    def __init__(self, group_name: str) -> None:
        self.group_name = group_name
        self.students: list[str] = []

    def add_student(self, name: str) -> None:
        self.students.append(name)

    def __len__(self) -> int:
        return len(self.students)

    def set_school_name(self, new_name: str) -> None:
        self.__class__.school_name = new_name


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = abs(width)
        self.height = abs(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Playlist:
    def __init__(self) -> None:
        self.songs: list[str] = []

    def add(self, song: str) -> None:
        self.songs.append(song)

    def __len__(self) -> int:
        return len(self.songs)

    def __iter__(self) -> Iterator[str]:
        return iter(self.songs)

    def __contains__(self, song: str) -> bool:
        return song in self.songs


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = max(price, 0.0)

    def get_price(self) -> float:
        return self.price

    def set_price(self, value: float) -> None:
        self.price = max(value, 0.0)

    def apply_discount(self, percent: float) -> None:
        percent = min(max(percent, 0.0), 100.0)
        self.price *= 1 - percent / 100


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        return f"Person(name={self.name})"


class Student(Person):
    def __init__(self, name: str, group: str) -> None:
        super().__init__(name)
        self.group = group

    def describe(self) -> str:
        return f"Student(name={self.name}, group={self.group})"


class Point2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: "Point2D") -> float:
        return hypot(self.x - other.x, self.y - other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y})"


class Inventory:
    def __init__(self) -> None:
        self.items: dict[str, int] = {}

    def add(self, name: str, qty: int = 1) -> None:
        if qty <= 0:
            return
        self.items[name] = self.items.get(name, 0) + qty

    def remove(self, name: str, qty: int = 1) -> None:
        if qty <= 0 or name not in self.items:
            return
        remaining = self.items[name] - qty
        if remaining > 0:
            self.items[name] = remaining
        else:
            self.items.pop(name, None)

    def count(self, name: str) -> int:
        return self.items.get(name, 0)

    def __contains__(self, name: str) -> bool:
        return self.count(name) > 0

    def __len__(self) -> int:
        return len(self.items)


class CourseCatalog:
    def __init__(self) -> None:
        self.courses: dict[str, str] = {}

    def add_course(self, code: str, title: str) -> None:
        self.courses[code] = title

    def get_title(self, code: str) -> str | None:
        return self.courses.get(code)

    def __iter__(self) -> Iterator[tuple[str, str]]:
        for code in sorted(self.courses):
            yield code, self.courses[code]

    def __len__(self) -> int:
        return len(self.courses)


class DefaultDict:
    def __init__(self, default_factory: Any = None) -> None:
        self.default_factory = default_factory if callable(default_factory) else None
        self.data: dict[Any, Any] = {}

    def __getitem__(self, key: Any) -> Any:
        if key in self.data:
            return self.data[key]
        if self.default_factory is None:
            return None
        value = self.default_factory()
        self.data[key] = value
        return value

    def __setitem__(self, key: Any, value: Any) -> None:
        self.data[key] = value

    def __contains__(self, key: Any) -> bool:
        return key in self.data

    def __len__(self) -> int:
        return len(self.data)
