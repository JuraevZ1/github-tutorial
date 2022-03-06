import pickle
import json
flag = True
while flag:
    soz = input('ismingizni kiriting:')
    if soz == 'no':
        break
    with open('pi.txt','a') as fayl:
        json.dump(soz,fayl)