
url = ""
class Billionair:
	def __init__(self,name,wealth):

		""" name,wealth both are added as private variables."""
		self._name = name   
		self._wealth  = wealth

	@property
	def name(self):
		return self._name

	@property
	def wealth(self):
		return self._wealth
		