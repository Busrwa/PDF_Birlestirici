import PyPDF2
from tkinter import Tk, filedialog
import os

def pdf_birleştir(pdf_dosyaları, çıktı_dosyası):
    birleştirici = PyPDF2.PdfMerger()

    for dosya in pdf_dosyaları:
        birleştirici.append(dosya)

    with open(çıktı_dosyası, 'wb') as çıktı:
        birleştirici.write(çıktı)

def dosya_seç():
    Tk().withdraw()
    dosyalar = filedialog.askopenfilenames(title="PDF Dosyalarını Seçin", filetypes=[("PDF Dosyaları", "*.pdf")])
    return dosyalar

def çıktı_dosyası():
    Tk().withdraw()
    dosya = filedialog.asksaveasfilename(title="Çıktı PDF Dosyasını Kaydedin", defaultextension=".pdf", filetypes=[("PDF Dosyaları", "*.pdf")])
    return dosya

if __name__ == "__main__":
    print("PDF Birleştiriciye Hoş Geldiniz!")
    print("Birleştirmek istediğiniz dosyaları seçin..")

    pdf_dosyaları = dosya_seç()
    if not pdf_dosyaları:
        print("PDF dosyaları seçilmedi.")
    else:
        masaüstü_yolu = os.path.join(os.path.join(os.environ['USERPROFILE']),
                                     'Desktop') if os.name == 'nt' else os.path.join(os.path.expanduser('~'), 'Desktop')

        if not os.path.exists(masaüstü_yolu):
            os.makedirs(masaüstü_yolu)

        çıktı_dosyası = os.path.join(masaüstü_yolu, 'birlesmis_dosya.pdf')

        pdf_birleştir(pdf_dosyaları, çıktı_dosyası)
        print(f"PDF dosyaları başarıyla {çıktı_dosyası} dosyasına birleştirildi!")