huruf = input("Masukkan kata : ")
jumlahVokal = 0

for i in huruf:
    if i.lower() in "aiueo":
        jumlahVokal = jumlahVokal + 1
print(jumlahVokal)
    
        

