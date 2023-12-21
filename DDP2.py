# Studi Kasus
# Di sebuah laboratorium, terdapat beberapa hasil penelitian tentang amoeba buatan. Amoeba buatan tersebut memiliki peningkatan populasi yang berbeda-beda.
# Berdasarkan hasil penelitian:

# Amoeba X1 memiliki peningkatan sebesar x ^ 2/menit.

# Amoeba X2 memiliki peningkatan sebesar x ^ 3/menit.

# Amoeba X3 memiliki peningkatan sebesar x ^ 4/menit.

# Dengan data yang kami miliki, kami ingin mengetahui berapa jumlah peningkatan setiap Amoeba buatan dalam waktu 10 menit kedepan


# 1) Memasukkan sistem numpy dan matplotlib
import numpy as np
import matplotlib.pyplot as plt

# 2) Memberikan interval/domain dari sebuah fungsi
x = np.arange(11) # sumbu x berisi barisan aritmatik angka 0-10
y = x**2 # sumbu y berisi perpangkatan dari barisan aritmatik sumbu x

# 3) Membuat visulaisasi berbentuk persegi
fig = plt.figure(figsize=(4,4), facecolor='grey', dpi=200) # figsize menentukan ukuran si persegi grafik, facecolor memberi warna pada background gambar, dpi berfungsi untuk meningkatkan resolusi gambar

# 4) Menentukan ukuran gambar berdasarkan satuan inci
ax = fig.add_axes([0,0,1,1])

# 5) Menentukan plot/masing-masing fungsi ke dalam grafik
ax.plot(x,y, label='Amoeba X1') # berdasarkan data Amoeba X1 meningkatkan populasi 2 kali lipat setiap menit
ax.plot(x,x**3, label='Amoeba X2') # berdasarkan data Amoeba X2 meningkatkan populasi 3 kali lipat setiap menit
ax.plot(x,x**4, label='Amoeba X3') # berdasarkan data Amoeba X3 meningkatkan populasi 4 kali lipat setiap menit

# 6) Memperjelas maksud tiap sumbu
ax.set_xlabel('Menit') # x
ax.set_ylabel('Jumlah Populasi') # y

# 7) Memberikan judul gambar grafik
ax.set_title('Hasil Penelitian Amoeba buatan')

# 8) Memberikan Legenda/penjelas maksud setiap fungsi (opsional)
ax.legend(loc=0)

# 9) Memberikan garis lintang dan bujur seperti globe agar mempermudah melihat grafik (opsional)
ax.grid(True)

# 10) Tampilkan gambar dengan bersih
plt.show()
