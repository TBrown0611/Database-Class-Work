from datetime import date#from the 'datetime' module import the 'date' function.
from datetime import datetime#from the 'datetime' module import the 'datetime' function.

class Person:#The code indented below this is a part of the 'Person' class.
    '''Defines a person.'''#Docstring.

    def __init__(self, firstname, surname, dob):#Defining the constructor - passing in 'self', 'firstname', 'surname' and 'dob'.
        '''Assigns instance variables for later use.'''#Docstring.

        self.firstname = firstname#'self.firstname is equal to 'firstname'.
        self.surname = surname#'self.surname' is equal to 'surname'.
        self.dob = datetime.strptime(dob, '%b %d %Y').date()#'self.dob' is equal to 'datetime.strptime', dob is presented in the format month, day, year.
        self.age = self.calculate_age(self.dob)#Caculating the age of the user using the date of birth entered by the user and the current date.

    def calculate_age(self, born):#Defining the 'calculate_age' function.
        '''Calculates age from Date of Birth'''#Docstring.

        today = date.today()#The 'today' variable is the current date.
        years_difference = today.year - born.year#The 'years_difference' variable equals the current year minus the year the user has input(born.year).
        is_before_birthday = (today.month, today.day) < (born.month, born.day)#This line detects whether the user has already had their birthday in the current year.
        elapsed_years = years_difference - int(is_before_birthday)#This line determines the user's age using the 'years_difference' and 'is_before_birthday' variable.
        return elapsed_years#Returns 'elapsed_years' for use in other sections of the code.
    
    
