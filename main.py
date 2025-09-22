from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self,value):
        if value.isdigit() and len(value) == 10:
            super().__init__(value)
        else:
            raise ValueError("Phone number must be exactly 10 digits")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Method to add a phone number
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Method to remove a phone number
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    # Method to edit a phone number
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError("Old phone number not found")
    
    # Method to find a phone number
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

# Checking of class functionality
# try:
#     book=AddressBook()
#     dof_record = Record("Dof")
#     dof_record.add_phone("1234567890")
#     dof_record.add_phone("0987654321")
#     dof_record.edit_phone("1234567890", "1112223333")
#     new_record = Record("New")
#     new_record.add_phone("5556667777")
#     book.add_record(dof_record)
#     book.add_record(new_record)
#     print(book)
# except ValueError as e:
#     print(e)