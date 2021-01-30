def fakt(a):
	if a == 1:
		return 1
	elif a>0:
		return a*fakt(a-1)
