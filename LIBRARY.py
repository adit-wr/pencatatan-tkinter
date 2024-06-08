import pandas as pd
import csv, locale
from datetime import datetime

class login:
    def __init__(self,username, password): # imutable ternary rekursif
        self.id = None
        pengembang = ("datalogin","password",0.1)
        def cek(dt):
            if pengembang[0] == username:
                if pengembang[1] == password:
                    self.id = pengembang[2]
                    return
            if len(dt) == 0:
                return
            else:
                if dt[0][0] == username:
                    self.id = dt[0][2] if dt[0][1] == password else None
                    if self.id is not None:
                        return 
                else:
                    cek(dt[1:])
        cek(pd.read_csv("Login.csv").values.tolist())

    def status(self):
        return self.id  

class registrasi: # filter chainin
    def __init__(self, Username, password):
        self.same = False
        self.iduser = None
        df = pd.read_csv("Login.csv")["Username"].tolist()
        def cek(x,y):
            return True if x == y else False
        filtered = list(filter(lambda x:cek(x,Username), df))
        print(filtered)
        if len(filtered) != 0:
            self.iduser = len(df)+1
            with open("Login.csv", "a", newline="") as file:
                write = csv.writer(file)
                write.writerow([Username,password,len(df)+1])
            self.same = False
        else:
            self.same = True

    def status(self):
        return self.same
    
class pushdata: # komposisi pure
    def __init__(self,iduser, inp, inp2, inp3):
        def f(x):
            return (x,x*5)
        def g(x):
            return x // 6
        def komposisi(x):
            return f(g(x))
        
        total = int(inp) * int(inp2) * 100
        hasilkotor = komposisi(total)
        berat = self.BeratPanen(int(inp))
        tgl = datetime.now().strftime('%Y-%m-%d')
        jam = datetime.now().strftime('%H:%M:%S')
        hg = self.MataUang(int(inp2))
        ttp = self.MataUang(total * 100)
        pp = self.MataUang(hasilkotor[1])
        up = self.MataUang(hasilkotor[0] // int(inp3))
        jp = f'{int(inp3)} orang'
        data_input = [iduser,tgl, jam, berat, hg,jp, ttp, up, pp]
        with open("DATA.csv", "a", newline="") as file:
            write = csv.writer(file)
            write.writerow(data_input)

    def BeratPanen(self, inp):
        if inp > 9:
            kw = inp % 10
            if kw == 0:
                berat = f'{inp//10} Ton'
            else:
                ton = (inp - kw) // 10
                berat = f'{ton} Ton {kw} Kw'
        elif inp > 0:
            berat = f'{inp} Kw'
        return berat
    
    def MataUang(self, inp):
        locale.setlocale(locale.LC_ALL, "id_ID")
        MU = locale.currency(inp, grouping=True).replace(",00","").replace("Rp","Rp ")
        return MU