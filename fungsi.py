from flask import Flask, render_template, request

app = Flask(__name__)

# Konsep OOP Kalkulator kita tetap dipertahankan
class Kalkulator:
    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b == 0:
            return "Error: Dibagi nol!"
        return a / b

# Instansiasi objek kalkulator
kal = Kalkulator()

# Routing web utama
@app.route('/', methods=['GET', 'POST'])
def beranda():
    hasil = None
    if request.method == 'POST':
        try:
            # Mengambil data dari form HTML
            angka1 = float(request.form['angka1'])
            angka2 = float(request.form['angka2'])
            operasi = request.form['operasi']

            # Menjalankan method OOP sesuai pilihan operator
            if operasi == 'tambah':
                hasil = kal.tambah(angka1, angka2)
            elif operasi == 'kurang':
                hasil = kal.kurang(angka1, angka2)
            elif operasi == 'kali':
                hasil = kal.kali(angka1, angka2)
            elif operasi == 'bagi':
                hasil = kal.bagi(angka1, angka2)
        except ValueError:
            hasil = "Error: Masukkan angka yang valid!"

    # Mengirimkan variabel 'hasil' kembali ke file index.html
    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)