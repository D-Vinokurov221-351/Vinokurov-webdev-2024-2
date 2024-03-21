class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

def sort_people_by_age(N, people):
    people.sort(key=lambda x: x.age)
    
    formatted_names = []
    for person in people:
        if person.gender == 'M':
            title = 'Mr.'
        else:
            title = 'Ms.'
        
        formatted_names.append(title + ' ' + person.first_name + ' ' + person.last_name)
    
    return formatted_names