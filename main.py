# Oyun alanındaki yatay çizgi sayısını kullanıcıdan alan ve kontrol eden fonksiyon
def sayi_al_kontrol_et(alt_sinir, ust_sinir):
    hatali_giris = True
    while hatali_giris:
        try:
            sayi = float(input())
            if alt_sinir <= sayi <= ust_sinir and int(sayi) == sayi:
                hatali_giris = False
            else:
                print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
        except ValueError:
            print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")

    return int(sayi)


# Hamleyi kullanıcıdan alan ve hamlenin koordinat listesinde olup olmadığını kontrol eden fonksiyon
def hamle_giris_kontrol(koordinat_liste):
    hamle = input("Lütfen hamlenizi giriniz: ")
    while hamle.upper() not in koordinat_liste:
        print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
        hamle = input("Lütfen hamlenizi doğru giriniz: ")
    return hamle.upper()


# Çıktı biçimlendirme ve hizalama yapan fonksiyon
def oyun_alanini_goruntule(satir_sayisi, iki_boyutlu_liste, harfler_listesi):
    print(" ", end="")
    for i in range(satir_sayisi + 1):  # Tablo başındaki sütun isimlerini yazdırma
        print(f" {harfler_listesi[i]}", end="  ")
    print()
    for j in range(satir_sayisi):  # Satır numaralarını yazdırma
        print(f"{(j + 1)}", end=" ")
        for k in range(satir_sayisi + 1):
            print(f"{iki_boyutlu_liste[j][k] }", end="")
            if k != satir_sayisi:
                print(f"---", end="")
        print(f"  {(j + 1)}")
        if j != satir_sayisi - 1:  # Satır numarasının altına dikey çizgi konmaması için kontrol
            for m in range(satir_sayisi + 1):
                print(f"  |", end=" ")
            print()
    print(" ", end="")
    for i in range(satir_sayisi + 1):  # Tablo başındaki sütun isimlerini yazdırma
        print(f" {harfler_listesi[i]}", end="  ")
    print()


# Taşın yerleşirileceği hamleyi alarak kontrolünü yaptıktan sonra yerleştiren ve oyun alanını görüntületen fonksiyon
def taslari_yerlestir(satir_sayisi, koordinat_liste, iki_boyutlu_liste, harfler_listesi):
    tur_sayisi = int(satir_sayisi * (satir_sayisi + 1))
    renk = "B"
    for tur in range(tur_sayisi):
        hamle = hamle_giris_kontrol(koordinat_liste)
        # taşın konulmak istendiği koordinatın boş olıup olmadığını kontrol eden döngü
        while iki_boyutlu_liste[int(hamle[0]) - 1][harfler_listesi.index(hamle[1])] != " ":
            print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
            hamle = hamle_giris_kontrol(koordinat_liste)
        # taşı yerleştirme
        iki_boyutlu_liste[int(hamle[0]) - 1][harfler_listesi.index(hamle[1])] = renk
        if renk == "B":
            renk = "S"
        else:
            renk = "B"
            print("Hamle sonrası oyun alanı aşağıdaki gibidir:")
        oyun_alanini_goruntule(satir_sayisi, iki_boyutlu_liste, harfler_listesi)


# hem siyah hem beyaz oyuncu için q sayısını hesaplayan ve bu sayıları geri döndüren fonksiyon
def kare_sayma(satir_sayisi, iki_boyutlu_liste):
    beyaz_kare_sayisi = 0
    siyah_kare_sayisi = 0
    renk = ["B", "S"]
    for i in range(satir_sayisi - 1):
        for j in range(satir_sayisi):
            if iki_boyutlu_liste[i][j] == renk[0]:
                if iki_boyutlu_liste[i][j+1] == renk[0] and iki_boyutlu_liste[i+1][j] == renk[0] and iki_boyutlu_liste[i+1][j+1] == renk[0]:
                    beyaz_kare_sayisi += 1
            elif iki_boyutlu_liste[i][j] == renk[1]:
                if iki_boyutlu_liste[i][j+1] == renk[1] and iki_boyutlu_liste[i+1][j] == renk[1] and iki_boyutlu_liste[i+1][j+1] == renk[1]:
                    siyah_kare_sayisi += 1
    return beyaz_kare_sayisi, siyah_kare_sayisi


