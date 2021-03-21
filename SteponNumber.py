'''
Soal:
Membuat function steponNumber() yang memprediksi nilai deret selanjutnya,
dengan memberi input koordinat (x,y)
'''

# Saya melihat grafik ini sebagai 2 garis dalam 1 grafik.
# Yaitu garis y = x, dan garis y = x - 2
# Sebenarnya saya mau menggunakan NumPy untuk membantu membuat array y = f(x), 
# tapi karena belum dipelajari bersama, saya coba usahakan menggunakan list.

def steponNumber(list_awal):
    # Pertama, saya akan membuat list berisi nilai (x,y) dari kedua fungsi garis tersebut.

    # 1. Untuk Garis 1 (y = x):
    x1 = list(range(0,101)) # Saya membuat list x hingga 101, sehingga pola dapat dicari hingga 100.
    y1 = list((i) for i in x1) # List y adalah nilai dari x itu sendiri, karena y = x
    garis1 = list(zip(x1,y1)) # Saya menyimpan kedua list tersebut ke dalam 1 list yang saya zip()
    garis1 = list(map(list,garis1)) # Karena zipped-list bertipe tuple, saya lakukan mapping untuk mengubahnya menjadi list

    # 2. Untuk Garis 2 (y = x - 2):
    x2 = list(range(0,103)) # Saya men-define hingga 103, supaya tetap bisa diakses hingga index 100
    y2 = list((i - 2) for i in x2) # Sama dengan garis1 sebelumnya, tapi setiap nilai dari x2 akan dikurangi 2
    garis2 = list(zip(x2,y2))
    garis2 = list(map(list,garis2))

    # Selanjutnya, saya akan membuat 2 list berisi deret pada y = x dan y = x - 2

    # 1. Deret 1
    deret1 = list() # Disiapkan list kosong
    # Berikut adalah 2 angka pertama, yaitu 0 dan 1
    x = 0 
    y = 1

    # Looping untuk membentuk Deret 1:
    for i in range(51): # Saya looping hingga 51, supaya bisa diakses pada index 100
        deret1.append(x) # Ketika  iterasi pertama, akan memasukkan x = 0
        x += 4 # Kemudian nilai x tersebut ditambah 4
        for j in range(1): 
            # Sebelum ditambah x, dilakukan loop 1 kali lagi untuk memasukkan nilai y
            deret1.append(y)
            y += 4 # Nilai y ditambah 4
        #Berulang kali sehingga setelah ditambah y, akan ditambah x, ditambah y, ditambah x, dst...
    # Maka didapatkanlah deret1 = [0, 1, 4, 5, 8, 9, 12, 13, 16, 17, 20, 21,...]

    # Selanjutnya looping untuk membentuk Deret 2:
    # Prosesnya sama dengan Deret 1, hanya saja diinisialisasi oleh 2 dan 3
    deret2 = list()
    x = 2
    y = 3
    for i in range(51):
        deret2.append(x)
        x += 4
        for j in range(1):
            deret2.append(y)
            y += 4
    # Maka didapatkanlah deret2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23,...]

    # Pada titik ini, sudah dibuat:
    # garis1, garis2, deret1, dan deret2
    # Selanjutnya, dibuatlah conditional statements untuk mengambil setiap nilai deret

    # Pertama, dibuatlah list kosong
    output = list()
    for i in list_awal: # Dilakukan looping pada list_awal tersebut yang sebagai input
        if i in garis1:
            # Jika input sebelumnya terdapat dalam deret1, makan list output akan di-append oleh nilai pada deret1
            output.append(deret1[i[1]]) 

        elif i in garis2:
            # Sebaliknya, akan di-append oleh nilai pada deret2
            output.append(deret2[i[1]])

        else:
            # Jika input tidak terdapat dalam deret1 maupun deret2, maka append 'No Number'
            output.append('No Number')

    # Function steponNumber ini akan mengembalikan list output tersebut,
    # yang berisi nilai pada setiap deret
    return output

# TESTING:
print(steponNumber([[4,2],[6,6],[3,4]]))
print(steponNumber([[4,2],[6,6],[3,4],[7,5],[6,6],[1,1],[3,1],[5,8]]))
print(steponNumber([[98,98],[95,95],[102,100],[99,97]]))





    