from tabulate import tabulate


listbarang=[['A11','Charger',50,70000,'Standar'],
            ['A12','Headset',70,10000,'Standar'],
            ['A13','Headset',50,100000,'Premium'],
            ['B11','Charger',50,99000,'Premium'],
            ['B13','Casing',50,100000,'Standar']]


def daftarbarang():
                    header=['No Item','Nama','Jumlah','Harga','Kualitas']
                    table=tabulate(listbarang, headers=header, tablefmt='grid')
                    print(table)

def filterbarang():
                
                    noitem=input('Masukan Nama Barang: ').upper()
                    for i in range(len(listbarang)):
                        if noitem == listbarang[i][0]:
                            print(f'Kualitas produk tersebut adalah {listbarang[i][4]}')
                            break
                    else:
                        print('No Item tidak terdaftar')
                         


def tambahbarang():
                    noitem = input('Masukkan No Item yang mau ditambah: ').upper()
                    nama = input('Masukkan Nama Barang: ').capitalize()
                    jumlah = int(input('Masukkan Jumlah Barang: '))
                    harga = int(input('Masukkan Harga Barang: '))
                    kualitas = input('Masukkan Kualitas Barang: ').capitalize()
                    listbarang.append([noitem,nama,jumlah,harga,kualitas])
    

def hapusbarang():
                    dihapus=input('Masukkan No Item barang yang mau dihapus: ').upper()
                    for i in range(len(listbarang)):
                        if dihapus == listbarang[i][0]:
                            del listbarang[i]
                            break

def updatebarang():
    while True:
            
            update = input('Masukan no item yang mau diupdate: ').upper()
            for i in range(len(listbarang)):   
                if update == listbarang[i][0]:
                        indeks=i                        
            
            print(''' Daftar Kolom
            1.No. item
            2.Nama
            3.Jumlah
            4.Harga
            5.Kualitas
            6.Kembali''')                    
                                        
        
                        
            menuupdate= int(input('Yang mau diupdate: '))
            if menuupdate==1:
                    noitembaru = input('Masukan no item baru: ').upper()
                    listbarang[indeks][0] = noitembaru
                    daftarbarang()
                    
            elif menuupdate== 2:
                    namabaru = input('Masukan nama baru: ').capitalize()
                    listbarang[indeks][1] = namabaru
                    daftarbarang()
                    
            elif menuupdate== 3:
                    jumlahbaru = int(input('Masukan jumlah baru: '))
                    listbarang[indeks][2] = jumlahbaru
                    daftarbarang()
                    
            elif menuupdate== 4:
                    hargabaru = int(input('Masukan harga baru: '))
                    listbarang[indeks][3] = hargabaru
                    daftarbarang()
                    
            elif menuupdate== 5:
                    kualitasbaru = input('Masukan kualitas baru: ').capitalize()
                    listbarang[indeks][4] = kualitasbaru
                    daftarbarang()
            
            elif menuupdate == 6:
                    break
                        
                                                
def belibarang():
            cart=[]


            while True:
                            
                noitem = input('Masukkan No Item yang mau dibeli: ').upper()
                for i in range(len(listbarang)):
                    if noitem == listbarang[i][0]:
                        print('No item terdaftar!')
                        break
                else:
                    print('No Item tidak terdaftar')
                    continue
                

                jumlahbarang = int(input('Masukkan jumlah barang: '))
                if jumlahbarang > listbarang[i][2]:
                    print(f'Maaf stock tidak tersedia, untuk barang {listbarang[i][1]}, ada {listbarang[i][2]} ')
                    continue
                else:
                    listbarang[i][2] -= jumlahbarang
                    cart.append([noitem,listbarang[i][1],jumlahbarang,listbarang[i][3]])
                        
                        
                print('CART')
                print('No Item\t|Nama\t|Jumlah\t|Harga\t|Total')
                for i in cart:
                    print(f'{i[0]}\t{i[1]}\t|{i[2]}\t{i[3]}\t|{i[2]*i[3]}')


                belanjalagi = input('Belanja lagi y/t: ').upper()
                if belanjalagi == 'T' :
                    break 
                elif belanjalagi == 'Y' :
                    continue

            totalbelanja = 0
            print(f'CART')
            print('No Item\t|Nama\t|Jumlah\t|Harga\tTotal')
            for i in cart:
                print(f'{i[0]}\t{i[1]}\t|{i[2]}\t{i[3]}\t|{i[2]*i[3]}')
                totalbelanja += i[2]*i[3]


            while True:
                print(f'Total belanja anda adalah {totalbelanja}')
                uang = int(input('Masukkan uang anda: '))
                kembalian = uang - totalbelanja
                kurang = totalbelanja - uang
                if uang > totalbelanja:
                    print (f'Berikut kembalian anda {kembalian},Terima kasih sudah berbelanja ')
                    break
                elif uang == totalbelanja:
                    print(f'Pembayaran diterima!Terima kasih sudah berbelanja')
                    break
                elif uang < totalbelanja:
                    print(f'Maaf uang anda kurang {kurang}, silahkan masukkan masukkan uang yang sesuai')
                    continue


while True:
        try:
            
            print('''Selamat datang di TOKO ELEKTRONIK HARAPAN
                Daftar Menu:
                1. Lihat Daftar barang
                2. Filter Barang 
                3. Menambah Barang
                4. Menghapus Barang
                5. Mengupdate 
                6. Membeli Barang
                7. Exit''' )
        

            pilihanmenu = int(input('Masukkan pilihan angka menu: '))

            if pilihanmenu == 1:
                                daftarbarang()
            
            elif pilihanmenu == 2:
                                 daftarbarang()
                                 filterbarang()
                                 daftarbarang()

            elif pilihanmenu == 3:
                                daftarbarang()
                                tambahbarang()
                                daftarbarang()

            elif pilihanmenu == 4:
                                daftarbarang()
                                hapusbarang()
                                daftarbarang()

            elif pilihanmenu == 5:
                                daftarbarang()
                                updatebarang()
                                daftarbarang()
                                

            elif pilihanmenu == 6:
                                daftarbarang()
                                belibarang()
                                daftarbarang()

            elif pilihanmenu== 7:
                    break   
        except:
            print('Masukkan angka yang ada pada daftar menu')  

                




            


                        


                     
                            

