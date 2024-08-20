# Program Penghitung BMI

def hitung_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesitas"

# Meminta input pengguna
berat_badan = float(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))

# Menghitung dan menampilkan hasil BMI
bmi = hitung_bmi(berat_badan, tinggi_badan)
kategori = kategori_bmi(bmi)

print(f"Nilai BMI Anda: {bmi:.2f}")
print(f"Kategori: {kategori}")
