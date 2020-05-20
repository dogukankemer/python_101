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
            print(f"Hakkınız Bitti! doğru sayı:{sayi}")
        elif puan ==0:
            print(f"Puanınız '0' olduğu için Oyun bitti. Doğru Cevap: {sayi}")
            break
    elif sayi > tahmin:
        print("Daha Büyük Sayı Yazmalısın!")
        if hak == 0:
            print(f"Hakkınız Bitti! Doğru Cevap: {sayi}")
        elif puan == 0:
            print(f"Puanınız '0' Olduğu için Oyun BİTTİ. Doğru Cevap: {sayi}")
    else:
        print(f"*****Tebrikler {ad} !!! Doğru Cevap ***** ({sayi}) Oyun Skorunuz: {puan}")
        break
  