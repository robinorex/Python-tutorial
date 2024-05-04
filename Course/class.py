#類別的定義與使用
class IO:        #定義類別IO
    supportedsrcs=["console","file"]    #定義變數 (屬性)
    def read(src):     #定義函式 (屬性)
        if src not in IO.supportedsrcs:
            print("not supported")
        else:
            print("Read from",src)
print(IO.supportedsrcs)
IO.read("file")
IO.read("internet")