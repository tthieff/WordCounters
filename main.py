s = input("Metni Girin : ")
sayı="123456789"
karakter =">£#$½{[]}\|_?=)(/&%+%^'!é<'"
sesli_harf = 'AEIİOÖUÜaeıioöuü'
sessiz_harf= "bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ"
sesli_sayac = 0
sessiz_sayac=0
sayı_sayac=0
karakter_sayac=0
for i in s:
    if i in sesli_harf:
        sesli_sayac += 1
    elif i in sessiz_harf:
        sessiz_sayac +=1
    elif i in sayı:
        sayı_sayac+=1
    elif i in karakter:
        karakter_sayac+=1

print("%s metnindeki sesli harf sayisi:%d" % (s, sayı_sayac))
print("%s metnindeki sessiz harf sayisi:%d" % (s, sessiz_sayac))
print("%s metnindeki sayı  miktarı :%d" % (s,sayı_sayac))
print("%s metnindeki özel karakter sayisi:%d" % (s, karakter_sayac))