# Hamle sonrası yeni kare oluşup oluşmadığına bakan fonksiyon
def yeni_kare_olusmus_mu(yeni_konum, iki_boyutlu_liste, harfler_listesi):
    kare = False
    x = int(yeni_konum[0]) - 1
    y = harfler_listesi.index(yeni_konum[1])
    renk = iki_boyutlu_liste[x][y]
    # Noktanın sol üst çaprazında kare oluşup oluşmadığını kontrol ediyor
    try:
        if iki_boyutlu_liste[x - 1][y - 1] == renk and iki_boyutlu_liste[x - 1][y] == renk and iki_boyutlu_liste[x][y - 1] == renk and x >= 1 and y >= 1:
            kare = True
    except IndexError:
        pass
    # Noktanın sağ üst çaprazında kare oluşup oluşmadığını kontrol ediyor
    try:
        if iki_boyutlu_liste[x - 1][y] == renk and iki_boyutlu_liste[x - 1][y + 1] == renk and iki_boyutlu_liste[x][y + 1] == renk and x >= 1 and y >= 1:
            kare = True
    except IndexError:
        pass
    # Noktanın sol alt çaprazında kare oluşup oluşmadığını kontrol ediyor
    try:
        if iki_boyutlu_liste[x][y - 1] == renk and iki_boyutlu_liste[x + 1][y - 1] == renk and iki_boyutlu_liste[x + 1][y] == renk and y >= 1:
            kare = True
    except IndexError:
        pass
    # Noktanın sağ alt çaprazında kare oluşup oluşmadığını kontrol ediyor
    try:
        if iki_boyutlu_liste[x + 1][y + 1] == renk and iki_boyutlu_liste[x][y + 1] == renk and iki_boyutlu_liste[x + 1][y] == renk:
            kare = True
    except IndexError:
        pass
    return kare


# Beyaz oyuncunun siyah taş çıkarması için hamle girmesini sağlayan ve hamlenin doğruluğunu kontrol eden fonksiyon
def beyaz_oyuncu_icin_siyah_tas_cikarma_hamlesi_al_kontrol_et(koordinat_liste, iki_boyutlu_liste, harfler_listesi):
    cikarma_hamlesi = hamle_giris_kontrol(koordinat_liste)
    while iki_boyutlu_liste[int(cikarma_hamlesi[0]) - 1][harfler_listesi.index(cikarma_hamlesi[1])] == "B" or \
            iki_boyutlu_liste[int(cikarma_hamlesi[0]) - 1][harfler_listesi.index(cikarma_hamlesi[1])] == " ":
        print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
        cikarma_hamlesi = hamle_giris_kontrol(koordinat_liste)
    return cikarma_hamlesi


# Siyah oyuncunun beyaz taş çıkarması için hamle girmesini sağlayan ve hamlenin doğruluğunu kontrol eden fonksiyon
def siyah_oyuncu_icin_beyaz_tas_cikarma_hamlesi_al_kontrol_et(koordinat_liste, iki_boyutlu_liste, harfler_listesi):
    cikarma_hamlesi = hamle_giris_kontrol(koordinat_liste)
    while iki_boyutlu_liste[int(cikarma_hamlesi[0]) - 1][harfler_listesi.index(cikarma_hamlesi[1])] == "S" or \
            iki_boyutlu_liste[int(cikarma_hamlesi[0]) - 1][harfler_listesi.index(cikarma_hamlesi[1])] == " ":
        print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
        cikarma_hamlesi = hamle_giris_kontrol(koordinat_liste)
    return cikarma_hamlesi


# Beyaz oyuncunun girdiği koordinattaki siyah taşı çıkaran fonksiyon
def beyaz_oyuncu_icin_siyah_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi):
    iki_boyutlu_liste[int(cikarma_hamlesi[0])-1][harfler_listesi.index(cikarma_hamlesi[1])] = " "


# Siyah oyuncunun girdiği koordinattaki beyaz taşı çıkaran fonksiyon
def siyah_oyuncu_icin_beyaz_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi):  # siyah oyuncu beyaz taş çıkarıyor
    iki_boyutlu_liste[int(cikarma_hamlesi[0])-1][harfler_listesi.index(cikarma_hamlesi[1])] = " "


# Beyaz oyuncunun çıkarırken kare bozduğu taşı geri ekleyen fonksiyon
def siyah_tasi_geri_ekleme(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi):
    iki_boyutlu_liste[int(cikarma_hamlesi[0]) - 1][harfler_listesi.index(cikarma_hamlesi[1])] = "S"

