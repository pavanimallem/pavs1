N,M=map(int,raw_input().split())
K=N*M
for i in range(K+1):
	if K==i*i:
		print("yes")
		break
else:
	print "no"
		
