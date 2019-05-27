def sec(f,e,a,b) :
	E=100
	while E>e :
		c=(a*f(b)-b*f(a) )/ (f(b)-f(a))
		(a,b)=(b,c)


		E=.5*abs(f(b))+.5*abs(f(a))

	print(a,b,E, f(a), f(b))
