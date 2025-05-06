import tkinter as tk
from tkinter import ttk
from pyswip import Prolog
from tkinter import messagebox

# Inisialisasi prolog
prolog = Prolog()
prolog.consult("jurusanku_gui.pl")

jurusan = list()
minat = dict()
index_jurusan = 0
index_minat = 0
current_jurusan = ""
current_minat = ""

def mulai_penentuan():
    global jurusan, minat, index_jurusan, index_minat

    # Bersihkan database prolog
    prolog.retractall("minat_pos(_)")
    prolog.retractall("minat_neg(_)")

    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)

    # Mendapatkan daftar jurusan dan minat
    jurusan = [p["X"].decode() for p in list(prolog.query("jurusan(X)"))]
    for p in jurusan:
        minat[p] = [g["X"] for g in list(prolog.query(f'minat(X, "{p}")'))]

    index_jurusan = 0
    index_minat= -1
    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_jurusan=False):
    global current_jurusan, current_minat, index_jurusan, index_minat

    # Atur index jurusan
    if ganti_jurusan:
        index_jurusan += 1
        index_minat = -1

    # Apabila daftar jurusan sudah habis berarti tidak terdeteksi penyakit
    if index_jurusan >= len(jurusan):
        hasil_penentuan()
        return

    current_jurusan = jurusan[index_jurusan]

    # Atur index minat
    index_minat += 1

    # Apabila semua gejala dari penyakit habis, berarti terdeteksi penyakit tsb
    if index_minat >= len(minat[current_jurusan]):
        hasil_penentuan(current_jurusan)
        return

    current_minat = minat[current_jurusan][index_minat]

    # Cek status gejala di database prolog
    if list(prolog.query(f"minat_pos({current_minat})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"minat_neg({current_minat})")):
        pertanyaan_selanjutnya(ganti_jurusan=True)
        return

    # Mendapatkan pertanyaan baru
    pertanyaan = list(prolog.query(f"pertanyaan({current_minat}, Y)"))[0]["Y"].decode()

    # Set pertanyaan ke kotak pertanyaan
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)


def jawaban(jwb):
    if jwb:
        prolog.assertz(f"minat_pos({current_minat})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"minat_neg({current_minat})")
        pertanyaan_selanjutnya(ganti_jurusan=True)


def hasil_penentuan(jurusan=""):
    if jurusan:
        messagebox.showinfo("Hasil Rekomendasi", f"Kamu cocok masuk jurusan {jurusan}.")
    else:
        messagebox.showinfo("Hasil Rekomendasi", "Tidak ditemukan jurusan yang cocok berdasarkan minatmu.")

    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)


# Inisialisasi window utama
root = tk.Tk()
root.title("Sistem Pakar Pemilihan Jurusan Kuliah")

# Inisialisasi frame utama
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Membuat widget yang diperlukan
ttk.Label(mainframe, text="Aplikasi Pemilihan Jurusan Kuliah", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=4, width=40, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Konsultasi", command=mulai_penentuan)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Tambah padding ke setiap widget
for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Menjalankan GUI
root.mainloop()