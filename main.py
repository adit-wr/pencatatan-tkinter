import tkinter as tk
from tkinter import Tk, ttk, messagebox, Canvas, Frame, Label, Button, Entry, NO, END, simpledialog
from PIL import ImageTk, Image
import pandas as pd
from datetime import datetime
import csv
from LIBRARY import *


class CustomInputDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title="Input Dialog"):
        self.parent = parent
        self.result = False
        tk.simpledialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        tk.Label(master, text="Berat Gabah (kw):").grid(row=0)
        tk.Label(master, text="Harga Gudang:").grid(row=1)
        tk.Label(master, text="Jumlah pekerja:").grid(row=2)

        self.nama_buah_entry = tk.Entry(master)
        self.alamat_entry = tk.Entry(master)
        self.jumlah_pembelian_entry = tk.Entry(master)

        self.nama_buah_entry.grid(row=0, column=1)
        self.alamat_entry.grid(row=1, column=1)
        self.jumlah_pembelian_entry.grid(row=2, column=1)

        return self.nama_buah_entry  # Fokus pada entri nama buah

    def apply(self):
        nama_buah = self.nama_buah_entry.get()
        alamat = self.alamat_entry.get()
        jumlah_pembelian = self.jumlah_pembelian_entry.get()

        self.result = (nama_buah, alamat, jumlah_pembelian)


class CSVViewer:
    def __init__(self, root, canvas, file):
        self.file = file
        self.root = root
        self.canvas = canvas
        self.tampil = False

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=30)
        style.configure("Treeview.Heading", font=("Arial", 14))
        self.tree = ttk.Treeview(self.canvas,height=20)
        self.tree["columns"] = ("No","Tanggal","Waktu","Berat Gabah","Harga Gudang","Jumlah Pekerja","Penghasilan","Upah/orang","Penghasilan Pemilik")  

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("No", width=50, minwidth=50, anchor="center")
        self.tree.column("Tanggal", width=150, minwidth=150, anchor="center")
        self.tree.column("Waktu", width=150, minwidth=150, anchor="center")
        self.tree.column("Berat Gabah", width=150, minwidth=150, anchor="center")
        self.tree.column("Harga Gudang", width=150, minwidth=150, anchor="center")
        self.tree.column("Jumlah Pekerja", width=150, minwidth=150, anchor="center")
        self.tree.column("Penghasilan", width=150, minwidth=150, anchor="center")
        self.tree.column("Upah/orang", width=150, minwidth=150, anchor="center")
        self.tree.column("Penghasilan Pemilik", width=250, minwidth=250, anchor="center")

        self.tree.heading("No", text="No")
        self.tree.heading("Tanggal", text="Tanggal")
        self.tree.heading("Waktu", text="Waktu")
        self.tree.heading("Berat Gabah", text="Berat Gabah")
        self.tree.heading("Harga Gudang", text="Harga Gudang")
        self.tree.heading("Jumlah Pekerja", text="Jumlah Pekerja")
        self.tree.heading("Penghasilan", text="Penghasilan")
        self.tree.heading("Upah/orang", text="Upah/orang")
        self.tree.heading("Penghasilan Pemilik", text="Penghasilan Pemilik")

        self.top = Canvas(self.canvas, height=50)  
        self.top.pack(side="top", fill="x")
        self.bottom = Canvas(self.canvas, height=50)  
        self.bottom.pack(side="bottom", fill="x")
        self.frame = Frame(self.bottom)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.edit_button2 = Button(self.frame, text="Tambah", command=self.tambah, bg="green", width=20)
        self.edit_button2.pack(padx=25, side="left")

        self.tree.pack(expand=True, fill="both")

    def load_data(self,id_u):
        self.id_u = id_u
        self.tree.delete(*self.tree.get_children())
        banyakdatatree = len(self.tree.get_children())
        def rekursiff(awal,akhir,df,nom = 1):
            if awal < akhir:
                if df['Id'].iloc[awal] == id_u:
                    self.tree.insert("", "end", values=(nom, df['Tanggal'].iloc[awal], df['Waktu'].iloc[awal], df['Berat Gabah'].iloc[awal], df['Harga Gudang'].iloc[awal], df['Jumlah Pekerja'].iloc[awal], df['Penghasilan'].iloc[awal], df['Upah/orang'].iloc[awal], df['Penghasilan Pemilik'].iloc[awal]))
                    nom+=1
                rekursiff(awal+1,akhir,df,nom)
            else:
                return
        df = pd.read_csv(self.file, index_col=False)
        ldt = len(df)
        if ldt > banyakdatatree:
            rekursiff(banyakdatatree, ldt,df)
    def tambah(self):
        input = CustomInputDialog(root, title="Inputan Panen")
        if bool(input.result): 
            try:
                a = int(input.result[0])
                b = int(input.result[1])
                c = int(input.result[2])
                pushdata(self.id_u,a,b,c)
                self.load_data(self.id_u)
            except:
                messagebox.showerror("INVALID INPUT", "GAGAL MENAMBAH DATA\nPastikan semua inputan berupa angka")


