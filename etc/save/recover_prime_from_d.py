from math import gcd #for gcd function (or easily implementable to avoid import)
import random #for random elements drawing in RecoverPrimeFactors

def failFunction():
	print("Prime factors not found")

def outputPrimes(a, n):
	p = gcd(a, n)
	q = int(n // p)
	if p > q:
		p, q = q, p
	print("Found factors p and q")
	print("p = {0}".format(str(p)))
	print("q = {0}".format(str(q)))
	return p,q


def RecoverPrimeFactors(n, e, d):
	"""The following algorithm recovers the prime factor
		s of a modulus, given the public and private
		exponents.
		Function call: RecoverPrimeFactors(n, e, d)
		Input: 	n: modulus
				e: public exponent
				d: private exponent
		Output: (p, q): prime factors of modulus"""

	k = d * e - 1
	if k % 2 == 1:
		failFunction()
		return 0, 0
	else:
		t = 0
		r = k
		while(r % 2 == 0):
			r = int(r // 2)
			t += 1
		for i in range(1, 101):
			g = random.randint(0, n) # random g in [0, n-1]
			y = pow(g, r, n)
			if y == 1 or y == n - 1:
				continue
			else:
				for j in range(1, t): # j \in [1, t-1]
					x = pow(y, 2, n)
					if x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q
					elif x == n - 1:
						continue
					y = x
					x = pow(y, 2, n)
					if  x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q


N = 68467069474804458789001075774184420276721174375995250030242738554585726402109569654437295860613003879739596798451841383614978297047751629345665419621894635025049166261226129943935413090051114660843761115160221691340800833293684624909407188872119353606551674332306352380787940669071938141417916730849158279283
e = 0x10001
d = 52969861659535994537112189221027399198782271150435435895500214732642020320828867818010195950694434223636064764513232428604151007754583683456875868152172403781744209485544987038191752913256939184282276831748711285314312591358660181283061346056724097087640197851314933575033042188065730066593695544639392863825

RecoverPrimeFactors(N, e, d)
