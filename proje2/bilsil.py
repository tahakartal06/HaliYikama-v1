def bilsild():
    silinecek = input("Silmek istediğiniz kişinin adını veya telefon numarasını giriniz: ").upper()
    
    
    with open("veri1.txt", "r", encoding="utf8") as dosya:
        satirlar = dosya.readlines()
    
   
    yeni_satirlar = []
    bulundu = False
    for satir in satirlar:
        if silinecek in satir.upper():
            bulundu = True
            print(f"Bulunan kayıt: {satir.strip()}")
            onay = input("Bu kaydı silmek istediğinize emin misiniz? (E/H): ").upper()
            if onay == "E":
                print("Kayıt silindi.")
                continue  
            else:
                print("Silme işlemi iptal edildi.")
        yeni_satirlar.append(satir)
    
    
    with open("veri1.txt", "w", encoding="utf8") as dosya:
        dosya.writelines(yeni_satirlar)
    
    if not bulundu:
        print(f"{silinecek} bulunamadı.")