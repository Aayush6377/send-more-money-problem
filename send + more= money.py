import random
while 1:
	li=[x for x in range(0,10)]
	s=random.choice(li)
	li.remove(s)
	e=random.choice(li)
	li.remove(e)
	n=random.choice(li)
	li.remove(n)
	d=random.choice(li)
	li.remove(d)
	m=random.choice(li)
	li.remove(m)
	o=random.choice(li)
	li.remove(o)
	r=random.choice(li)
	li.remove(r)
	y=random.choice(li)
	li.remove(y)
	send=s*1000+ e*100+ n*10 +d
	more= m*1000+ o*100+ r*10 + e
	money= m*10000+ o*1000+ n*100 + e*10 + y
	if send+more==money and m!=0 and s!=0:
		break
print("s=",s)
print("e=",e)
print("n=",n)
print("d=",d)
print("m=",m)
print("o=",o)
print("r=",r)
print("y=",y)
print("send=",send)
print("more=",more)
print(send,"+",more,"=",send+more)
print("money=",money)

