#Algoritma struktur data pertemuan 1 - praktikum 1 : KONSEP ADT DAN FILE HANDLING
#=================================================================
#Latihan Dasar 1 : membaca seluruh isi file
#=================================================================
#Membukafile dengan mode 'r' (read)
with open("data_mahasiswa.txt", 'r') as file:
    #Membaca isi file
    isi_file = file.read() #Membaca seluruh isi file dalam satu string
    #Menampilkan isi file
    print(isi_file)
print("===hasil read===")
print("Tipe Data:", type(isi_file))
print("jumlah karakter:", len(isi_file))
print("jumlah baris:", isi_file.count('\n')+1)

#Membukafile per baris
print("===membaca file per baris===")
jumlah_baris=0 #Inisialisasi penghitung baris
with open("data_mahasiswa.txt", 'r') as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #Menghilangkan karakter newline dan spasi di awal/akhir (\n)
        print("Baris ke-", jumlah_baris)
        print("isinya:", baris)
#=================================================================

#=================================================================
#Latihan Dasar 2 : Parsing baris menjadi kolom data
#=================================================================
with open("data_mahasiswa.txt", 'r') as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter newline dan spasi di awal/akhir (\n)
        kolom = baris.split(',') #Memisahkan kolom berdasarkan tanda koma
        nim, nama, nilai = baris.split(',') #parsing data berdasarkan karakter , 
        print("NIM:", nim, "Nama:", nama, "Nilai:",int(nilai))
#=================================================================

#=================================================================
#Latihan Dasar 3 : Membaca file  dan menyimpan ke list
#=================================================================

data_list = [] #Inisialisasi list kosong

with open("data_mahasiswa.txt", 'r') as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter newline dan spasi di awal/akhir (\n)
        #simpan sebagai list "[NIM, Nama, Nilai]"
        nim, nama, nilai = baris.split(',') #parsing data berdasarkan karakter ,    
        data_list.append([nim, nama, int(nilai)])
print("===Data mahasiswa dalam list===")
print(data_list)
print("===Jumlah record dalam list===")
print("jumlah record", len(data_list))
print("===menampilkan data record tertentu===")
print("contoh record pertama: ", data_list[0]) #array dimulai dari 0
#=================================================================

#=================================================================
#Latihan Dasar 4 : Membaca file  dan menyimpan ke dictionary
#=================================================================

data_dict = {} #Inisialisasi dictionary kosong

with open("data_mahasiswa.txt", 'r') as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter newline dan spasi di awal/akhir (\n)
        nim, nama, nilai = baris.split(',') #parsing data berdasarkan karakter , 
        #simpan sebagai dictionary  dengan key NIM {NIM: [Nama, Nilai]}
        data_dict[nim] = {  #key
            "nama": nama,   #values
            "nilai": int(nilai) #values
            }
print("===Data mahasiswa dalam dictionary===")
print(data_dict)
#=================================================================