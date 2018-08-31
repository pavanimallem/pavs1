string=raw_input()
c=0
for x in string:
	if(x=='a' or x=='A' or x=='e' or x=='E' or x=='i' or x=='I' or x=='o' or x=='O' or x=='u' or x=='U'):
		c+=1
if(c>=1):
	       print("yes")
else:
	       print("no")
