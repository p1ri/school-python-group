class Person:

    def __init__(self, firstname, lastname, dateofbirth, address):
        self.firstname = firstname
        self.lastname = lastname
        self.dateofbirth = dateofbirth
        self.address = address

    def to_string(self):
        return f"{self.firstname} {self.lastname}, born on {self.dateofbirth}, living at {self.address}"