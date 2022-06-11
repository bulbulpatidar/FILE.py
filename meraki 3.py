f=open("quetion3.txt","w")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
for i in banks_list:
    print(i)
    a=f.write(i+"\n")
    # print(a)
f.close()
    