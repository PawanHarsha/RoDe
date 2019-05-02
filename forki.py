import math
l1=int(input("the length of first arm is:"))
l2=int(input("the length of second arm is:"))
l3=int(input("the length of third arm is:"))
angles=int(input("do you like to input angles:")) # enter 0 if no, 1 if yes
if angles== True:
    th1= math.radians(int(input("the first angle is:")))
    th2= math.radians(int(input("the second angle is:")))
    th3= (3*math.pi/2)+math.radians(int(input("the third angle is:")))
#def for_ki():
    nd_efx= math.cos(th1)*((l2*math.cos(th2))+(l3*math.cos(th2+th3)))
    nd_efy= math.sin(th1)*((l2*math.cos(th2))+(l3*math.cos(th2+th3)))
    nd_efz= l1+((l2*math.sin(th2))+(l3*math.sin(th2+th3)))
#for_ki()
print(nd_efx, nd_efy, nd_efz, sep=',')

