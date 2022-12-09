class maths:
    def sub(self, x, y):
        return x-y
    def add(self,x,y):
        return x+y
    def mul(self, x,y):
        return x*y
    def div(self, x,y):
        return x/y

a = int(input('Enter first value: '))
b = int(input('Enter second value: '))
obj = maths()
print('mul:',obj.mul(a,b))
print('sub:',obj.sub(a,b))
print('div:',obj.div(a,b))
print('add:',obj.add(a,b))