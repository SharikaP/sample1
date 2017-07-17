class myError(Exception):
	def __init__(self, value):
		self.value=value
	def __str__self(self):
		return(repr(self.value))
try:
	raise(myError(2))
except myError as e:
	print ("A new exception occured: "+str(e.value))