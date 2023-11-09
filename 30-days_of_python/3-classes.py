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
	def get_a(self):
		return self.a
	def set_a(self, a):
		self.a = a



print(MyClass)
g = MyClass(312,18)
print(g.add() )
print(g.get_a())
g.set_a(1000)
print(g.add())
