import time,random,sys

class oyuncu:
    def __init__(self,isim,can=5,enerji=100):
        self.isim=isim
        self.can=can
        self.darbe=0
        self.enerji =enerji
    def mevcut_durumu_görüntüle(self):
        print('darbe ;' ,self.darbe)
        print('can:',self.can)
        print('enerji :',self.enerji)

    def saldır(self,rakip):
        print("Bir saldırı gerçekleştirdiniz \n Saldırı sürüyor . Bekleyiniz")
        
        for i in range(10):
            time.sleep(.3)
            print('',end='',flush=True)
        sonuç= self.saldırı_sonucunu_hesapla()
        
        if sonuç == 0:
            print("berabere")
        if sonuç== 1:
            print("darbe vuruldu")
            self.darbele(rakip)

        if sonuç== 2:
            print("darbe aldınız")
            self.darbele(self)
    def saldırı_sonucunu_hesapla(self):
        return random.randint(0,2)
    
    def kaç(self):
        print("kaçılıyor...")
        for i in range(10):
            time.sleep(.3)
            print('\n',flush=True)
        print("rakibiniz sizi yakaladı")

    def darbele(self,darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -1
        if (darbelenen.darbe %5) == 0:
            darbelenen.can -=1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print("oyunuu{self.isim} kazandı!!!")
            self.oyundan_çık()
    def oyundan_çık(self):
        print("çıkılıyor...")
        sys.exit()

####################################
siz = oyuncu("burak")
rakip = oyuncu("rakip")
while True:
   print("rakip karşında \n saldırı : s\n kaç : k\n çık : q")
   hamle = input("\n>")
   if hamle == "s":
       siz.saldır(rakip)
       print("rakip durumu : ")
       rakip.mevcut_durumu_görüntüle()
       print("\n kendi durumum : ")
       siz.mevcut_durumu_görüntüle()
   elif hamle == "k":
       siz.kaç()
   elif hamle == "q":
       siz.oyundan_çık()