class maths:
    def fraction(self,x):
        f = 1
        for i in range(1, x+1):
            f = f*i
        print(f'Freaction of {a} is:', f)
a = int(input('Enter a value: '))
obj = maths()
obj.fraction(a)