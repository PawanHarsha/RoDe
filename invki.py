import math
l1=int(input("the length of first arm is:"))
l2=int(input("the length of second arm is:"))
l3=int(input("the length of third arm is:"))
px=int(input("the x co-ordinate of end effector:"))
py=int(input("the y co-ordinate of end effector:"))
pz=int(input("the z co-ordinate of end effector:"))
"""angles=int(input("do you like to input angles:")) # enter 0 if no, 1 if yes
if angles== True:
    th1= math.radians(int(input("the first angle is:")))
    th2= math.radians(int(input("the second angle is:")))
    th3= (3*math.pi/2)+math.radians(int(input("the third angle is:")))
#def for_ki():
    nd_efx= math.cos(th1)*((l2*math.cos(th2))+(l3*math.cos(th2+th3)))
    nd_efy= math.sin(th1)*((l2*math.cos(th2))+(l3*math.cos(th2+th3)))
    nd_efz= l1+((l2*math.sin(th2))+(l3*math.sin(th2+th3)))
#for_ki()
print(nd_efx, nd_efy, nd_efz, sep=',')"""
th1=[math.atan2(py, px), math.pi+math.atan2(py, px)]
de= (px**2)+(py**2)+(pz**2)
c3=((px**2)+(py**2)+((pz-l1)**2)-(l2**2)-(l3**2))/(2*l2*l3)
print(c3)
s3=math.sqrt(1-(c3**2))
th3=[math.atan2(-s3, c3), math.atan2(s3,c3)]
s2=(((l2+l3*c3)*pz)-(l3*s3*math.sqrt(px**2+py**2)))/de
c2=(((l2+l3*c3)*math.sqrt(px**2+py**2))+(l3*s3*pz))/de
th2=math.atan2(s2,c2)
s=[math.degrees(th1[0]), math.degrees(th3[0]), math.degrees(th2)]
print(s[0], s[1], s[2], sep=',')


