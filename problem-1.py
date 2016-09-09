"""
	PRIME1 - Prime Generator
	#number-theory
	Peter wants to generate some prime numbers for his cryptosystem. 
	Help him! Your task is to generate all prime numbers between two given numbers!

	Input

	The input begins with the number t of test cases in a single line (t<=10). 
	In each of the next t lines there are two numbers m 
	and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

	Output

	For every test case print all prime numbers p such that m <= p <= n,
	 one number per line, test cases separated by an empty line.

	Example

	Input:
	2
	1 10
	3 5

	Output:
	2
	3
	5
	7

	3
	5

@author: Avishek Arora
"""
from math import sqrt

def BruteForcePrime(n):
	"""Returns True if n is a prime number
	   Applies simple brute-force algorithm.
	   n:	number to check whether prime or not.
	"""
	if n > 1:
		for x in range(n-1, 1, -1):
			if n % x == 0:
				return False
		return True
	else:
		return False

def SieveOfEratosthenes(n):
	"""Returns list of Primes between 2 to n
	   Take advantage of sieve of eratosthenes algorithm
	   n:	upper bound starting from 2 to n
	"""
	n += 1
	numbers = [True] * n
	for i in range(0,int(sqrt(n))):
			if numbers[i] == True:
					for j in range((i+2)**2,n,(i+2)): #Using Formulae for crossing non-primes i.e i^2, i^2+i, i^2+2i, ... n
							numbers[j-2] = False #j-2 because starting memory from 0, hence saving two blocks of memeory locations.
	primes = [i+2 for i in range(0,n-2) if numbers[i] == True]
	return primes 

def SegmentedSOE(start, end):
	"""Returns a list of Primes between start to end
	   Uses Segmented sieve algorithm
	   start: lower bound >= 1, 
	   end:   upper bound <= 10^9
	   TC: O(n log log n),
	   SC: sqrt(n)
	"""
	#Get the primes till sqrt(end) + 1 using SOE
	segment_size = int(sqrt(end))
	primes = SieveOfEratosthenes(segment_size + 1)
	limit = segment_size
	composite = 0
	starting_segment_value = start
	while limit > 0:
		segment = [True] * segment_size
		for prime in primes:
			composite = (starting_segment_value // prime) * prime 
			
	
def run():
		testcases = input()
		assert testcases <= 10, "No: of test cases must be <= 10"
		inputs = []
		for i in range(0,testcases):
			inputs += [map(int, raw_input().split())]
				



	


		