#!/usr/bin/python3
class MyClass:
	x = 5
	def __init__(self, a, b=None):
		self.a = a
		self.b = b
	def add(self):
		if self.b == None:
			return self.a + MyClass.x
		return self.a + self.b

print(MyClass)
g = MyClass(312,18)
h = MyClass(30)
print(g.add())
print(h.add())
