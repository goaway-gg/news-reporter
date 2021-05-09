class SomeClass(object):
    attr1 = 42

    def method1(self, x):
        return 2*x

obj = SomeClass()
obj.method1(6) # 12
obj.attr1 # 42

def ret():
	x = 13+1
	y = 7
	c = x*y
	return c
ret()
print(ret())