
while True:
    sayi = int(input("Lütfen negatif OLMAYAN bir sayı giriniz: "))

    if sayi < 0:
        print("Negatif sayı girdiniz, tekrar deneyiniz.")
        print("---")
        continue

    faktoriyel = 1

    for i in range(1, sayi + 1):
        faktoriyel *= i

    print(f"Faktöriyel değeriniz: {faktoriyel}")
    print("---")

    cevap = input("Başka bir sayı girmek ister misiniz? (evet/hayır): ").lower().strip()

    if cevap == "hayır" or cevap == "hayir":
        print("Programdan çıkılıyor. İyi günler!")
        break
