import datetime


# Ehliyet Şartı

print("-"*30)
print("Ehliyet Alma Durumu Sorgulama")
print("-"*30)

isim = input("Adınız: ")
yas = int(input("Yaşınız: "))
egitim = input("Eğitim Durumunuz: ")

if (yas >= 18) and (egitim == "Lise") or (egitim == "Üniversite"):
    print(f"Sayın {isim} Ehliyet alabilirsin")
elif (yas <= 18) and (egitim == "Lise") or (egitim == "Üniversite"):
    print(f"Sayın{isim} Ehliyet için yaş yetersiz.")
    
elif (yas >= 18) and (egitim != "Lise") or (egitim != "Üniversite"):
    print(f"Sayın{isim} Ehliyet için eğitim yetersiz.")
else: 
    print(f"Sayın{isim} Ehliyet için hem yaş hem eğitim yetersiz.")

