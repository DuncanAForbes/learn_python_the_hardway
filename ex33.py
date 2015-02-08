
def count(a, b, c, d, e, f, g, h, i, k, l, m, n, o, p, q, r): 
	i = 0
	numbers = []	
	while i < r:
		print "At the top i is %d" % i
		i = i + a
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		print "The numbers: "

		for num in numbers:
			print num

count(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)

