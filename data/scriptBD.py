from compushow_app.models import Computista
f = open('computistas.txt', 'r+')
for line in f:
	t=line.split()
	i=1
	n=''
	while i<len(t):
		n+=t[i]+' '
		i+=1
	n=n[:len(n)-1]
	c=Computista.objects.create(carnet = t[0], nombre = n)
	c.save()
