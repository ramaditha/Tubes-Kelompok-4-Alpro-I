import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def center_window(window, width, height):
    # Mendapatkan ukuran layar
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Menghitung posisi window di tengah layar
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Mengatur posisi window
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


class MoneyLog:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Log")
        self.root.geometry("700x400")
        self.root.configure(bg="#f4d5b7")

        # Variabel untuk menyimpan data
        self.saldo = 0
        self.transaksi = []

        # Entry widget untuk input jumlah pemasukan
        self.label_pemasukan = tk.Label(root, text="Input Pemasukan:", fg="#f3e8e3", bg="#9c9c9c", font=("Helvetica", 12))
        self.label_pemasukan.grid(row=1, column=9, padx=5, pady=2, sticky="E")
        self.entry_pemasukan = tk.Entry(root)
        self.entry_pemasukan.grid(row=1, column=10, padx=5, pady=2, sticky="E")
        self.btn_save_pemasukan = tk.Button(root, text="Simpan Pemasukan", fg="#f3e8e3", bg="#9c9c9c",font=("Helvetica", 12), command=self.save_pemasukan)
        self.btn_save_pemasukan.grid(row=1, column=11, padx=5, pady=2, sticky="W")
        # clear_entries()

        # Entry widget untuk input keterangan pemasukan
        self.label_keterangan = tk.Label(root, text="Input Keterangan:", fg="#f3e8e3", bg="#9c9c9c", font=("Helvetica", 12))
        self.label_keterangan.grid(row=2, column=9, padx=5, pady=2, sticky="E")
        self.entry_keterangan = tk.Entry(root)
        self.entry_keterangan.grid(row=2, column=10, padx=5, pady=2, sticky="E")
        # clear_entries()

        # Entry widget untuk input jumlah pengeluaran
        self.label_pengeluaran = tk.Label(root, text="Input Pengeluaran:", fg="#f3e8e3", bg="#9c9c9c", font=("Helvetica", 12))
        self.label_pengeluaran.grid(row=3, column=9, padx=5, pady=2, sticky="W")
        self.entry_pengeluaran = tk.Entry(root)
        self.entry_pengeluaran.grid(row=3, column=10, padx=5, pady=2, sticky="E")
        self.btn_save_pengeluaran = tk.Button(root, text="Simpan Pengeluaran", fg="#f3e8e3", bg="#9c9c9c", font=("Helvetica", 12), command=self.save_pengeluaran)
        self.btn_save_pengeluaran.grid(row=3, column=11, padx=5, pady=2, sticky="W")

        # Entry widget dan tombol untuk input keterangan pengeluaran
        self.label_pengeluaran_keterangan = tk.Label(root, text="Input Keterangan:", fg="#f3e8e3", bg="#9c9c9c", font=("Helvetica", 12))
        self.label_pengeluaran_keterangan.grid(row=4, column=9, padx=5, pady=5, sticky="E")
        self.entry_pengeluaran_keterangan = tk.Entry(root)
        self.entry_pengeluaran_keterangan.grid(row=4, column=10, padx=5, pady=5, sticky="E")

        # Tombol lihat Transaksi
        self.btn_lihat_transaksi = tk.Button(root, text="Lihat Transaksi", font=("Helvetica", 12), fg="#f3e8e3", bg="#9c9c9c", command=self.lihat_transaksi)
        self.btn_lihat_transaksi.grid(row=4, column=0, pady=4, sticky="N")

        # Tombol Keluar aplikasi
        self.btn_keluar = tk.Button(root, text="Keluar", fg="#322e2a", bg="#9c9c9c", font=("Helvetica", 12), command=root.quit)
        self.btn_keluar.grid(row=4, column=11, sticky="SE")

        # # Muat dan tampilkan gambar
        self.muat_dan_tampilkan_gambar()

    def muat_dan_tampilkan_gambar(self):
        # Muat gambar
        gambar = Image.open("moneylog.png")

        # Konversi gambar menjadi objek yang bisa ditampilkan di Tkinter
        self.gambar_tk = ImageTk.PhotoImage(gambar)

        # Buat label untuk menampil kan gambar
        self.label_gambar = tk.Label(self.root, image=self.gambar_tk, bg="#f4d5b7")
        self.label_gambar.grid(row=0, column=0, sticky="N")

        # Tambahkan label untuk menampilkan saldo di bawah gambar:
        self.label_saldo = tk.Label(self.root, text="Saldo Anda: Rp. {}".format(self.saldo), font=("Helvetica", 12), fg="#322e2a", bg="#f4d5b7")
        self.label_saldo.grid(row=3, column=0, padx=5, pady=5, sticky="N")
    # Simpan Pemasukan
    def save_pemasukan(self):
        pemasukan = self.entry_pemasukan.get()
        keterangan = self.entry_keterangan.get()
        try:
            pemasukan = float(pemasukan)
            self.saldo += pemasukan
            self.transaksi.append(("Pemasukan", pemasukan, keterangan))
            messagebox.showinfo("Info", "Pemasukan berhasil dicatat.")
            self.label_saldo.config(text="Saldo Anda: Rp. {}".format(self.saldo))
            self.entry_pemasukan.delete(0, 'end')
            self.entry_keterangan.delete(0, 'end')
        except ValueError:
            messagebox.showerror("Error", "Mohon masukkan angka untuk jumlah pemasukan.")
    # Simpan Pengeluaran
    def save_pengeluaran(self):
        pengeluaran = self.entry_pengeluaran.get()
        keterangan = self.entry_pengeluaran_keterangan.get()
        try:
            pengeluaran = float(pengeluaran)
            self.saldo -= pengeluaran
            self.transaksi.append(("Pengeluaran", pengeluaran, keterangan))
            messagebox.showinfo("Info", "Pengeluaran berhasil dicatat.")
            self.label_saldo.config(text="Saldo Anda: Rp. {}".format(self.saldo))
            self.entry_pengeluaran.delete(0, 'end')
            self.entry_pengeluaran_keterangan.delete(0, 'end')
        except ValueError:
            messagebox.showerror("Error", "Mohon masukkan angka untuk jumlah pemasukan.")
    # Pop Up Riwayat Transaksi
    def lihat_transaksi(self):
        transaksi_text = "Riwayat Transaksi Anda:\n"
        for jenis, jumlah, keterangan in self.transaksi:
            transaksi_text += "{}: Rp. {} - {}\n".format(jenis, jumlah, keterangan)
        messagebox.showinfo("Transaksi", transaksi_text)

root = tk.Tk()
app = MoneyLog(root)
# Mendapatkan ukuran layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Mendapatkan ukuran jendela
window_width = 700
window_height = 400

# Menghitung posisi jendela di tengah layar
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Mengatur posisi jendela
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
# Mengganti Logo Aplikasi
root.iconbitmap("icon.ico.ico")

root.mainloop()