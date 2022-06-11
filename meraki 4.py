name="""rishabh - meerut
imtiyaz - delhi
nilima - cochin
rati - shimla
ayishah - delhi
raghu - shimla
naseer - kanpur
karthikeyan - delhi
salma - jaipur
pankaj - delhi
brijesh - delhi
govind - delhi
puneet - shimla
siddhi - delhi
suman - jaipur
rajeev - shimla
mohinder - delhi
rajendra - jaipur
priyanka - shimla
neela - delhi
sashi - jaipur
sarika - delhi
deepti - shimla
harshad - delhi
trishna - raipur
pradeep - jaipur
sekhar - delhi
nand - delhi
anoop - delhi
balwinder - tokyo"""
u=open("list.txt","w")
b=u.write(name)
print(b)
u.close()
b=open("list.txt","r")
f=b.read().splitlines()
print(f)
# for i in f:
#     if "delhi" in i:
#         f=open("delhi.txt","a")
#         f.write(i)
#         f.write("\n")
#         f.close()
#     if "shimla" in i:
#         f=open("shimla.txt","a")
#         f.write(i)
#         f.write("\n")
#         f.close()
#     if "delhi" not in i and "shimla" not in i:
#         f=open("other.txt","a")
#         f.write(i)
#         f.write("\n")
#         f.close()
# f=open("delhi.txt","r")
# print(f.read())



