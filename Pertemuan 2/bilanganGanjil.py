def cetak_bilangan_ganjil(n):
    # Loop mulai dari 1 sampai n dengan langkah (step) 2
    for i in range(1, n + 1, 2):
        print(i, end=" ")


# Menerima input dari pengguna
try:
    n = int(input("Masukkan nilai n: "))
    if n < 1:
        print("Harap masukkan bilangan bulat positif lebih besar dari 0.")
    else:
        print(f"Bilangan ganjil dari 1 sampai {n}:")
        cetak_bilangan_ganjil(n)
except ValueError:
    print("Input tidak valid! Harap masukkan angka bulat.")