class tampil:
    def __init__(self, root):
        self.root = root
        self.iduser = None
        self.image = Image.open("bb.jpg")
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background_label = Label(self.root, image=self.background_image, bg="black")
        self.background_label.pack(side="right", expand=True, fill="both")
        self.Username = self.textbox(-80,"Username")
        self.Password = self.textbox(0, "Password")
        self.buttonLogin = Button(root, text="Login", bg="green" ,width=10, command=self.Login)
        self.buttonLogin.place(relx=0.52,rely=0.6, anchor="center")
        self.buttonRegis = Button(root, text="Registrasi", bg="green", width=10, command=self.Regis)
        self.buttonRegis.place(relx=0.46,rely=0.6, anchor="center")
        self.buttonlogout = Button(root, text="Logout", bg="red", width=10, command=self.Logout)
        self.c = Frame(self.background_label, bg="gray")
        self.tabel = CSVViewer(self.background_label, self.c,"DATA.csv")

    def textbox(self,b,c):
        label = Label(self.root, text=c,font=("Arial", 12),width=23)
        # label.pack()
        label.place(relx=0.42, rely = 0.5, y=b)
        entry = Entry(self.root,font=("Arial", 18),width=16) # textBox
        entry.place(relx=0.42, rely = 0.5, y = b+23)
        return [label,entry]
    
    def clear(self):
        self.Username[0].place_forget()
        self.Username[1].delete(0, END)
        self.Username[1].place_forget()
        self.Password[0].place_forget()
        self.Password[1].delete(0, END)
        self.Password[1].place_forget()
        self.buttonLogin.place_forget()
        self.buttonRegis.place_forget()
        self.buttonlogout.place_forget()
        self.c.pack_forget()

    def Login(self):
        cek = login(self.Username[1].get(),self.Password[1].get()).status()
        if cek is not None:
            self.clear()
            self.iduser = cek
            self.Menu()
        else:
            messagebox.showerror("Login Gagal", "Username dan Password tidak sesuai")

    def Regis(self):
        user = self.Username[1].get()
        userpass = self.Password[1].get()
        if len(user) < 8 or len(userpass) < 8 or " " in user:
            kata = ""
            if len(user) < 8:
                kata = "Username Minimal 8 karakter"
            if " " in user:
                if len(kata) == 0:
                    kata += "Dilarang menggunakan karakter space"
                else:
                    kata += "\nUsername dilarang menggunakan karakter space"
            if len(userpass) < 8:
                if len(kata) == 0:
                    kata += "Password Minimal 8 karakter"
                else:
                    kata += "\nDan password Minimal 8 karakter"

            return messagebox.showwarning("Username dan Pasword", kata)

        cek = registrasi(user,userpass)
        if not cek.status():
            messagebox.showinfo("Sukses", "Username dan Password Berhasil ditambahkan")
            self.clear()
            self.iduser = cek.iduser
            self.Menu()
        else:
            messagebox.showerror("Username", "Username telah digunakan Buat username yang berbeda")
    
    def Menu(self):
        self.clear()
        self.buttonlogout.place(relx=0.95,rely=0.94, anchor="center")
        self.tabel.load_data(self.iduser)
        self.c.pack(pady=70)

    def Logout(self):
        self.clear()
        self.Username = self.textbox(-80,"Username")
        self.Password = self.textbox(0, "Password")
        self.buttonLogin = Button(root, text="Login", bg="green" ,width=10, command=self.Login)
        self.buttonLogin.place(relx=0.52,rely=0.6, anchor="center")
        self.buttonRegis = Button(root, text="Registrasi", bg="green", width=10, command=self.Regis)
        self.buttonRegis.place(relx=0.46,rely=0.6, anchor="center")


def cekData():
    try:
        open("DATA.csv")
    except:
        with open("DATA.csv", "w", newline="") as file:
            rd = csv.writer(file)
            rd.writerow(['Id','Tanggal','Waktu','Berat Gabah','Harga Gudang','Jumlah Pekerja','Penghasilan','Upah/orang','Penghasilan Pemilik'])

    try:
        open("Login.csv")
    except:
        with open("Login.csv","w",newline="") as file:
            rd = csv.writer(file)
            rd.writerow({'Username','Paswword','Id'})



if __name__ == "__main__":
    cekData()
    root = Tk()
    app = tampil(root)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.mainloop()