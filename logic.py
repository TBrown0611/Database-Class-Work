from person import Person
import pickle
import MainPersonProg as Main

def create_person():
    ''' Creates a new user and asks for their data.'''

    firstname = input('Enter your firstname: \n>>')
    surname = input('Enter your surname: \n>>')
    dob = input('Enter your date of birth in the format, mmm dd yyyy: \n>>')
    ListaddP = Person(firstname, surname, dob)
    Main.People_list_instance()
    Peoplelist_.people.append(ListaddP)
    
def print_people():
    '''Iterates through the people list and prints out details'''
    
    for person in People_list.people:
        print('{0} {1} is {2} years old' .format(person.firstname, person.surname, person.age))        

def pickle_data(file, ListaddP):
    '''Opening a file and pickling data to it.'''
    
    with open('people_list.p', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        

def read_pickle_data(file):
    '''Unpickling the data from the file and reading it.'''

    with open('people_list.p', 'rb') as f:
        return pickle.load(f)




        