# Siyah oyuncunun çıkarken kare bozduğu taşı geri ekleyen fonksiyon
def beyaz_tasi_geri_ekleme(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi):
    iki_boyutlu_liste[int(cikarma_hamlesi[0]) - 1][harfler_listesi.index(cikarma_hamlesi[1])] = "B"


# Beyaz oyuncunun girdiği hamlenin siyah kare bozup bozmadığını kontrol eden fonksiyon
def beyaz_oyuncunun_siyah_kare_bozmamasi_icin_kontrol(koordinat_liste, iki_boyutlu_liste, harfler_listesi, satir_sayisi, siyah_kare_sayisi):
    print(f"Beyaz oyuncunun çıkaracağı siyah taşın koordinatlarını giriniz:")
    cikarma_hamlesi = beyaz_oyuncu_icin_siyah_tas_cikarma_hamlesi_al_kontrol_et(koordinat_liste, iki_boyutlu_liste, harfler_listesi)  # beyaz oyuncu taş çıkaracak o yüzden siyah tas çıkarma hamlesi kontrolü kullaılmalı
    beyaz_oyuncu_icin_siyah_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
    son_beyaz_kare_sayisi, son_siyah_kare_sayisi = kare_sayma(satir_sayisi, iki_boyutlu_liste)
    while son_siyah_kare_sayisi != siyah_kare_sayisi:
        print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
        siyah_tasi_geri_ekleme(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
        cikarma_hamlesi = beyaz_oyuncu_icin_siyah_tas_cikarma_hamlesi_al_kontrol_et(koordinat_liste, iki_boyutlu_liste, harfler_listesi)  # siyah oyuncu taş çıkaracak o yüzden beyaz tas çıkarma hamlesi kontrolü kullaılmalı
        beyaz_oyuncu_icin_siyah_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
        son_beyaz_kare_sayisi, son_siyah_kare_sayisi = kare_sayma(satir_sayisi, iki_boyutlu_liste)
    oyun_alanini_goruntule(satir_sayisi, iki_boyutlu_liste, harfler_listesi)


# Siyah oyuncunun girdiği hamlenin beyaz kare bozup bozmadığını kontrol eden fonksiyon
def siyah_oyuncunun_beyaz_kare_bozmamasi_icin_kontrol(koordinat_liste, iki_boyutlu_liste, harfler_listesi, satir_sayisi, beyaz_kare_sayisi):
    print(f"Siyah oyuncunun çıkaracağı beyaz taşın koordinatlarını giriniz: ", end="")
    cikarma_hamlesi = siyah_oyuncu_icin_beyaz_tas_cikarma_hamlesi_al_kontrol_et(koordinat_liste, iki_boyutlu_liste, harfler_listesi)  # beyaz oyuncu taş çıkaracak o yüzden siyah tas çıkarma hamlesi kontrolü kullaılmalı
    siyah_oyuncu_icin_beyaz_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
    son_beyaz_kare_sayisi, son_siyah_kare_sayisi = kare_sayma(satir_sayisi, iki_boyutlu_liste)
    while son_beyaz_kare_sayisi != beyaz_kare_sayisi:
        print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
        beyaz_tasi_geri_ekleme(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
        cikarma_hamlesi = siyah_oyuncu_icin_beyaz_tas_cikarma_hamlesi_al_kontrol_et(koordinat_liste, iki_boyutlu_liste, harfler_listesi)  # siyah oyuncu taş çıkaracak o yüzden beyaz tas çıkarma hamlesi kontrolü kullaılmalı
        siyah_oyuncu_icin_beyaz_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
        son_beyaz_kare_sayisi, son_siyah_kare_sayisi = kare_sayma(satir_sayisi, iki_boyutlu_liste)
    oyun_alanini_goruntule(satir_sayisi, iki_boyutlu_liste, harfler_listesi)


def kare_bozma_kontrol(siyah_kare_sayisi, beyaz_kare_sayisi, koordinat_liste, iki_boyutlu_liste, harfler_listesi, satir_sayisi):
    for i in range(beyaz_kare_sayisi):
        print(f"Beyaz oyuncunun çıkaracağı {i + 1}. siyah taşın koordinatlarını giriniz:")
        cikarma_hamlesi = beyaz_oyuncu_icin_siyah_tas_cikarma_hamlesi_al_kontrol_et(koordinat_liste, iki_boyutlu_liste, harfler_listesi)  # beyaz oyuncu taş çıkaracak o yüzden siyah tas çıkarma hamlesi kontrolü kullaılmalı
        beyaz_oyuncu_icin_siyah_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
        son_beyaz_kare_sayisi, son_siyah_kare_sayisi = kare_sayma(satir_sayisi, iki_boyutlu_liste)
        while son_siyah_kare_sayisi != siyah_kare_sayisi:
            print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
            siyah_tasi_geri_ekleme(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
            cikarma_hamlesi = beyaz_oyuncu_icin_siyah_tas_cikarma_hamlesi_al_kontrol_et(koordinat_liste, iki_boyutlu_liste, harfler_listesi)  # siyah oyuncu taş çıkaracak o yüzden beyaz tas çıkarma hamlesi kontrolü kullaılmalı
            beyaz_oyuncu_icin_siyah_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
            son_beyaz_kare_sayisi, son_siyah_kare_sayisi = kare_sayma(satir_sayisi, iki_boyutlu_liste)
        oyun_alanini_goruntule(satir_sayisi, iki_boyutlu_liste, harfler_listesi)
    for i in range(siyah_kare_sayisi):
        print(f"Siyah oyuncunun çıkaracağı {i + 1}. beyaz taşın koordinatlarını giriniz:", end='')
        cikarma_hamlesi = siyah_oyuncu_icin_beyaz_tas_cikarma_hamlesi_al_kontrol_et(koordinat_liste, iki_boyutlu_liste, harfler_listesi)  # beyaz oyuncu taş çıkaracak o yüzden siyah tas çıkarma hamlesi kontrolü kullaılmalı
        siyah_oyuncu_icin_beyaz_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
        son_beyaz_kare_sayisi, son_siyah_kare_sayisi = kare_sayma(satir_sayisi, iki_boyutlu_liste)
        while son_beyaz_kare_sayisi != beyaz_kare_sayisi:
            print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
            beyaz_tasi_geri_ekleme(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
            cikarma_hamlesi = siyah_oyuncu_icin_beyaz_tas_cikarma_hamlesi_al_kontrol_et(iki_boyutlu_liste, koordinat_liste, harfler_listesi)  # siyah oyuncu taş çıkaracak o yüzden beyaz tas çıkarma hamlesi kontrolü kullaılmalı
            siyah_oyuncu_icin_beyaz_tas_cikarma(iki_boyutlu_liste, harfler_listesi, cikarma_hamlesi)
            son_beyaz_kare_sayisi, son_siyah_kare_sayisi = kare_sayma(satir_sayisi, iki_boyutlu_liste)
        oyun_alanini_goruntule(satir_sayisi, iki_boyutlu_liste, harfler_listesi)


def beyaz_oyuncu_icin_hareket_hamlesi_kontrol(koordinat_liste, harfler_listesi, iki_boyutlu_liste, satir_sayisi):
    while True:
        hareket_hamlesi = input("Hareket ettirmek istediğiniz taşın koordinatlarını giriniz [eski konum _ yeni konum örn: 3C 2C ]: ")
        eski_konum = hareket_hamlesi[0:2].upper()
        yeni_konum = hareket_hamlesi[3:5].upper()
        while eski_konum not in koordinat_liste or yeni_konum not in koordinat_liste or hareket_hamlesi[2] != " " or \
                (yeni_konum[0] != eski_konum[0] and yeni_konum[1] != eski_konum[1]) or eski_konum == yeni_konum or \
                iki_boyutlu_liste[int(eski_konum[0]) - 1][harfler_listesi.index(eski_konum[1])] == "S":
            print("Hatalı veri girişi! Tekrar deneyiniz: ", end=" ")
            hareket_hamlesi = input("Hareket ettirmek istediğiniz taşın koordinatlarını giriniz [eski konum _ yeni konum örn: 3C 2C ]: ")
            eski_konum = hareket_hamlesi[0:2].upper()
            yeni_konum = hareket_hamlesi[3:5].upper()
        if not konuma_gore_hata_kontrol(eski_konum, yeni_konum, harfler_listesi, iki_boyutlu_liste, satir_sayisi):
            continue
        return eski_konum, yeni_konum


def siyah_oyuncu_icin_hareket_hamlesi_kontrol(koordinat_liste, harfler_listesi, iki_boyutlu_liste, satir_sayisi):
    while True:
        hareket_hamlesi = input("Hareket ettirmek istediğiniz taşın koordinatlarını giriniz [eski konum _ yeni konum örn: 3C 2C ]: ")
        eski_konum = hareket_hamlesi[0:2].upper()
        yeni_konum = hareket_hamlesi[3:5].upper()
        while eski_konum not in koordinat_liste or yeni_konum not in koordinat_liste or hareket_hamlesi[2] != " " \
                or (yeni_konum[0] != eski_konum[0] and yeni_konum[1] != eski_konum[1]) or eski_konum == yeni_konum\
                or iki_boyutlu_liste[int(eski_konum[0]) - 1][harfler_listesi.index(eski_konum[1])] == "B":
            print("Hatalı veri girişi! Tekrar deneyiniz: ", end=" ")
            hareket_hamlesi = input("Hareket ettirmek istediğiniz taşın koordinatlarını giriniz [eski konum _ yeni konum örn: 3C 2C ]: ")
            eski_konum = hareket_hamlesi[0:2].upper()
            yeni_konum = hareket_hamlesi[3:5].upper()
        if not konuma_gore_hata_kontrol(eski_konum, yeni_konum, harfler_listesi, iki_boyutlu_liste, satir_sayisi):
            continue
        return eski_konum, yeni_konum


def konuma_gore_hata_kontrol(eski_konum, yeni_konum, harfler_listesi, iki_boyutlu_liste, satir_sayisi):
    if eski_konum[0] == yeni_konum[0]:  # eğer yatayda hareket etttirmeye çalışıyorsa:
        if harfler_listesi.index(eski_konum[1]) < harfler_listesi.index(yeni_konum[1]):  # eğer soldan sağa gitmeye çalışıyorsa
            for eleman in iki_boyutlu_liste[int(eski_konum[0]) - 1][harfler_listesi.index(eski_konum[1]) + 1:harfler_listesi.index(yeni_konum[1]) + 1]:
                if eleman != " ":
                    print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
                    return False
        else:
            for eleman in iki_boyutlu_liste[int(eski_konum[0]) - 1][harfler_listesi.index(eski_konum[1]) - 1:harfler_listesi.index(yeni_konum[1]) - 1: -1]:
                if eleman != " ":
                    print("Hatalı veri girişi! Tekrar deneyiniz: ", end="")
                    return False
    else:  # eğer dikeyde hareket ettirmeye çalışıyorsa:
        tek_boyutlu_liste = [v1 for sub_list in iki_boyutlu_liste for v1 in sub_list]
        if int(eski_konum[0]) < int(yeni_konum[0]):  # listede yukarıdan aşağıya doğru iniyor
            for eleman in tek_boyutlu_liste[(int(eski_konum[0]) - 1) * (satir_sayisi + 1) + harfler_listesi.index(eski_konum[1]) + (satir_sayisi + 1):(int(yeni_konum[0]) - 1) * (satir_sayisi + 1) + harfler_listesi.index(eski_konum[1]) + 1:satir_sayisi + 1]:
                if eleman != " ":
                    print("Hatalı veri girişi! Tekrar deneyiniz(yukarıdan aşağı hareket ettirme hatası): ", end="")
                    return False
        else:  # Aşağıdan yukarı hareket ettirmeye çalışıyorsa:
            for eleman in tek_boyutlu_liste[(int(eski_konum[0]) - 1) * (satir_sayisi + 1) + harfler_listesi.index(eski_konum[1]) - (satir_sayisi + 1):(int(yeni_konum[0]) - 1) * (satir_sayisi + 1) + harfler_listesi.index(eski_konum[1]) - 1:-(satir_sayisi + 1)]:
                if eleman != " ":
                    print("Hatalı veri girişi! Tekrar deneyiniz(aşağıdan yukarı hareket ettirme hatası): ", end="")
                    return False
    return True


def tas_sayma(iki_boyutlu_liste):
    beyaz_tas_sayisi = sum(x.count("B") for x in iki_boyutlu_liste)
    siyah_tas_sayisi = sum(x.count("S") for x in iki_boyutlu_liste)
    return beyaz_tas_sayisi, siyah_tas_sayisi


def beyaz_tasi_hareket_ettirme(iki_boyutlu_liste, harfler_listesi, satir_sayisi, koordinat_liste, siyah_kare_sayisi):
    print('Beyazın sırası')
    eski_konum, yeni_konum = beyaz_oyuncu_icin_hareket_hamlesi_kontrol(koordinat_liste, harfler_listesi, iki_boyutlu_liste, satir_sayisi)
    iki_boyutlu_liste[int(eski_konum[0]) - 1][harfler_listesi.index(eski_konum[1])] = " "
    iki_boyutlu_liste[int(yeni_konum[0]) - 1][harfler_listesi.index(yeni_konum[1])] = "B"
    oyun_alanini_goruntule(satir_sayisi, iki_boyutlu_liste, harfler_listesi)
    if yeni_kare_olusmus_mu(yeni_konum, iki_boyutlu_liste, harfler_listesi):
        beyaz_oyuncunun_siyah_kare_bozmamasi_icin_kontrol(koordinat_liste, iki_boyutlu_liste, harfler_listesi, satir_sayisi, siyah_kare_sayisi)


def siyah_tasi_hareket_ettirme(iki_boyutlu_liste, harfler_listesi, satir_sayisi, koordinat_liste, beyaz_kare_sayisi):
    print('Siyahın sırası')
    eski_konum, yeni_konum = siyah_oyuncu_icin_hareket_hamlesi_kontrol(koordinat_liste, harfler_listesi, iki_boyutlu_liste, satir_sayisi)
    iki_boyutlu_liste[int(eski_konum[0]) - 1][harfler_listesi.index(eski_konum[1])] = " "
    iki_boyutlu_liste[int(yeni_konum[0]) - 1][harfler_listesi.index(yeni_konum[1])] = "S"
    oyun_alanini_goruntule(satir_sayisi, iki_boyutlu_liste, harfler_listesi)
    if yeni_kare_olusmus_mu(yeni_konum, iki_boyutlu_liste, harfler_listesi):
        siyah_oyuncunun_beyaz_kare_bozmamasi_icin_kontrol(koordinat_liste, iki_boyutlu_liste, harfler_listesi, satir_sayisi, beyaz_kare_sayisi)


def main():
    harfler = ["A", "B", "C", "D", "E", "F", "G", "H"]
    satir_sutun = []
    print("Oyun için satır sayısını giriniz:" , end ='')
    satir_sayisi = (sayi_al_kontrol_et(3, 7))
    for i in range(satir_sayisi):
        sutun_listesi = [" "] * (satir_sayisi + 1)
        satir_sutun.append(sutun_listesi)

    # Satır sayısına göre koordinat listesi oluşturuluyor
    koordinat = []
    for i in range(satir_sayisi):
        for j in range(satir_sayisi + 1):
            koordinat.append(str(i + 1) + harfler[j])

    print("Boş oyun alanı aşağıdaki gibi görüntülenmektedir:")
    print("   - BOŞ OYUN ALANI - ")
    oyun_alanini_goruntule(satir_sayisi, satir_sutun, harfler)
    taslari_yerlestir(satir_sayisi, koordinat, satir_sutun, harfler)
    beyaz_kare_sayisi, siyah_kare_sayisi = kare_sayma(satir_sayisi, satir_sutun)
    kare_bozma_kontrol(siyah_kare_sayisi, beyaz_kare_sayisi, koordinat, satir_sutun, harfler, satir_sayisi)

    siyah_tas_sayisi, beyaz_tas_sayisi = tas_sayma(satir_sutun)
    while siyah_tas_sayisi > 3 and beyaz_tas_sayisi > 3:
        beyaz_tasi_hareket_ettirme(satir_sutun, harfler, satir_sayisi, koordinat, siyah_kare_sayisi)
        beyaz_kare_sayisi, siyah_kare_sayisi = kare_sayma(satir_sayisi, satir_sutun)
        beyaz_tas_sayisi, siyah_tas_sayisi = tas_sayma(satir_sutun)
        if siyah_tas_sayisi == 3 or beyaz_tas_sayisi == 3:
            break
        siyah_tasi_hareket_ettirme(satir_sutun, harfler, satir_sayisi, koordinat, beyaz_kare_sayisi)
        beyaz_kare_sayisi, siyah_kare_sayisi = kare_sayma(satir_sayisi, satir_sutun)
        beyaz_tas_sayisi, siyah_tas_sayisi = tas_sayma(satir_sutun)

    if beyaz_tas_sayisi == 3:
        print("TEBRİKLER ! SİYAH TAŞLARLA OYNAYAN OYUNCU KAZANDI !")
    else:
        print("TEBRİKLER ! BEYAZ TAŞLARLA OYNAYAN OYUNCU KAZANDI ! ")


main()
