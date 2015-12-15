from time import time


def timeit(f):
	def wrap(*args):
		start = time()
		ret = f(*args)
		end = time()
		print '%s function took %0.3f ms' % (f.func_name, (end-start)*1000.0)
		return ret
	return wrap
