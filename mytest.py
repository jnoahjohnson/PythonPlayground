class Person():
    university = "BYU"
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = "John"
    
myPerson = {
    'first_name': 'noah'
}

new_person = Person("noah")
print(new_person.university)
new_person.university = "UVU"
another_person = Person("someone")
print(new_person.university)
print(another_person.university)