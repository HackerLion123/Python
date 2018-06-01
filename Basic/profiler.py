import cProfile, pstats, io


#COMMAND_LINE: It can also done 'python3 -m cProfile script arg' this can do profiling

def profile(fnc):
	"""A decorator that uses cprofile to profile a fnc. It is just a regular decorator function."""

	def inner(*args, **kwargs):
		pr = cProfile.Profile()

		pr.enable()
		return_value = fnc(*args, **kwargs)
		pr.disable()

		s = io.StringIO()
		sortby = 'cumulative'
		pstatus = pstats.Stats(pr,stream = s).sort_stats(sortby)
		pstatus.print_stats()
		print(s.getvalue())
		return return_value
	return inner



