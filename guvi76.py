x=int(raw_input())
factor=0
for i in range(1,x):
	if(x%i==0):
	 factor=i
if factor>1:
	print("yes")
elif x==1:
	print("neither prime nor composite")
else:
	print("no")
