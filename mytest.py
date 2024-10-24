class Person():
    def __init__(self , firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    @property    
    def fullname(self):    
        print (f'your fullname is : {self.firstname} {self.lastname}.')
    

one = Person('ghazal' , 'hafezi')
one.fullname


   