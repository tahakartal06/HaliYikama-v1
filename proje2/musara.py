def musarad():
    arama = input("Aramak istediğiniz müşteri adı veya telefon numarasını girin: ").upper()
    
    try:
        with open("veri1.txt", "r", encoding="utf8") as dosya:
            bulundu = False
            for satir in dosya:
                if arama in satir.upper():
                  
                    temiz_satir = satir.replace("___", " | ")
                    print("Bulunan müşteri bilgisi:")
                    print(temiz_satir.strip())
                    bulundu = True
            
            if not bulundu:
                print("Aradığınız müşteri bulunamadı.")
                
    except FileNotFoundError:
        print("Henüz veri dosyası oluşturulmamış.")