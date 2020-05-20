import random
print(" Sayı Tahmin Uygulaması ".center(50,"*"))
print("\n")



baslangic = int(input("Rastgele sayı kaçtan başlasın: "))
bitis = int(input("Rastgele sayı kaçta bitsin: "))
sayi = random.randint(baslangic,bitis)
ad = input("Adınızı Girin: ")
hak = int(input("Kaç Hak İstiyorsunuz: "))
puan = 110

while hak > 0:
    hak -=1
    puan -=10
    tahmin = int(input("Sayı Tahmininizi Giriniz: "))
    if sayi < tahmin:
        print("Daha Küçük Rakam Yazmalısın!")
        if hak == 0:
            print("Hakkınız Bitti!")
        elif puan ==0:
            print("Puanınız '0' olduğu için Oyun bitti")
            break
    elif sayi > tahmin:
        print("Daha Büyük Sayı Yazmalısın!")
        if hak == 0:
            print("Hakkınız Bitti!")
        elif puan == 0:
            print("Puanınız '0' Olduğu için Oyun BİTTİ")
    else:
        print(f"*****Tebrikler {ad} !!! Doğru Cevap ***** - {sayi} - Oyun Skorunuz: {puan}")
        break
  