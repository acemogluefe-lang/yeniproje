import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input ("parola uzunluğunu giriniz"))
sifre = ""
for i in range (uzunluk):
    sifre += random.choice(karakterler)

print (sifre)
