# To do: 1) vizualize 2) research modules (including rpy)


# http://unicornsrest.org/reference/catan/maps/source.html
# http://www.mathpages.com/home/kmath093.htm

# want to compute expected values for number of resources collected given
# a tile number and the number of turns 

# individual probs are just number of dots / 36

# E(resources | n rolls and p prob on a single roll) 
# = n*n!/((n-0)!*0!)p^n + (n-1)*n!/((n-1)!*1!)p^(n-1)*(1-p)^1 + ... + n!/((n-n-1)!*n-1!)1*p^1*(1-p)^(n-1)



import math

def expected_haul(n, p):
# do a loop -- break when n - k < 0
	expected = 0.000000
	for k in range(0, n):
		expected += (n-k)*math.factorial(n)/(math.factorial(n-k)*math.factorial(k))*(p**(n-k))*((1-p)**k)
	return expected		


	
# p = raw_input("What is the combined probability of the dice outcomes you are evaluating? \n >")
n = 5
p = .333333

print expected_haul(n,p)



# would probably also want to be able to compare scenarios