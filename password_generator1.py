import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("berapa banyak karakter yang diingankan untuk passwordnya:"))
                  
password = ""

for i in range(pass_length):
    password += random.choice(karakter)

print(password)

a = "1"
b = "2"
print(a)

a += b
print(a)