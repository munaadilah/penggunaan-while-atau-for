print("Menentukan bilangan prima")

a = int(input("Masukkan bilangan prima : "))
n = True

for i in range(2,a):
    if(a % i == 0):
        a = int(input("bukan bilangan prima, masukkan bilangan lagi : "))
print(n)


