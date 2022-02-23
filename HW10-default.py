from collections import UserDict
from random import randint


class Field:
    def __init__(self, name) -> None:
        self.value = name

    def __str__(self) -> str:
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, *args) -> None:
        self.name = name
        self.phones = []
        self.add_phone(*args)

    def add_phone(self, *args) -> None:
        for item in args:
            if isinstance(item, Phone):
                self.phones.append(item)

    def __str__(self) -> str:
        return f"Name: {self.name}, phones : {', '.join([str(p) for p in self.phones])}"


class AddressBook(UserDict):
    def add_record(self, obj):
        if isinstance(obj, Record):
            self.data[obj.name] = obj

    def __str__(self) -> str:
        result = "\n".join([str(rec) for rec in self.data.values()])
        return result


if __name__ == "__main__":
    p_start = 10000000
    p_end = 99999999
    ab = AddressBook()
    rec = Record(Name("Bill"), Phone(str(randint(p_start, p_end))))
    ab.add_record(rec)
    rec = Record(Name("Jill"), Phone(str(randint(p_start, p_end))))
    ab.add_record(rec)
    for k in ab.data:
        ab.data.get(k).add_phone(Phone(str(randint(p_start, p_end))))

    print(ab)
