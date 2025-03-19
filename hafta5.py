t1='17.1.2002'
tarih1=t1.split('.')
yıl1=int(tarih1[-1])
ay1=int(tarih1[-2])
gun1=int(tarih1[-3])

t2='3/8/2005'
tarih2=t2.split('/')
yıl2=int(tarih2[-1])
ay2=int(tarih2[-2])
gun2=int(tarih2[-3])

kategory=['saglik','dunya','teknoloji']
gazeteler=['sabah','hurriyet','milliyet']
for m in gazeteler:
  gaste='www.{}.com.tr'.format(m)
  for k in kategory:
    for i in range(yıl1,yıl2,1):
      for j in range(1,13):
        for gun in range(1,30):

          print('{}/{}/{}-{}-{}'.format(gaste,k,i,j,gun1))
