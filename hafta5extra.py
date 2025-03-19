isimler=['merve acar', 'yaren parlak', 'efe akar']
def harf_sayisi(isimler):
  for isim in isimler:
    parcala=isim.split(' ')
    for parca in parcala:
      print(parca, len(parca))
harf_sayisi(isimler)
