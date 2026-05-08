print("KALKULATOR ")
print("Ketik 'keluar' untuk berhenti")

while True:
    masukan_oprasi_perhitungan = input("Masukan operasi (+ | - | * | /): ").strip()
    angka_pertama = int(input("Masukan angka pertama : "))
    angka_kedua   = int(input("Masukan angka kedua   : "))

    if masukan_oprasi_perhitungan == "keluar":
        print("program selesai")
        break
    if masukan_oprasi_perhitungan not in ('+','-','*','/'):
        print("oprasi salah/tidak Valid")
    if masukan_oprasi_perhitungan == '+':
        hasil_perhitungan = angka_pertama + angka_kedua
        print(f"Hasil: {angka_pertama} + {angka_kedua} = {hasil_perhitungan}")
    elif masukan_oprasi_perhitungan == '-':
        hasil_perhitungan = angka_pertama - angka_kedua
        print(f"Hasil: {angka_pertama} - {angka_kedua} = {hasil_perhitungan}")
    elif masukan_oprasi_perhitungan == '*':
        hasil_perhitungan = angka_pertama * angka_kedua
        print(f"Hasil: {angka_pertama} X {angka_kedua} = {hasil_perhitungan}")
    elif masukan_oprasi_perhitungan == '/':
        hasil_perhitungan = angka_pertama / angka_kedua
        print(f"Hasil: {angka_pertama} - {angka_kedua} = {hasil_perhitungan}")


