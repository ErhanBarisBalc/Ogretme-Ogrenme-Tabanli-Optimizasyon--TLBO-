#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:17:38 2022

@author: barisbalci
"""

import math
from random import random
import numpy as np

#İTERASYON SÜRECİ
for dongu in range(0,durma_kriteri):
    
#ÖĞRETMEN AŞAMASI
    for ogr in range(0,sn):
        
#Başlangıç çözüm matrisinde amaç fonksiyonnu minimum yapayn en,iyi çözüm(öğretmen) ve bu çözüme ait tasarım değişkenlerinin elde edilmesi

    deger=min(OPT[AF][:])
    sira=np.argmin(OPT[AF])
    
    X1geniyi= OPT[0][sira]
    X2geniyi = OPT[0][sira]

#OPT[0][:]: 1. tasarım değişkeni için başlangıç çözüm matrisindeki tüm aday çözümler
    TF=round(1+random())
    
    X1new=OPT[0][ogr]+random()*(X1geniyi-TF*
 (np.mean(OPT[0][:])))
    X2new=OPT[1][ogr]+random()*(X2geniyi-TF*
 (np.mean(OPT[1][:])))
.......

#ÖĞRENCİ AŞAMASI

for ogr in range(0,sn):

#Birbirinden farklı olacak şekilde gerekli çözümün (öğrencinin)
rassal seçimi

    a=math.ceil(random()*sn)
    b=math.ceil(random()*sn)
    
#Üretilen iki çözümün aynı olması durumunda while döngüsü ile farklılaşana kadar yeniden belirlenmesi sağlanmalıdır.

    while (a==b):
        a=math.ceil(random()*sn)
        b=math.ceil(random()*sn)
        
    a=a-1
    b=b-1 
    
#OPT[0][a]: 1. tasarım değşkeninin başlangıç çözüm matrisinden rassal olarak belirlenen a. vektörleri değeri
#OPT[1][b]: 2. tasarım değişkeninin başlangıç çözüm matrisinden rassaol olarak belirlenen b. vektörleri değeri
   if(OPT[AF][a]<OPT[AF][b]):
       X1new=OPT[0][ogr]+random()*OPT[0][a]-OPT[0][b]
       X1new=OPT[1][ogr]+random()*OPT[01[a]-OPT[1][b]
..........
  else:
      X1new=OPT[0][ogr]+random()*OPT[0][a]-OPT[0][a]
      X1new=OPT[1][ogr]+random()*OPT[01[a]-OPT[1][a]
                                     

    
deger=min(OPT[AF][:])
sira=np.argmin(OPT[AF])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    