import random

secenekler = ["taş", "kağıt", "makas"]

while True:
    oyuncu = input("Seçiminizi yapın (taş, kağıt, makas ya da çık): ").lower()
    if oyuncu == "çık":
        break
    if oyuncu not in secenekler:
        print("Geçersiz seçim.")
        continue
    bilgisayar = random.choice(secenekler)
    print(f"Bilgisayar: {bilgisayar}")
    if oyuncu == bilgisayar:
        print("Berabere!")
    elif (oyuncu == "taş" and bilgisayar == "makas") or          (oyuncu == "kağıt" and bilgisayar == "taş") or          (oyuncu == "makas" and bilgisayar == "kağıt"):
        print("Kazandınız!")
    else:
        print("Kaybettiniz!")
