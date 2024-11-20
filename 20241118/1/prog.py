from collections import UserString

class DivStr(UserString):
	def __init__(self, value=""):
		super().__init__(value)

	def __floordiv__(self, n):
		size = len(self.data) // n
		return iter(self.data[i * size:(i + 1) * size] for i in range(n))

	def __mod__(self, n):
		size = len(self.data) // n
		remainder = len(self.data) % n
		return DivStr(self.data[-remainder:]) if remainder else DivStr()

import sys

exec(sys.stdin.read())
