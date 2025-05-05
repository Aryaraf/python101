import json
import os

while True:
    data = []
    # Membaca file json terlebih dahulu
    if os.path.exists("Biodata.json"):
        with open("Biodata.json", "r") as f:
            data = json.load(f)
    
    print("===============")
    print("Welcome Selamat")
    print("===============")
            
    nama = input("Masukkan Nama: ")
    umur = input("Masukkan Umur: ")
    alamat = input("Masukkan Alamat: ")
    
    data.append({"Nama": nama, "Umur": umur, "Alamat": alamat})
    # Menulis data ke file json
    with open("Biodata.json", "w") as f:
        json.dump(data, f, indent=4)
        
    # Menampilkan data pada file json 
    print("\n== Biodata ==")
    for i, item in enumerate(data, start=1):
        print(f"{i}. Nama: {item['Nama']}, Umur: {item['Umur']}, Alamat: {item['Alamat']}")
        
    again = input("\nApakah anda ingin mengulang? (Y/n): ")
    if again.lower() != "y":
        break