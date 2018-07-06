
url = ""

class Billionair:
	def __init__(self,name,wealth=1.0):

		""" name,wealth both are added as private variables."""
		self._name = name   
		self._wealth  = wealth

	@property
	def name(self):
		return self._name

	@property
	def wealth(self):
		return self._wealth

	@name.setter
	def name(self,name):
		self._name = name

	@wealth.setter
	def wealth(self,wealth):
		try:
			self._wealth = float(wealth)
		except ValueError as e:
			raise ValueError("wealth should be a number") 
	
b = Billionair('Bill Gates')

print(b.name)
b.name = "Bill"
#b.wealth = "r"  # will produce Value Error 
print(b.name)