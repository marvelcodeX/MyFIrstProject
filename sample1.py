


class test:
    def write_file():
        f1=open("sample.txt","w")
        f1.write("This is a text")
        f1.close()


    def read_file():
        f2=open("sample.txt","r")
        print(f2.read())
        f2.close()



test.write_file()
test.read_file()


