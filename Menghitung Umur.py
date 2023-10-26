import datetime
import os

os.system("clear")

print("=" * 20, "PROGRAM MENGHITUNG UMUR", 20 * "=", "\n")

print("Silakan masukan tanggal, bulan, dan tahun." "\n")

while True:
    tanggal = int(input("Tanggal\t: "))
    bulan = int(input("Bulan\t: "))
    tahun = int(input("Tahun\t: "))
    tanggal_lahir = datetime.date(tahun, bulan, tanggal)

    hari_ini = datetime.date.today()
    umur_hari = hari_ini - tanggal_lahir
    umur_tahun = umur_hari.days // 365
    umur_bulan_sisa = (umur_hari.days % 365) // 30

    print(f"\nUsia anda saat ini {umur_tahun} tahun, {umur_bulan_sisa} bulan. \n")

    is_done = input("Masih mau ngecek again ? (y/n)")

    if is_done == "n" or is_done == "N":
        break
print("PROGRAM SELESAI")
