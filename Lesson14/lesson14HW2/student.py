from human import Human


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # --- comparison required by the task ---
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return str(self) == str(other)

    # --- to allow using Student in a set() ---
    def __hash__(self):
        return hash(str(self))
