# coding=utf-8
"""
random modülü ile işlem yapıldığı için program 
istenilen çıktıyı vermezse birkaç kez daha deneyebilirsiniz,
her seferinde farklı çıktı verebilir
"""
import random 
paragraf=input("Lütfen Paragrafı Giriniz:")

kelimeler=paragraf.split()
yeni_harf=[]
for kelime in kelimeler:
    kelime_uzunlugu=len(kelime)
    kisaltilacak_harf_sayisi=(kelime_uzunlugu//2)+1    
    kisaltilan_harf=0
    unlu_harfler=["a","e","ı","i","u","ü","o","ö","A","E","I","İ","U","Ü","O","Ö"] 
    sans=random.randint(0,1) #sesli harflerin bazı kelimelerde olmamasını ayarlamak için 1/2lik şans ataması yapılıyor
    kisaltilacak_harf_yerleri=[]
    for sayi in range(kisaltilacak_harf_sayisi+1):
        kisaltilacak_harf_yerleri.append(random.randint(0,kelime_uzunlugu))
    kisaltilacak_harf_yerleri = list(set(kisaltilacak_harf_yerleri))
    deneme_sayisi=0
    while (len(kisaltilacak_harf_yerleri)==kisaltilacak_harf_sayisi) or deneme_sayisi==10 :
        kisaltilacak_harf_yerleri.append(random.randint(0,kelime_uzunlugu))
        kisaltilacak_harf_yerleri = list(set(kisaltilacak_harf_yerleri))
        if 0 in kisaltilacak_harf_yerleri:#ilk harfin kısaltılması önleniyor
            kisaltilacak_harf_yerleri.remove(0)
            deneme_sayisi=deneme_sayisi+1#sonsuz döngüyü önlemek önlemek için yapılmıştır
        elif kelime_uzunlugu-1 in kisaltilacak_harf_yerleri:#son harfin kısaltılması önleniyor
            kisaltilacak_harf_yerleri.remove(kelime_uzunlugu-1)
            deneme_sayisi=deneme_sayisi+1
            
        deneme_sayisi=deneme_sayisi+1
             
    harf_sirasi=0    
    for harf in kelime:
        if harf_sirasi in kisaltilacak_harf_yerleri and harf_sirasi!=0 and harf_sirasi!=kelime_uzunlugu-1 :
            if sans==1:#sesli harfler çıkarılıyor
                if not harf in unlu_harfler:
                    harf="." #harf yerine nokta konulması tercih edilmiştir,bu durum değiştirilebilir
            else :
                harf="."
            
        yeni_harf.append(harf)
        harf_sirasi=harf_sirasi+1
    
    yeni_harf.append(" ")#kelimeler arası boşluk bırakılıyor
    
    
    
    
file=open("kisaltilmisparagraf.txt","w",encoding="utf-8") #yeni paragraf dosyaya kaydediliyor
for harf in yeni_harf:
    file.write(harf)

file.close()
print("İşlemler Başarılı.")     

            
        
            
            
    
