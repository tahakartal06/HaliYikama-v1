def bilgünd():

    arama_terimi = input("Güncellemek istediğiniz müşterinin adı veya telefonunu giriniz: ").strip().upper()
    
    
    with open("veri1.txt", "r", encoding="utf8") as mus:
        müşteriler = mus.readlines()

    
    müşteri_bulundu = False
    for i, müşteri in enumerate(müşteriler):
        if arama_terimi in müşteri:  
            print(f"Bulunan Müşteri: {müşteri}")
            müşteri_bulundu = True
            
            adsoyad = input("Yeni Ad Soyad giriniz: ").strip().upper()
            telefon = input("Yeni Telefon numarasını giriniz: ").strip()
            while True:
                try:
                    ebatı = float(input("Yeni Metrekare giriniz: ").strip())  
                    break
                except ValueError:
                    print("Lütfen geçerli bir metrekare değeri giriniz.")
            adres = input("Yeni Adres giriniz: ").strip().upper()
            türü = türüekle()  

            
            yeni_müşteri = f"{adsoyad}___{telefon}___{türü}___{ebatı}m2___{adres}\n"
            
            müşteriler[i] = yeni_müşteri
            break

    if not müşteri_bulundu:
        print(f"{arama_terimi} ile eşleşen bir müşteri bulunamadı.")
        return
    
   
    with open("veri1.txt", "w", encoding="utf8") as mus:
        mus.writelines(müşteriler)
        print("Müşteri bilgileri başarıyla güncellendi.")

def türüekle():
    türler = ["yolluk", "dokuma", "kilim"]
    while True:
        print("Geçerli türler: Yolluk, Dokuma, Kilim")
        tür = input("Türünü giriniz: ").lower()  
        if tür in türler:
            print(f"Seçilen tür: {tür}")
            return tür
        else:
            print(f"Girdiğiniz tür, {türler} listesinde olmalı. Lütfen geçerli bir tür giriniz.")


bilgünd()