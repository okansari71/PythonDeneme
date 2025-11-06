import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os

def select_pdf():
    pdf_path = filedialog.askopenfilename(
        title="PDF Dosyası Seç",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if pdf_path:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(0, pdf_path)

def convert_to_docx():
    pdf_path = entry_pdf.get()
    if not pdf_path:
        messagebox.showerror("Hata", "Lütfen bir PDF dosyası seçin.")
        return
    
    # DOCX kaydetme yeri seç
    docx_path = filedialog.asksaveasfilename(
        defaultextension=".docx",
        filetypes=[("Word Files", "*.docx")],
        title="Kaydedilecek Word Dosyasını Seçin"
    )
    if not docx_path:
        return

    try:
        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()
        messagebox.showinfo("Başarılı", f"Dönüştürme tamamlandı:\n{os.path.basename(docx_path)}")
    except Exception as e:
        messagebox.showerror("Hata", f"Dönüştürme başarısız:\n{e}")

# Tkinter Arayüzü
root = tk.Tk()
root.title("PDF → DOCX Dönüştürücü")
root.geometry("400x180")
root.resizable(False, False)

# PDF Dosya Seçimi
tk.Label(root, text="PDF Dosyası:", font=("Arial", 11)).pack(pady=10)
frame = tk.Frame(root)
frame.pack()

entry_pdf = tk.Entry(frame, width=40)
entry_pdf.pack(side=tk.LEFT, padx=5)

btn_browse = tk.Button(frame, text="Gözat", command=select_pdf)
btn_browse.pack(side=tk.LEFT)

# Dönüştürme Butonu
btn_convert = tk.Button(root, text="PDF'yi DOCX'e Dönüştür", command=convert_to_docx, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
btn_convert.pack(pady=20)

root.mainloop()
