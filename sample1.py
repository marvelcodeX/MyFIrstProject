f1=open("sample.txt","w")
f1.write("This is a text")
f1.close()

f2=open("sample.txt","r")
print(f2.read())
f2.close()


print("Ji")