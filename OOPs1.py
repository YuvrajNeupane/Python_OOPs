# What OOPs? (Object Orianted Programmin g)
'''
It's a programming approach based on CLASS and OBJECT.
                or
Its a method to represent real world entityin profram.
                                                     '''

# OOPs features:
'''
1. Class & Objects -> create class and define objects
2. Inheritance     -> Code reusability
3. Polymorphism    -> One object can show diffent behaviors (poly = many, morphism = form)
   # Two types of polymorphism:
   a. Overloading - (Operator, Function)
   b. Overriding
4. Incapsulation   -> Grouping of requred functions and variables in a single unit
5. Abstraction     -> process of hiding the internal details of an application from the outer world
                                                                                                    '''

# What is the access modifire? 
'''
Access modifire are used to set the limit of member accessebility.
1. Public
2. Protected (_) use _var
3. Private (__) use __var
                                                                 '''
class A: #(This is our parent class)
    a = 10    # public
    _b = 20   # Protected
    __c = 30  # Private
    print(a, '', _b, '', __c) # we can access in the SAME CLASS.

    # We can use PUBLIC and Protected variables outside the class
    def add(self):
        self.__c = self.a+self._b
        print('Addition: ',self.__c)
# createing object of class access

addition = A()
addition.add()
print(addition.a)
print(addition._b)
#print(addition.__c) #If you run this variable it won't print because it's a private variable (AttributeError: 'access' object has no attribute '__c')

class B(A): # (This is a child class)
    def show(self):
        print(self.a)
        print(self._b)
        print(self.__c)
obj = B
obj.show()