#### USING ONLY Python's STANDARD LIBRARY COMPLETE THE FOLLOWING CODE

#### There are 5 methods worth 25 points that you must write to gain 
#### full credit for the my_sequence.py module: the reset methods 
#### for the Arithmetic and Geometric Classes, as well as, the asList 
#### methods for the Arithmetic, Geometric, and Quadratic Classes

import math

# An arithmetic sequence, is a sequence of numbers such that the 
# difference between consecutive terms is constant. This constant is referred
# to as the common difference. Any arithmetic sequence can be defined as a 
# linear function of the form f(n) = a1 + (n-1)d, where a1 is the first term,
# d is the common difference, and the domain n is the natural numbers 
# {1,2,3,..} 
class Arithmetic:
	# initializer with default first_term = 1, default common_difference = 5
	# and default max_terms = 10
	def __init__(self, first_term = 1, common_difference = 5, max_terms = 10):
		self.first_term = first_term
		self.common_difference = common_difference
		self.max_terms = max_terms
	
	# ****** COMPLETE THE METHOD BELOW	
	# @param mx_plus_b a string containing a linear expression of the form 
	# mx + b  
	# Precondition: mx_plus_b must be a valid linear expression in the form
	# mx + b 
	# sets first_term and common_difference to the correct values based on
	# the parameter mx_plus_b, default max terms = 5
	def reset(self, mx_plus_b = 'x', max_terms = 5):
		self.max_terms = max_terms
		self.first_term = 0
		found = False
		for i in range(0,len(mx_plus_b)):
			if mx_plus_b[i] == 'x':
				if len(mx_plus_b[0:i]) > 1:
					if mx_plus_b[0] != '-':
						self.common_difference = float(mx_plus_b[0:i])
					else:
						if len(mx_plus_b) >1:
							self.common_difference = float(mx_plus_b[1:i]) * -1
				else:
					if mx_plus_b[0] == '-':
						self.common_difference = -1
					else:
						self.common_difference = 1
				break
		for i in range(0,len(mx_plus_b)):
			if mx_plus_b[i] == '+':
				self.first_term = float(mx_plus_b[i+1:len(mx_plus_b)])
		self.first_term += self.common_difference
				
		
		
	# ****** COMPLETE THE METHOD BELOW
	# returns the sequence as a list
	# @param none 
	# @return a list containing the terms of the sequence rounded to 
	# a precision of 6
	def asList(self):
		list = [self.first_term]
		for i in range(1, self.max_terms):
			current = list[i-1] + self.common_difference
			list.append(round(current,6))
		return list

# A geometric sequence, is a sequence of numbers where each term after the
# first is found by multiplying the previous one by a fixed, non-zero number 
# called the common ratio. Any geometric sequence can be defined as an 
# exponential function of the form f(n) = a1(r)^n, where a1 is the first 
# term, r is the common ratio raised to the n power, and the domain n is 
# the whole numbers {0,1,2,3,..} 
class Geometric:
	# initializer with default first_term = 1, default common_ratio = 2
	# and default max_terms = 10
	def __init__(self, first_term = 1, common_ratio = 2, max_terms = 10):
		self.first_term = first_term
		self.common_ratio = common_ratio
		self.max_terms = max_terms
		
	# ****** COMPLETE THE METHOD BELOW	
	# @param arn a string containing an exponential expression of the form 
	# a(r)^n or r^n, r > 0, r not equal to 1, a not equal to 0  
	# Precondition: arn must be a valid exponential expression of the form
	# a(r)^n or r^n, r > 0, r not equal to 1, a not equal to 0   
	# sets first_term and common_ratio to the correct values based on
	# the parameter arn, default exponential expression = 2^n
	# default max terms = 5
	# @return void
	def reset(self, arn = '2^n', max_terms = 5):
		self.max_terms = max_terms
		self.common_ratio = 1
		self.first_term = 1
		if arn.find('(') != -1:
			openP = 0
			for i in range(0,len(arn)):
				if arn[i] == '(':
					openP = i
					if arn[0] == '-':
						self.first_term = float(arn[1:i]) * -1
					else:
						self.first_term = float(arn[0:i])
				if arn[i]==')':
					temp = arn[openP:i].replace('(','')
					if temp[0] == '-':
						self.common_ratio = float(temp[1:len(temp)]) * -1
					else:
						self.common_ratio = float(temp[0:len(temp)])
		else:
			temp = arn.split('^')[0]
			if temp[0] == '-':
				self.first_term = -1
				self.common_ratio = float(temp[1:len(temp)])
			else:
				self.first_term = 1
				self.common_ratio = float(temp[0:len(temp)])
	# ****** COMPLETE THE METHOD BELOW	
	# returns the sequence as a list
	# @param none 
	# @return a list containing the terms of the sequence rounded to 
	# a precision of 6
	def asList(self):
		list = [self.first_term]
		for i in range(1,self.max_terms):
			current = list[i-1] * self.common_ratio
			list.append(round(current,6))
		return list
		
	
# A quadratic sequence, is a sequence of numbers in which the second 
# differences between each consecutive term differ by the same amount, 
# called a common second difference. Any geometric sequence can be defined 
# as a quadratic function of the form f(n) = An^2 + Bn + C, where A, B, and
# C are constants, and n^2 means n raised to the 2nd power.
class Quadratic:
	# initializer with default constants A = 1, B = 0, C = 0
	# and default max_terms = 10
	def __init__(self, A = 1, B = 0, C = 0, max_terms = 10):
		self.A = A
		self.B = B
		self.C = C
		self.max_terms = max_terms
		
	# ****** COMPLETE THE METHOD BELOW	
	# returns the sequence as a list
	# @param none 
	# @return a list containing the terms of the sequence
	def asList(self):
		list = []
		for i in range(1,self.max_terms+1):
			current = (self.A * i * i) + (self.B * i) + self.C
			list.append(current)
		return list
	
