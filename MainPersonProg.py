from person import Person
import logic
import sys
from people_ import People_list

choices = ['A', 'a', 'B', 'b', 'Q', 'q']

def People_list_instance():
            People_list.people=[]

def Main():
    '''Create test users and add them to the people list.'''
    
    while True:
        Menutext()
        Menulogic()

def Menutext():
    ''' Menu defined here'''
    
    print ('Welcome to The Nameslist')
    print ('A = Add data to list')
    print ('B = View List')
    print ('Q = Quit')
    
def Menulogic():
    ''' The code that makes the menu function'''

    try:     
        people = logic.read_pickle_data('people_list.p')
    except FileNotFoundError as E:
        print('Error locating file:' + str(E))
        People_list_instance()
    Answer = ''
    Answer = input('Please Enter what you would like to do:')
    if Answer == choices[0] or Answer == choices[1]:
        logic.create_person()
    if Answer == choices[2] or Answer == choices[3]:
        logic.print_people()
    if Answer == choices[4] or Answer == choices[5]:
        logic.pickle_data('people_list.p', logic.people)
        print ('Goodbye')
        sys.exit()
    
if __name__ == '__main__':

    Main()
