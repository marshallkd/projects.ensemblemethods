import numpy as np

class Polynomial:

	def __init__(self, coeff = []):
		self.coeff = np.asarray(coeff, np.float32)
		self.deg = len(coeff) - 1
		self.var_name = 'x'

	def eval(self, x):
		Xt = np.vstack([x**i for i in range(0, self.deg+1)])
		return np.matmul(self.coeff,Xt)

	def show(self):

		def indeterminanter(i):
			if i == 0:
				return ''
			elif i == 1:
				return '*'+self.var_name
			else:
				return '*'+self.var_name+'^'+str(i)

		return ' + '.join([str(c)+indeterminanter(i) for i,c in enumerate(self.coeff)])

