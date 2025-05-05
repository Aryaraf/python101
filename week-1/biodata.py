while True:
    print("=========================")
    print("Selamat Datang di Program")
    print("=========================")
    
    nama = input("Nama: ")
    umur = input("Umur: ")
    
    teks = "\nNama: {}\nUmur: {}".format(nama, umur)
    
    with open("biodata.txt", "a") as file_bio:
        file_bio.write(teks) 
    
    lagi = input("Apakah kamu ingin isi lagi? (Y/n): ")
    if lagi.lower() != "y":
        break
    
print("\n==Daftar Biodata==")
try:
    with open("biodata.txt", "r") as file_bio:
        isi = file_bio.read()
        if isi.strip() == "":
            print("Biodata masih kosong.")
        else:
            print(isi)
except FileNotFoundError:
    print("Belum ada file biodata")
    