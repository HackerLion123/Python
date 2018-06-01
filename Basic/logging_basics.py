import logging

#DEBUG: Detailed information, typically of interest only when diagnosing problems.

#INFO: Confirmation that the things are working properly.

#WARNING: An indication that something unexpected happend, or indication of a problem in near future. The software is still working properly. 

#ERROR: Due to a serious problem, the software has not been able to perform some function.

#CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

class Employee:

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary

		logging.Info("New object created")

	def work(self):
		pass;

	def __exit__(self):
		pass;

	def __enter__(self):
		pass;


