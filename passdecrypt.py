pswd = input("Çözülecek Şifreyi Girin: ")

liste = [i for i in pswd if i.isalpha()]
print("".join(liste))