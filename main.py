'''
1. Feladat
Hozz létre egy tuple-t! Írasd ki a képernyőre az egyik elemét! 
Próbáld meg módosítani az egyik elemét! 
Milyen hibaüzenetet eredményez ez?
'''
tyupl = 255,255,0

'''
>>> tyupl[1] = 6
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''