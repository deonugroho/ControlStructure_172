def fibonacci_banyak_suku(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Dua suku pertama deret Fibonacci
    deret = [0, 1]

    # Menghitung suku ke-3 hingga ke-n
    for i in range(2, n):
        suku_baru = deret[-1] + deret[-2]
        deret.append(suku_baru)

    return deret


# Contoh Penggunaan:
n = 10
hasil = fibonacci_banyak_suku(n)
print(f"{n} suku pertama deret Fibonacci:")
print(hasil)