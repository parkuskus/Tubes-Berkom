''' 
Author              : Kelompok 9
Tanggal Pengerjaan  : 3-10 November 2024

PROGRAM ATM BANK TPB SUKSES 
Deskripsi           : Simulasi ATM (Anjungan Tunai Mandiri / Automatic Teller Machine) bahasa Indonesia dan Inggris dengan fitur-fitur berupa
                      cek saldo, penarikan tunai, transfer antarbank, pembayaran/pembelian, dan ganti pin.

KAMUS
nama_lengkap                    = menyimpan nama lengkap pengguna
tanggal_lahir                   = menyimpan tanggal lahir pengguna
status_pin                      = menyimpan status pin yang telah dimasukkan apakh benar atau tidak
pin                             = menyimpan pin dari pengguna
pin_konfirmasi                  = menyimpan pin pengguna saat mengonfirmasi pin yang telah dibuat
saldo                           = menyimpan saldo pengguna
bahasa                          = menyimpan pilihan bahasa yang dipilih pengguna
counter                         = menyimpan percobaan yang tersisa ketika pengguna salah memasukkan PIN
status_pin_masuk                = menyimpan status pin yang dimasukkan ketika pengguna akan masuk ke ATM
nama_lengkap_konfirmasi         = menyimpan nama lengkap pengguna ketika proses recovery akun
tanggal_lahir konfirmasi        = menyimpan tanggal lahir pengguna ketika recovery akun
pilihan                         = menyimpan pilihan fitur ATM yang dipilih oleh pengguna
lanjut                          = menyimpan pilihan apakah pengguna ingin melanjutkan transaksi atau tidak
tarik                           = menyimpan pilihan jumlah uang yang ingin ditarik oleh pengguna
receipt                         = menyimpan pilihan apakah pengguna ingin mencetak struk atau tidak
status_tarik                    = menyimpan status penarikan pengguna ketika memilih pilihan "5. JUMLAH LAIN" di menu penarikan tunai
cek_kode_bank                   = menyimpan pilihan pengguna apakah ingin cek kode bank atau tidak
kumpulan_bank                   = array yang menyimpan bank-bank yang tersedia
status_transfer                 = menyimpan status transfer dari pengguna
rekening_tujuan                 = menyimpan rekening tujuan 
kode_bank                       = menyimpan kode bank dari rekening tujuan
nama_penerima                   = menyimpan nama penerima dari transfer
nominal_transfer                = menyimpan nomimal yang akan ditransfer kepada rekening penerima
status_transfer                 = menyimpan pilihan pengguna apakah ingin melakukan transfer atau tidak
pilih_pembayaran                = menyimpan pilihan menu pembayaran yang ingin digunakan oleh pengguna
nomor_hp                        = menyimpan nomor telepon genggam dari pengguna
daftar_pembelian                = menyimpan nomor nomimal voucher pulsa yang dapat dipilih oleh pengguna
nominal_isi_ulang               = menyimpan nominal isi ualng yang dipilih oleh pengguna
admin_bank                      = menyimpan nomimal admin bank 
total_isi_ulang                 = menyimpan isi total biaya isi ulang pulsa yang harus dibayar pengguna
proses_transaksi                = menyimpan konfirmasi permintaan pengguna untuk membeli pulsa prabayar
nomor_meter                     = menyimpan nomor meteran listrik pengguna
id_pelanggan                    = menyimpan nomor id listrik pelanggan/pengguna
waktu                           = menyimpan waktu ketika pengguna melakukan transaksi 
status_kode                     = menyimpan pilihan pengguna apakah ingin melihat kode PAM atau tidak
nomor_pelanggan                 = menyimpan nomor PAM/Air pelanggan
tagihan                         = menyimpan tagihan yang dimiliki oleh pengguna
total_bayar                     = menyimpan total tagihan PAM yang dimiliki oleh pengguna
konfirmasi_pembayaran           = menyimpan pilihan pengguna apakah ingin melakukan pembayaran PAM atau tidak

'''
import os
import time
import random
import sys
from datetime import datetime


#Fungsi Typing Effect di Terminal
def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after typing is done

#Menyambut pengguna
print('==================================')
print('SELAMAT DATANG DI BANK TPB SUKSES')
print('==================================')
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

# Membuat akun 
print('Silahkan masukkan data-data di bawah ini!')
nama_lengkap    = str(input('Nama Lengkap: '))
tanggal_lahir   = str(input('Tanggal Lahir (DD/MM/YYYY): '))

#Membuat PIN 
status_pin = False 
while (status_pin == False) :
    pin = str(input('Silahkan buat PIN anda: '))
    pin_konfirmasi = str(input(('Masukkan kembali PIN yang telah anda buat: '))) #Konfimasi PIN yang telah dibuat
    if (pin == pin_konfirmasi) :
        status_pin = True
    else : #Alert jika PIN yang dikonfirmasi berbeda dengan PIN yang dibuat
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('PIN yang anda masukkan belum sama. Silahkan masukkan kembali PIN anda')

#Mengisi saldo awal
os.system('cls' if os.name == 'nt' else 'clear')
saldo = int(input('Masukkan jumlah saldo awal (minimum 50.000): '))
while (saldo<50000) :
    print('Mohon maaf, saldo awal yang anda masukkan belum mencukupi batas minimal')
    saldo = int(input('Masukkan kembali saldo awal (minimum 50.000): '))

# Menampilkan kembali data-data yang sudah dimasukkan
os.system('cls' if os.name == 'nt' else 'clear')
typing_effect('Berikut adalah data-data pribadi anda!')
typing_effect(f'Nama Lengkap    : {nama_lengkap}')
typing_effect(f'Tanggal Lahir   : {tanggal_lahir}')
typing_effect(f'PIN             : {pin}')
typing_effect(f'Saldo Awal      : Rp{saldo:,}'.replace(',', '.'))
time.sleep(4)

# TAHAP ATM
# Memasukkan Kartu
os.system('cls' if os.name == 'nt' else 'clear')
print("Silakan masukkan kartu Anda untuk memulai.")
input("Tekan Enter untuk memasukkan kartu...")

card = [
            "|=============|",
            "|             |",
            "|             |",
            "|    KARTU    |",
            "|     ATM     |",
            "|             |",
            "|             |",
            "|=============|"
        ]

# Cetak kartu 
for i in range(len(card), 0, -1):
    os.system('cls' if os.name == 'nt' else 'clear')  
    for line in card[-i:]:
        print(line)
    time.sleep(0.2)
    
os.system('cls' if os.name == 'nt' else 'clear')  
print("Kartu berhasil dimasukkan!")
time.sleep(2)

#Memilih Bahasa pada ATM
os.system('cls' if os.name == 'nt' else 'clear')
print('PILIH BAHASA YANG ANDA INGIN GUNAKAN!')
print('1. Indonesia')
print('2. Inggris')
bahasa = int(input(('Pilih bahasa yang anda ingin gunakan!: ')))

# ATM Bahasa Indonesia
if (bahasa == 1) :
    # Memasukkan dan Mengecek PIN yang dimasukkan
    os.system('cls' if os.name == 'nt' else 'clear')
    counter = 2
    status_pin_masuk = False
    while (counter>= 0) and (status_pin_masuk == False) :
        pin_masuk = str(input('Masukkan PIN anda: ')) 
        if (pin_masuk == pin) and (counter>0) : 
            status_pin_masuk = True
            print('Anda berhasil masuk')
        elif (counter == 0) : # Mengunci akun dan melakukan recovery akun
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('Akun anda telah dikunci. Silahkan atur ulang PIN anda.')
            print('Silakan konfirmasi kembali data pribadi anda.')
            nama_lengkap_konfirmasi = str(input('Nama Lengkap: '))
            tanggal_lahir_konfirmasi = str(input('Tanggal Lahir: '))
            # Mengatur ulang PIN dengan memasukkan data-data pribadi (nama, tanggal lahir)
            if (nama_lengkap == nama_lengkap_konfirmasi) and (tanggal_lahir == tanggal_lahir_konfirmasi) :
                status_pin = False 
                while (status_pin == False) :
                    pin = str(input('Masukkan PIN baru anda: '))
                    pin_konfirmasi = str(input('Konfirmasikan kembali PIN anda: '))
                    if (pin == pin_konfirmasi) :
                        status_pin = True
                        print('PIN berhasil diubah!')
                        counter = 3
                    else :
                        print('PIN tidak sesuai!')

            else :# Menanyakan ulang data-data pribadi jika sebelumnya data yang diberikan di awal salah
                while (nama_lengkap_konfirmasi != nama_lengkap) and (tanggal_lahir_konfirmasi != tanggal_lahir) :
                    print('Akun anda telah dikunci. Silahkan atur ulang PIN anda.')
                    print('Silakan konfirmasi kembali data pribadi anda.')
                    nama_lengkap_konfirmasi = str(input('Nama Lengkap: '))
                    tanggal_lahir_konfirmasi = str(input('Tanggal Lahir: '))
                if (nama_lengkap == nama_lengkap_konfirmasi) and (tanggal_lahir == tanggal_lahir_konfirmasi) :
                    status_pin = False 
                    while (status_pin == False) :
                        os.system('cls' if os.name == 'nt' else 'clear') 
                        pin = str(input('Masukkan PIN baru anda: '))
                        pin_konfirmasi = str(input('Konfirmasikan kembali PIN anda: '))
                        if (pin == pin_konfirmasi) :
                            status_pin = True
                            print('PIN berhasil diubah!')
                            counter = 3

                            os.system('cls' if os.name == 'nt' else 'clear') 
                        else :
                            print('PIN tidak sesuai!')
                            os.system('cls' if os.name == 'nt' else 'clear') 
        else : # Alert ketika user salah memasukkkan PIN
            counter -= 1
            print(f'PIN yang dimasukkan salah. Silakan coba lagi. Anda memiliki {counter+1} kesempatan lagi')
                        
    # Menampilkan menu yang bisa dipilih
    os.system('cls' if os.name == 'nt' else 'clear')     
    print('SILAHKAN PILIH MENU TRANSAKSI YANG ANDA INGINKAN')
    print('1. Informasi Saldo')
    print('2. Penarikan Tunai')
    print('3. Transfer')
    print('4. Pembayaran')
    print('5. Ganti PIN')
    print('6. Selesai Transaksi')
    
    pilihan = int(input('Masukkan menu yang anda inginkan: '))
    os.system('cls' if os.name == 'nt' else 'clear')     

    # Masuk ke menu-menu yang disediakan 
    while ((pilihan == 0) or (pilihan == 1) or (pilihan == 2) or (pilihan == 3) or (pilihan == 4) or (pilihan == 5)):
        if (pilihan == 0) :
            os.system('cls' if os.name == 'nt' else 'clear')   
            print('SILAHKAN PILIH MENU TRANSAKSI YANG ANDA INGINKAN!')
            print('1. Informasi Saldo')
            print('2. Penarikan Tunai')
            print('3. Transfer')
            print('4. Pembayaran')
            print('5. Ganti PIN')
            print('6. Selesai Transaksi')
            
            pilihan = int(input('Masukkan menu yang anda inginkan: '))
            os.system('cls' if os.name == 'nt' else 'clear')  
        
        # Menu informasi saldo       
        elif (pilihan == 1) :
            print('HARAP MENUNGGU')
            print('TRANSAKSI ANDA SEDANG DIPROSES')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')   

            # Menampilkan saldo rekening         
            print('SALDO REKENING ANDA')
            print(f'RP.{saldo:,}'.replace(',', '.'))
            print('')
            
            # Konfirmasi lanjut transaksi/tidak?
            print('Lanjut Transaksi?')
            print('1. Ya')
            print('2. Tidak')
            lanjut = int(input())
            if lanjut == 1:
                pilihan = 0
            else:
                pilihan = 10
            os.system('cls' if os.name == 'nt' else 'clear')   

        # Menu penarikan tunai 
        elif (pilihan == 2) :
            print('MENU PENARIKAN CEPAT')
            print('SILAKAN PILIH JUMLAH PENARIKAN')
            print('1. Rp    50.000')
            print('2. Rp   200.000')
            print('3. Rp   500.000')
            print('4. Rp 1.000.000')
            print('5. JUMLAH LAIN')
            tarik = int(input())
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Penarikan Tunai Cepat
            receipt = 0
            
            # Mengambil Rp50.000
            if tarik == 1:
                print('HARAP MENUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')       
                if saldo >= 50000:
                    saldo -= 50000
                    tunai = 50000
                    print('Anda telah berhasil menarik Rp50.000')
                    print(f'Sisa saldo di rekening anda adalah Rp{saldo:,}'.replace(',', '.'))
                    print('Apakah anda ingin mencetak receipt?')
                    print('1. Ya')
                    print('2. Tidak')
                    receipt = int(input())
                else:
                    print('SALDO TIDAK MENCUKUPI')
                    print('')     

            # Mengambil Rp200.000       
            elif tarik == 2:
                print('HARAP MENUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   
                if saldo >= 200000:
                    saldo -= 200000
                    tunai = 200000
                    print('Anda telah berhasil menarik Rp200.000')
                    print(f'Sisa saldo di rekening anda adalah Rp{saldo:,}'.replace(',', '.'))
                    print('Apakah anda ingin mencetak receipt?')
                    print('1. Ya')
                    print('2. Tidak')
                    receipt = int(input())
                else:
                    print('SALDO TIDAK MENCUKUPI')
                    print('')     

            # Mengambil Rp500.000          
            elif tarik == 3:
                print('HARAP MENUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   
                if saldo >= 500000:
                    saldo -= 500000
                    tunai = 500000
                    print('Anda telah berhasil menarik Rp500.000')
                    print(f'Sisa saldo di rekening anda adalah Rp{saldo:,}'.replace(',', '.'))
                    print('Apakah anda ingin mencetak receipt?')
                    print('1. Ya')
                    print('2. Tidak')
                    receipt = int(input())
                else:
                    print('SALDO TIDAK MENCUKUPI')
                    print('')    

            # Mengambil Rp1.000.000           
            elif tarik == 4:
                print('HARAP MENUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   
                if saldo >= 1000000:
                    saldo -= 1000000
                    tunai = 1000000
                    print('Anda telah berhasil menarik Rp1.000.000')
                    print(f'Sisa saldo di rekening anda adalah Rp{saldo:,}'.replace(',', '.'))
                    print('Apakah anda ingin mencetak receipt?')
                    print('1. Ya')
                    print('2. Tidak')
                    receipt = int(input())
                else:
                    print('SALDO TIDAK MENCUKUPI')
                    print('')    
            # Mengambil selain pilihan sebelumnya (harus kelipatan 50.000, maks Rp1.250.000)         
            elif tarik == 5:
                status_tarik = False
                while status_tarik == False:   
                    print('MASUKKAN JUMLAH PENARIKAN TUNAI YANG ANDA INGINKAN')
                    print('(DALAM KELIPATAN RP50.000)')
                    print('MAKSIMAL RP1.250.000')
                    tunai = int(input('JUMLAH PENARIKAN: '))
                    if tunai < 50000:
                        print('NOMINAL YANG DIINPUT TIDAK MENCUKUPI')
                        print('')
                    elif tunai > 1250000:
                        print('NOMINAL YANG DIINPUT TERLALU BESAR')
                        print('')
                    elif tunai % 50000 != 0:
                        print('NOMINAL TIDAK VALID')
                        print('')
                    elif saldo < tunai:
                        print('SALDO TIDAK MENCUKUPI')
                        print('')
                    else: 
                        print(f'NOMINAL YANG ANDA INPUT ADALAH Rp{tunai:,}'.replace(',', '.'))
                        print('APAKAH ANDA YAKIN?')
                        konfirmasi_tarik = input('Konfirmasi (y/n): ')
                        if konfirmasi_tarik == 'y':
                            status_tarik = True
                
                # Mencetak sisa saldo setelah tarik tunai
                if status_tarik == True:
                    os.system('cls' if os.name == 'nt' else 'clear')  
                    print('HARAP MENUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')   
                    saldo -= tunai  
                    print(f'Anda telah berhasil menarik Rp {tunai:,}'.replace(',', '.'))
                    print(f'Sisa saldo di rekening anda adalah Rp {saldo:,}'.replace(',', '.'))
                    print('')
                    print('Apakah anda ingin mencetak receipt?')
                    print('1. Ya')
                    print('2. Tidak')
                    receipt = int(input())
                    os.system('cls' if os.name == 'nt' else 'clear')  

            # Mencetak receipt
            if receipt == 1:
                waktu = datetime.now().isoformat(' ', 'seconds')
                print('---------------------------------------------------')
                print('TARIK TUNAI')
                print(f'JUMLAH            : Rp{tunai:,}'.replace(',', '.'))
                print(f'SISA SALDO        : Rp{saldo:,}'.replace(',', '.'))
                print(f'WAKTU TRANSAKSI   : {waktu}')
                print('---------------------------------------------------')
                
            # Ingin lanjut bertransaksi?
            print('Lanjut Transaksi?')
            print('1. Ya')
            print('2. Tidak')
            lanjut = int(input())
            if lanjut == 1:
                pilihan = 0
            else:
                pilihan = 10
            os.system('cls' if os.name == 'nt' else 'clear')   
            
        # Menu transfer
        elif (pilihan == 3) :
            typing_effect('===================ATM TRANSFER===================')
            typing_effect('==============MASUKKAN KODE BANK DAN==============')
            typing_effect('============NOMOR REKENING TUJUAN ANDA============')
            print('No. Kode Bank Diikuti Oleh No. Rek Tujuan')
            print('3 nomor diawal kode bank diikuti dengan 5 nomor rekening bank')
            print('Cth. 42612345')

            print('Apakah anda ingin melihat kode bank terlebih dahulu (y/n)?')
            cek_kode_bank = str(input(''))

            # Mencetak daftar kode bank
            os.system('cls' if os.name == 'nt' else 'clear') 
            kumpulan_bank = {
                '001':'BRI',        '007' : 'MANDIRI',
                '002':'BNI',        '008' : 'BTN',
                '003':'BRI',        '009' : 'PERMATA',
                '004':'RBS',        '010' : 'DKI',
                '005':'CITIBANK',   '011' : 'BSI',
                '006':'MUAMALAT',   '012' : 'KB BUKOPIN',
            }
            if (cek_kode_bank == 'y') :
                print('DAFTAR KODE BANK')
                print('001: BRI             007: MANDIRI')
                print('002: BNI             008: BTN')
                print('003: BCA             009: PERMATA')
                print('004: RBS             010: DKI')
                print('005: CITIBANK        011: BSI')
                print('006: MUAMALAT        012: KB BUKOPIN')

                time.sleep(7)
                print('Transaksi Akan Dilanjutkan')

                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')

            print('=================ATM TRANSFER=================')
            print('MASUKKAN KODE BANK DAN')
            print('NOMOR REKENING TUJUAN')
            print('No. Kode Bank Diikuti Oleh No. Rek Tujuan')
            print('3 nomor diawal kode bank diikuti dengan 5 nomor rekening bank')
            print('Cth. 00112345')
            print('')
            status_transfer = 'n'

            # Memasukkan nomor rekening tujuan
            while (status_transfer == 'n') :
                rekening_tujuan = str(input('Nomor Rekening Tujuan: '))
                kode_bank = rekening_tujuan[:3]
                nama_penerima = str(input('Nama Penerima: '))
                nomimal_transfer = int(input('Masukkan Jumlah Nominal Yang  Akan Ditransfer: '))
                while (nomimal_transfer>saldo) :
                    print('MOHON MAAF, SALDO ANDA TIDAK MENCUKUPI')
                    nomimal_transfer = int(input('Masukkan Kembali Nominal Yang Akan Ditransfer: '))

                print('HARAP MENUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   
                
                # Konfirmasi data transfer
                print('---------------------------------------------------')
                print('TRANSFER ATM')
                print(f'Bank            : {kumpulan_bank[kode_bank]}')
                print(f'Tujuan          : {rekening_tujuan}')
                print(f'Penerima        : {nama_penerima}')
                print(f'Jumlah Transfer : Rp{nomimal_transfer:,}'.replace(',', '.'))
                print('---------------------------------------------------')

                status_transfer= str(input(('Apakah data sudah sesuai (y/n)?    :')))

                os.system('cls' if os.name == 'nt' else 'clear') 
                if (status_transfer == 'y') :
                    print('HARAP MENUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')   
                    waktu = datetime.now().isoformat(' ', 'seconds')
                    saldo -= nomimal_transfer

                    # Mencetak struk transfer
                    print('====================================================')
                    typing_effect('TRANSFER ATM')
                    typing_effect(f'Bank            : {kumpulan_bank[kode_bank]}')
                    typing_effect(f'Tujuan          : {rekening_tujuan}')
                    typing_effect(f'Penerima        : {nama_penerima}')
                    typing_effect(f'Jumlah Transfer : Rp{nomimal_transfer:,}'.replace(',', '.'))
                    typing_effect(f'Waktu Transaksi : {waktu}')
                    print('====================================================')
                    print('')
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')   

                    print('TRANSAKSI TELAH SELESAI')
                    print('PERLU TRANSAKSI YANG LAIN?')

                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                    else :
                        pilihan = 10

        # Menu pembayaran (Telepon, PLN, dan PDAM)
        elif (pilihan == 4) :
            print('----------------------SILAHKAN PILIH----------------------')
            print('---------------JENIS PEMBAYARAN/PEMBELIAN-----------------')
            print('1. Telepon/HP')
            print('2. Listrik/PLN')
            print('3. Air/PDAM')
            pilih_pembayaran = int(input(''))
            os.system('cls' if os.name == 'nt' else 'clear')   

            # Pembayaran telepon/HP
            if (pilih_pembayaran == 1) :
                print('SILAHKAN MASUKKAN')
                print('NOMOR PELANGGAN/NOMOR')
                print('TAGIHAN/KODE PEMBAYARAN/NOMOR HANDPHONE ANDA')
                nomor_hp = int(input(''))
                os.system('cls' if os.name == 'nt' else 'clear')   

                print('HARAP MENUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   

                daftar_pembelian = {
                    '1' : 20000,            '5' : 150000,
                    '2' : 25000,            '6' : 200000,
                    '3' : 50000,            '7' : 300000,
                    '4' : 100000,           
                }

                # Mencetak nominal transfer
                print('PILIH JUMLAH NOMIMAL')
                print('1. 20.000            5. 150.000')
                print('2. 25.000            6. 200.000')
                print('3. 50.000            7. 300.000')
                print('4. 100.000           8. LAINNYA')
                print('BIAYA ADMIN RP 1.000')
                print('')

                nominal_isi_ulang = str(input(''))
                admin_bank = 1000
                total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank

                # Konfirmasi sebelum transaksi
                os.system('cls' if os.name == 'nt' else 'clear')   
                print('===========PEMBELIAN PULSA PRABAYAR===========')
                print(f'Nomor Handphone     : {nomor_hp}')
                print(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))
                print(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
                print('')
                print('PROSES TRANSAKSI (y/n)? ')
                proses_transaksi = str(input(''))
                os.system('cls' if os.name == 'nt' else 'clear')   

                # Pemrosesan transaksi
                if (proses_transaksi == 'y') and (saldo>=total_isi_ulang) :
                    saldo -= total_isi_ulang
                    print('HARAP MENUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')   

                    print('TRANSAKSI BERHASIL')
                    print('BERIKUT ADALAH STRUK ANDA')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    
                    # Mencetak struk transaksi pembayaran telepon/HP
                    print('=====================BANK TPB SUKSES======================')
                    print('=================PEMBELIAN PULSA PRABAYAR=================')
                    waktu = datetime.now().isoformat(' ', 'seconds')
                    typing_effect(f'Nomor Handphone     : {nomor_hp}')
                    typing_effect(f'Voucher Reff        : {random.randint(10000000000,99999999999)}')
                    typing_effect(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))
                    typing_effect(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
                    typing_effect(f'Waktu Transaksi     : {waktu}')

                    print('=========Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1=======')
                    print('===========PROVIDER BERKOM MENYATAKAN STRUK INI===========')
                    print('=============SEBAGAI BUKTI PEMBAYARAN YANG SAH============')
                    print('')

                    print('APAKAH ANDA MAU MELAKUKAN TRANSAKSI LAIN?')
                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                    else :
                        pilihan = 10

                # Kondisi ketika saldo tidak mencukupi
                elif (proses_transaksi == 'y') and (saldo<total_isi_ulang) :
                    print('MOHON MAAF SALDO ANDA TIDAK MENCUKUPI')
                    print('APAKAH ANDA MAU MELAKUKAN TRANSAKSI LAIN?')
                    
                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 

                # Kembali ke menu utama
                else :
                    print('MOHON TUNGGU SEBENTAR')
                    print('ANDA AKAN DIALIHKAN KE MENU UTAMA')
                    time.sleep(1)
                    pilihan = 0
            # Pembayaran PLN
            elif (pilih_pembayaran == 2) :
                print('MASUKKAN NOMOR METER ANDA')
                nomor_meter     = int(input(''))
                id_pelanggan    = random.randint(100000000000,999999999999)

                print('HARAP TUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')   

                # Menampilkan data listrik user
                print('===========PEMBELIAN LISTRIK PRABAYAR===========')
                print(f'Nomor Meter         : {nomor_meter}')
                print(f'IDPEL               : {id_pelanggan}')
                print(f'Nama                : {nama_lengkap}')
                print(f'Tarif/Daya          : R1M / 900 VA')
                print()

                daftar_pembelian = {
                    '1' : 20000,            '5' : 500000,
                    '2' : 50000,            '6' : 1000000,
                    '3' : 100000,           '7' : 5000000,
                    '4' : 200000,           '8' : 10000000,
                }

                # Memilih nominal pengisian
                print('PILIH JUMLAH NOMIMAL')
                print('1. 20.000            5. 500.000')
                print('2. 50.000            6. 1.000.000')
                print('3. 100.000           7. 5.000.000')
                print('4. 200.000           8. 10.000.000')
                print('BIAYA ADMIN RP 1.000')

                # Inisialisasi data untuk struk
                nominal_isi_ulang = str(input(''))
                admin_bank = 1000
                total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank
                os.system('cls' if os.name == 'nt' else 'clear')   

                # Kondisi ketika saldo mencukupi
                if (saldo>=total_isi_ulang) :
                    print('HARAP MENUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')  

                    saldo -= total_isi_ulang
                    waktu = datetime.now().isoformat(' ', 'seconds')
                    print('TRANSAKSI TELAH BERHASIL')
                    print('BERIKUT ADALAH STRUK ANDA')
                    print('')
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear') 

                    # Mencetak struk pembayaran listrik
                    print('=====================BANK TPB SUKSES======================')
                    print('============STRUK PEMBELIAN LISTRIK PRABAYAR==============')
                    typing_effect(f'Nomor meter         : {nomor_meter}')
                    typing_effect(f'IDPEL               : {id_pelanggan}')
                    typing_effect(f'Nama Lengkap        : {nama_lengkap}')
                    typing_effect(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))                    
                    typing_effect(f'Total Bayar         : {total_isi_ulang:,}'.replace(',', '.'))
                    typing_effect(f'Stroom/Token        : {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)}')
                    typing_effect(f'Admin Bank          : {admin_bank:,}'.replace(',', '.'))
                    typing_effect(f'Waktu Transaksi     : {waktu}')
                    print('=========Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1=======')
                    print('=================PLN MENYATAKAN STRUK INI=================')
                    print('=============SEBAGAI BUKTI PEMBAYARAN YANG SAH============')
                    print('')

                    print('APAKAH ANDA MAU MELAKUKAN TRANSAKSI LAIN?')
                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 
                else :
                    print('MOHON MAAF SALDO ANDA TIDAK MENCUKUPI')
                    print('APAKAH ANDA MAU MELAKUKAN TRANSAKSI LAIN?')
                    
                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 
            # Menu pembayaran PDAM
            elif (pilih_pembayaran == 3) :
                print('MASUKKAN KODE PERUSAHAAN')
                print('DIIKUTI NOMOR PELANGGAN ANDA')
                print('CONTOH')
                print('Kode Perusahaan  : 1300')
                print('No Pelanggan     : 1234567890')
                print('Tekan            : 13001234567890')

                status_kode = str(input('Apakah anda ingin melihat daftar kode air minum/PDAM (y/n)? '))
                os.system('cls' if os.name == 'nt' else 'clear')   
                
                kode_perusahaan = {
                    401 : 'PAM KOTA BOGOR'   , 406 : 'PAM KOTA CIREBON',
                    402 : 'PAM KOTA CIANJUR' , 407 : 'PAM KOTA SUBANG' ,
                    403 : 'PAM KOTA KUNINGAN', 408 : 'PAM KOTA CILEGON',
                    404 : 'PAM KOTA SUMEDANG', 409 : 'PAM KOTA DEPOK'  ,
                    405 : 'PAM KOTA SUKABUMI', 410 : 'PAM KOTA BANDUNG',
                }

                # Menampilkan daftar PDAM
                if (status_kode == 'y') :
                    print('DAFTAR KODE PERUSAHAAN')
                    print('PAM KOTA BOGOR               452')
                    print('PAM KOTA CIANJUR             453')
                    print('PAM KOTA KUNINGAN            456')
                    print('PAM KOTA SUMEDANG            458')
                    print('PAM KOTA SUKABUMI            465')
                    print('PAM KOTA CIREBON             476')
                    print('PAM KOTA SUBANG              480')
                    print('PAM KOTA CILEGON             489')
                    print('PAM KOTA DEPOK               494')
                    print('PAM KOTA BANDUNG             499')
                    time.sleep(7)
                    os.system('cls' if os.name == 'nt' else 'clear') 
                
                # Memasukkan data pelanggan
                print('MASUKKAN KODE PERUSAHAAN')
                print('DIIKUTI NOMOR PELANGGAN ANDA')
                print('CONTOH')
                print('Kode Perusahaan  : 1300')
                print('No Pelanggan     : 1234567890')
                print('Tekan            : 13001234567890') 
                print('')

                # Inisialisasi dan perhitungan nilai untuk di struk
                nomor_pelanggan = str(input(''))
                os.system('cls' if os.name == 'nt' else 'clear')   
                tagihan       = random.randint(0,saldo-1000)
                biaya_admin   = 1000
                total_bayar   = tagihan + biaya_admin
                 
                print('HARAP MENUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   

                # Konfirmasi data-data transaksi
                print('---------------------------------------------------')
                print('KONFIRMASI PEMBAYARAN')
                print(f'TAGIHAN {kode_perusahaan[nomor_pelanggan[:3]]}')
                print(f'No Pelanggan     : {nomor_pelanggan[3:]}')
                print(f'Nama             : {nama_lengkap}')
                print(f'Tagihan          : {tagihan:,}'.replace(',', '.')) 
                print(f'Biaya admin      : {biaya_admin:,}'.replace(',', '.')) 
                print(f'Total Bayar      : {total_bayar:,}'.replace(',', '.')) 
                print('---------------------------------------------------')
                print('')

                konfirmasi_pembayaran = str(input('Ingin Melanjutkan Pembayaran (y/n)? '))
                os.system('cls' if os.name == 'nt' else 'clear')

                # Mencetak struk pembayaran PDAM   
                if(konfirmasi_pembayaran == 'y') and (saldo>=total_bayar):
                    print('HARAP MENUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    saldo -= total_bayar
                    waktu = datetime.now().isoformat(' ', 'seconds')

                    print('TRANSAKSI TELAH BERHASIL')
                    print('Berikut adalah struk anda')
                    print('=====================BANK TPB SUKSES======================')
                    print('================STRUK PEMBAYARAN AIR/PDAM===============')
                    typing_effect(f'No pelanggan        : {nomor_pelanggan}')
                    typing_effect(f'Nama                : {nama_lengkap}')
                    typing_effect(f'Tagihan             : {tagihan}')
                    typing_effect(f'Biaya admin         : {biaya_admin:,}'.replace(',', '.')) 
                    typing_effect(f'Total Bayar         : {total_bayar:,}'.replace(',', '.')) 
                    typing_effect(f'Waktu Transaksi     : {waktu:,}'.replace(',', '.')) 
                    print('=========Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1=======')
                    print('=================PDAM MENYATAKAN STRUK INI=================')
                    print('=============SEBAGAI BUKTI PEMBAYARAN YANG SAH============')
                    print('')
                    print('APAKAH ANDA INGIN MELANJUTKAN TRANSAKSI (y/n)?')
                    lanjut_transaksi = str(input(''))

                    if (lanjut_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 
                elif (konfirmasi_pembayaran == 'y') and (saldo<total_bayar) :
                    print('MOHON MAAF SALDO ANDA TIDAK MENCUKUPI')
                    print('APAKAH ANDA MAU MELAKUKAN TRANSAKSI LAIN?')
                    print('')
                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 
                else :
                    print('MOHON TUNGGU SEBENTAR')
                    print('ANDA AKAN DIALIHKAN KE MENU UTAMA')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    pilihan = 0

        # Mengubah PIN
        elif (pilihan == 5) :
            status_pin_masuk = False
            while status_pin_masuk == False :
                pin_masuk = str(input('Masukkan PIN anda: '))
                if (pin_masuk == pin) :
                    status_pin_masuk = True
                    status_pin = False 
                    while (status_pin == False) :
                        pin = str(input('Masukkan PIN baru anda: '))
                        pin_konfirmasi = str(input('Konfirmasikan kembali PIN anda: '))
                        if (pin == pin_konfirmasi) :
                            os.system('cls' if os.name == 'nt' else 'clear')   
                            status_pin = True
                            print('PIN berhasil diubah!')
                            print('')
                            
                            # Ingin lanjut bertransaksi?
                            print('Lanjut Transaksi?')
                            print('1. Ya')
                            print('2. Tidak')
                            lanjut = int(input())
                            if lanjut == 1:
                                pilihan = 0
                            else:
                                pilihan = 10
                            os.system('cls' if os.name == 'nt' else 'clear')                               
                        else :
                            print('PIN tidak sesuai!')
                else :
                    print('PIN anda salah')
                    
    # Keluar dari ATM
    print('Silakan Ambil Kartu Anda')
    print('')
    time.sleep(0.3)
    card = [
                "|=============|",
                "|             |",
                "|             |",
                "|    KARTU    |",
                "|     ATM     |",
                "|             |",
                "|             |",
                "|=============|"
            ]
    
    # Cetak kartu 
    for i in range(len(card)):
        os.system('cls' if os.name == 'nt' else 'clear')
        # Cetak bagian bawah kartu bertahap hingga ke atas
        for line in card[-(i+1):]:
            print(line)
        time.sleep(0.2)

    print('')
    print('Terima Kasih telah menggunakan ATM BANK TPB SUKSES')
    time.sleep(3)

elif(bahasa == 2):
    # Memasukkan dan Mengecek PIN yang dimasukkan
    os.system('cls' if os.name == 'nt' else 'clear')
    counter = 2
    status_pin_masuk = False
    while (counter>= 0) and (status_pin_masuk == False) :
        pin_masuk = str(input('Enter your PIN: ')) 
        if (pin_masuk == pin) and (counter>0) : 
            status_pin_masuk = True
            print('You have logged in.')
        elif (counter == 0) : # Mengunci akun dan melakukan recovery akun
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('Your account has been locked. Please reset your PIN.')
            print('Please reconfirm your identity data.')
            nama_lengkap_konfirmasi = str(input('Full Name: '))
            tanggal_lahir_konfirmasi = str(input('Date Of Birth: '))
            # Mengatur ulang PIN dengan memasukkan data-data pribadi (nama, tanggal lahir)
            if (nama_lengkap == nama_lengkap_konfirmasi) and (tanggal_lahir == tanggal_lahir_konfirmasi) :
                status_pin = False 
                while (status_pin == False) :
                    pin = str(input('Enter your new PIN: '))
                    pin_konfirmasi = str(input('Confirm your new PIN: '))
                    if (pin == pin_konfirmasi) :
                        status_pin = True
                        print('PIN changed successfully!')
                        counter = 3
                    else :
                        print('Wrong PIN entered !')

            else :# Menanyakan ulang data-data pribadi jika sebelumnya data yang diberikan di awal salah
                while (nama_lengkap_konfirmasi != nama_lengkap) and (tanggal_lahir_konfirmasi != tanggal_lahir) :
                    print('Your account has been locked. Please reset your PIN.')
                    print('Please reconfirm your identity data.')
                    nama_lengkap_konfirmasi = str(input('Nama Lengkap: '))
                    tanggal_lahir_konfirmasi = str(input('Tanggal Lahir: '))
                if (nama_lengkap == nama_lengkap_konfirmasi) and (tanggal_lahir == tanggal_lahir_konfirmasi) :
                    status_pin = False 
                    while (status_pin == False) :
                        os.system('cls' if os.name == 'nt' else 'clear') 
                        pin = str(input('Enter your new PIN: '))
                        pin_konfirmasi = str(input('Confirm your new PIN: '))
                        if (pin == pin_konfirmasi) :
                            status_pin = True
                            print('PIN changed successfully!')
                            counter = 3

                            os.system('cls' if os.name == 'nt' else 'clear') 
                        else :
                            print('Wrong PIN Entered!')
                            os.system('cls' if os.name == 'nt' else 'clear') 
        else : # Alert ketika user salah memasukkkan PIN
            counter -= 1
            print(f'Wrong PIN Entered. Please try again. You have {counter+1} more chances')
                        
    # Menampilkan menu yang bisa dipilih
    os.system('cls' if os.name == 'nt' else 'clear')     
    print('PLEASE SELECT YOUR DESIRED TRANSACTION MENU')
    print('1. Balance Information')
    print('2. Cash Withdrawal')
    print('3. Transfer')
    print('4. Payment')
    print('5. Change PIN')
    print('6. Finish Transaction')
    
    pilihan = int(input('Enter your desired menu: '))
    os.system('cls' if os.name == 'nt' else 'clear')     

    # Masuk ke menu-menu yang disediakan 
    while ((pilihan == 0) or (pilihan == 1) or (pilihan == 2) or (pilihan == 3) or (pilihan == 4) or (pilihan == 5)):
        if (pilihan == 0) :
            os.system('cls' if os.name == 'nt' else 'clear')   
            print('PLEASE SELECT YOUR DESIRED TRANSACTION MENU')
            print('1. Balance Information')
            print('2. Cash Withdrawal')
            print('3. Transfer')
            print('4. Payment')
            print('5. Change PIN')
            print('6. Finish Transaction')
            
            pilihan = int(input('Enter your desired menu: '))
            os.system('cls' if os.name == 'nt' else 'clear')     
                
        # Menu informasi saldo       
        elif (pilihan == 1) :
            print('PLEASE WAIT')
            print('YOUR TRANSACTION IS BEING PROCESSED')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')   

            # Menampilkan saldo rekening         
            print('YOUR ACCOUNT BALANCE')
            print(f'RP.{saldo:,}'.replace(',', '.'))
            print('')
            
            # Konfirmasi lanjut transaksi/tidak?
            print('Continue Transaction?')
            print('1. Yes')
            print('2. No')
            lanjut = int(input())
            if lanjut == 1:
                pilihan = 0
            else:
                pilihan = 10
            os.system('cls' if os.name == 'nt' else 'clear')   

        # Menu penarikan tunai 
        elif (pilihan == 2) :
            print('FAST WITHDRAWAL MENU')
            print('PLEASE ENTER WITHDRAWAL AMOUNT')
            print('1. Rp    50.000')
            print('2. Rp   200.000')
            print('3. Rp   500.000')
            print('4. Rp 1.000.000')
            print('5. OTHER AMOUNT')
            tarik = int(input())
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Penarikan Tunai Cepat
            receipt = 0
            
            # Mengambil Rp50.000
            if tarik == 1:
                print('PLEASE WAIT')
                print('YOUR TRANSACTION IS BEING PROCESSED')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')       
                if saldo >= 50000:
                    saldo -= 50000
                    tunai = 50000
                    print('You have successfully withdrawed Rp50.000')
                    print(f'Your remaining account balance is Rp{saldo:,}'.replace(',', '.'))
                    print('Do you wish to print the receipt?')
                    print('1. Yes')
                    print('2. No')
                    receipt = int(input())
                else:
                    print('BALANCE NOT ENOUGH')
                    print('')     

            # Mengambil Rp200.000       
            elif tarik == 2:
                print('PLEASE WAIT')
                print('YOUR TRANSACTION IS BEING PROCESSED')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   
                if saldo >= 200000:
                    saldo -= 200000
                    tunai = 200000
                    print('You have successfully withdrawed Rp200.000')
                    print(f'Your remaining account balance is Rp{saldo:,}'.replace(',', '.'))
                    print('Do you wish to print the receipt?')
                    print('1. Yes')
                    print('2. No')
                    receipt = int(input())
                else:
                    print('BALANCE NOT ENOUGH')
                    print('')     

            # Mengambil Rp500.000          
            elif tarik == 3:
                print('PLEASE WAIT')
                print('YOUR TRANSACTION IS BEING PROCESSED')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   
                if saldo >= 500000:
                    saldo -= 500000
                    tunai = 500000
                    print('You have successfully withdrawed Rp500.000')
                    print(f'Your remaining account balance is Rp{saldo:,}'.replace(',', '.'))
                    print('Do you wish to print the receipt?')
                    print('1. Yes')
                    print('2. No')
                    receipt = int(input())
                else:
                    print('BALANCE NOT ENOUGH')
                    print('')     

            # Mengambil Rp1.000.000           
            elif tarik == 4:
                print('PLEASE WAIT')
                print('YOUR TRANSACTION IS BEING PROCESSED')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   
                if saldo >= 1000000:
                    saldo -= 1000000
                    tunai = 1000000
                    print('You have successfully withdrawed Rp1.000.000')
                    print(f'Your remaining account balance is Rp{saldo:,}'.replace(',', '.'))
                    print('Do you wish to print the receipt?')
                    print('1. Yes')
                    print('2. No')
                    receipt = int(input())
                else:
                    print('BALANCE NOT ENOUGH')
                    print('')     
            # Mengambil selain pilihan sebelumnya (harus kelipatan 50.000, maks Rp1.250.000)         
            elif tarik == 5:
                status_tarik = False
                while status_tarik == False:   
                    print('ENTER YOUR DESIRED CASH AMOUNT')
                    print('(MULTIPLE OF RP50.000)')
                    print('MAXIMAL RP1.250.000')
                    tunai = int(input('JUMLAH PENARIKAN: '))
                    if tunai < 50000:
                        print('AMOUNT TOO SMALL')
                        print('')
                    elif tunai > 1250000:
                        print('AMOUNT TOO LARGE')
                        print('')
                    elif tunai % 50000 != 0:
                        print('AMOUNT INVALID')
                        print('')
                    elif saldo < tunai:
                        print('BALANCE NOT ENOUGH')
                        print('')
                    else: 
                        print(f'THE AMOUNT YOU INPUTTED IS Rp{tunai:,}'.replace(',', '.'))
                        print('ARE YOU SURE?')
                        konfirmasi_tarik = input('Confirmation (y/n): ')
                        if konfirmasi_tarik == 'y':
                            status_tarik = True
                
                # Mencetak sisa saldo setelah tarik tunai
                if status_tarik == True:
                    os.system('cls' if os.name == 'nt' else 'clear')  
                    print('PLEASE WAIT')
                    print('YOUR TRANSACTION IS BEING PROCESSED')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')   
                    saldo -= tunai  
                    print(f'You have successfully withdrawedt Rp {tunai:,}'.replace(',', '.'))
                    print(f'Your remaining account balance is Rp{saldo:,}'.replace(',', '.'))
                    print('Do you wish to print the receipt?')
                    print('1. Yes')
                    print('2. No')
                    receipt = int(input())
                    os.system('cls' if os.name == 'nt' else 'clear')  

            # Mencetak receipt
            if receipt == 1:
                waktu = datetime.now().isoformat(' ', 'seconds')
                print('---------------------------------------------------')
                print('CASH WITHDRAWAL')
                print(f'TOTAL                  : Rp{tunai:,}'.replace(',', '.'))
                print(f'REMAINING BALANCE      : Rp{saldo:,}'.replace(',', '.'))
                print(f'TRANSACTION TIME       : {waktu}')
                print('---------------------------------------------------')
                
            # Ingin lanjut bertransaksi?
            print('Continue Transaction?')
            print('1. Yes')
            print('2. No')
            lanjut = int(input())
            if lanjut == 1:
                pilihan = 0
            else:
                pilihan = 10
            os.system('cls' if os.name == 'nt' else 'clear')   
            
        # Menu transfer
        elif (pilihan == 3) :
            typing_effect('=================ATM TRANSFER=====================')
            typing_effect('============ENTER YOUR BANK CODE AND==============')
            typing_effect('=========THE DESTINATION ACCOUNT NUMBER===========')
            print('Bank Code Followed By Destination Account Number')
            print(' 3 digits bank code followed by 5 digits destination account')
            print('Cth. 42612345')

            print('Do you wish to see the bank codes first? (y/n)?')
            cek_kode_bank = str(input(''))

            # Mencetak daftar kode bank
            os.system('cls' if os.name == 'nt' else 'clear') 
            kumpulan_bank = {
                '001':'BRI',        '007' : 'MANDIRI',
                '002':'BNI',        '008' : 'BTN',
                '003':'BRI',        '009' : 'PERMATA',
                '004':'RBS',        '010' : 'DKI',
                '005':'CITIBANK',   '011' : 'BSI',
                '006':'MUAMALAT',   '012' : 'KB BUKOPIN',
            }
            if (cek_kode_bank == 'y') :
                print('BANK CODES LIST')
                print('001: BRI             007: MANDIRI')
                print('002: BNI             008: BTN')
                print('003: BCA             009: PERMATA')
                print('004: RBS             010: DKI')
                print('005: CITIBANK        011: BSI')
                print('006: MUAMALAT        012: KB BUKOPIN')

                time.sleep(7)
                print('Transaction Will Be Continued')

                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')

            typing_effect('=================ATM TRANSFER=====================')
            typing_effect('============ENTER YOUR BANK CODE AND==============')
            typing_effect('=========THE DESTINATION ACCOUNT NUMBER===========')
            print('Bank Code Followed By Destination Account Number')
            print(' 3 digits bank code followed by 5 digits destination account')
            print('Cth. 42612345')
            status_transfer = 'n'

            # Memasukkan nomor rekening tujuan
            while (status_transfer == 'n') :
                rekening_tujuan = str(input('Destination Account Number: '))
                kode_bank = rekening_tujuan[:3]
                nama_penerima = str(input('Transferee Name: '))
                nomimal_transfer = int(input('Enter The Amount You Wish To Transfer: '))
                while (nomimal_transfer>saldo) :
                    print('SORRY, YOUR BALANCE IS NOT ENOUGH')
                    nomimal_transfer = int(input('Renter The Amount You Wish To Transfer: '))

                print('PLEASE WAIT')
                print('YOUR TRANSACTION IS BEING PROCESSED')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   
                
                # Konfirmasi data transfer
                print('---------------------------------------------------')
                print('TRANSFER ATM')
                print(f'Bank            : {kumpulan_bank[kode_bank]}')
                print(f'Destination     : {rekening_tujuan}')
                print(f'Transferee      : {nama_penerima}')
                print(f'Transfer Amount : Rp{nomimal_transfer:,}'.replace(',', '.'))
                print('---------------------------------------------------')

                status_transfer= str(input(('Is the data correct? (y/n)    :')))

                os.system('cls' if os.name == 'nt' else 'clear') 
                if (status_transfer == 'y') :
                    print('PLEASE WAIT')
                    print('YOUR TRANSACTION IS BEING PROCESSED')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')   
                    waktu = datetime.now().isoformat(' ', 'seconds')

                    # Mencetak struk transfer
                    print('====================================================')
                    typing_effect('TRANSFER ATM')
                    typing_effect(f'Bank             : {kumpulan_bank[kode_bank]}')
                    typing_effect(f'Destination      : {rekening_tujuan}')
                    typing_effect(f'Transferee       : {nama_penerima}')
                    typing_effect(f'Transfer Amount  : Rp{nomimal_transfer:,}'.replace(',', '.'))
                    typing_effect(f'Transaction Time : {waktu}')
                    print('====================================================')
                    print('')
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')   

                    print('TRANSACTION COMPLETED')
                    print('CONTINUE TRANSACTION?')

                    status_transaksi = str(input('Confirmation (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                    else :
                        pilihan = 10

        # Menu pembayaran (Telepon, PLN, dan PDAM)
        elif (pilihan == 4) :
            print('----------------------PLEASE CHOOSE ----------------------')
            print('---------------PAYMENT / PURCHASE TYPE--------------------')
            print('1. Telephone')
            print('2. Electric Bill/PLN')
            print('3. Water Bill/PDAM')
            pilih_pembayaran = int(input(''))
            os.system('cls' if os.name == 'nt' else 'clear')   

            # Pembayaran telepon/HP
            if (pilih_pembayaran == 1) :
                print('PLEASE ENTER')
                print('CUSTOMER CODE/ INVOICE')
                print('NUMBER/PAYMENT CODE/PHONE NUMBER')
                nomor_hp = int(input(''))
                os.system('cls' if os.name == 'nt' else 'clear')   

                print('PLEASE WAIT')
                print('YOUR TRANSACTION IS BEING PROCESSED')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   

                daftar_pembelian = {
                    '1' : 20000,            '5' : 150000,
                    '2' : 25000,            '6' : 200000,
                    '3' : 50000,            '7' : 300000,
                    '4' : 100000,           
                }

                # Mencetak nominal transfer
                print('CHOOSE AMOUNT')
                print('1. 20.000            5. 150.000')
                print('2. 25.000            6. 200.000')
                print('3. 50.000            7. 300.000')
                print('4. 100.000           8. LAINNYA')
                print('ADMIN FEE RP 1.000')
                print('')

                nominal_isi_ulang = str(input(''))
                admin_bank = 1000
                total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank

                # Konfirmasi sebelum transaksi
                os.system('cls' if os.name == 'nt' else 'clear')   
                print('===========PREPAID PHONE CREDIT PURCHASE===========')
                print(f'PHONE NUMBER        : {nomor_hp}')
                print(f'CREDIT AMOUNT       : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))
                print(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
                print('')
                print('CONFIRM TRANSACTION (y/n)? ')
                proses_transaksi = str(input(''))
                os.system('cls' if os.name == 'nt' else 'clear')   

                # Pemrosesan transaksi
                if (proses_transaksi == 'y') and (saldo>=total_isi_ulang) :
                    saldo -= total_isi_ulang
                    print('PLEASE WAIT')
                    print('YOUR TRANSACTION IS BEING PROCESSED')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')   

                    print('TRANSACTION SUCCESS')
                    print('HERE IS YOUR RECEIPT')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    
                    # Mencetak struk transaksi pembayaran telepon/HP
                    print('=====================BANK TPB SUKSES======================')
                    print('==============PREPAID PHONE CREDIT PURCHASE===============')
                    waktu = datetime.now().isoformat(' ', 'seconds')
                    typing_effect(f'Phone Number        : {nomor_hp}')
                    typing_effect(f'Voucher Reff        : {random.randint(10000000000,99999999999)}')
                    typing_effect(f'Credit Amount       : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))
                    typing_effect(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
                    typing_effect(f'Transaction Time    : {waktu}')

                    print('=========Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1=======')
                    print('==========PROVIDER BERKOM DECLARES THIS RECEIPT===========')
                    print('================AS VALID PROOF OF PURCHASE================')
                    print('')

                    print('DO YOU WISH TO MAKE ANOTHER TRANSACTION?')
                    status_transaksi = str(input('Confirmation (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                    else :
                        pilihan = 10

                # Kondisi ketika saldo tidak mencukupi
                elif (proses_transaksi == 'y') and (saldo<total_isi_ulang) :
                    print('SORRY YOUR BALANCE IS NOT ENOUGH')
                    print('DO YOU WISH TO MAKE ANOTHER TRANSACTION?')
                    
                    status_transaksi = str(input('Confirmation (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 

                # Kembali ke menu utama
                else :
                    print('PLEASE WAIT A MOMENT')
                    print('YOU WILL BE REDIRECTED TO THE MAIN MENU')
                    time.sleep(1)
                    pilihan = 0
            # Pembayaran PLN
            elif (pilih_pembayaran == 2) :
                print('ENTER YOUR METER NUMBER')
                nomor_meter     = int(input(''))
                id_pelanggan    = random.randint(100000000000,999999999999)

                print('PLEASE WAIT')
                print('YOUR TRANSACTION IS BEING PROCESSED')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')   

                # Menampilkan data listrik user
                print('===========PREPAID ELECTRIC PAYMENT===========')
                print(f'Meter Number        : {nomor_meter}')
                print(f'Customer ID         : {id_pelanggan}')
                print(f'Name                : {nama_lengkap}')
                print(f'Tariff/Power        : R1M / 900 VA')
                print()

                daftar_pembelian = {
                    '1' : 20000,            '5' : 500000,
                    '2' : 50000,            '6' : 1000000,
                    '3' : 100000,           '7' : 5000000,
                    '4' : 200000,           '8' : 10000000,
                }

                # Memilih nominal pengisian
                print('SELECT AMOUNT ')
                print('1. 20.000            5. 500.000')
                print('2. 50.000            6. 1.000.000')
                print('3. 100.000           7. 5.000.000')
                print('4. 200.000           8. 10.000.000')
                print('ADMIN FEE RP 1.000')

                # Inisialisasi data untuk struk
                nominal_isi_ulang = str(input(''))
                admin_bank = 1000
                total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank
                os.system('cls' if os.name == 'nt' else 'clear')   

                # Kondisi ketika saldo mencukupi
                if (saldo>=total_isi_ulang) :
                    print('PLEASE WAIT')
                    print('YOUR TRANSACTION IS BEING PROCESSED')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')  

                    waktu = datetime.now().isoformat(' ', 'seconds')
                    print('TRANSACTION COMPLETED')
                    print('HERE IS YOUR RECEIPT')
                    print('')
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear') 

                    # Mencetak struk pembayaran listrik
                    print('=====================BANK TPB SUKSES======================')
                    print('==========PREPAID ELECTRICITY PURCHASE RECEIPT============')
                    typing_effect(f'Meter Number        : {nomor_meter}')
                    typing_effect(f'Customer ID         : {id_pelanggan}')
                    typing_effect(f'Full Name           : {nama_lengkap}')
                    typing_effect(f'Purchase Amount     : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))                    
                    typing_effect(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
                    typing_effect(f'Stroom/Token        : {random.randint(1000,9999)}, {random.randint(1000,9999)}, {random.randint(1000,9999)}, {random.randint(1000,9999)}')
                    typing_effect(f'Admin Bank          : {admin_bank:,}'.replace(',', '.'))
                    typing_effect(f'Transaction Time    : {waktu}')
                    print('=========Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1=======')
                    print('=================PLN DECLARES THIS RECEIPT================')
                    print('================AS A VALID PROOF OF PURCHASE==============')
                    print('')

                    print('DO YOU WISH TO MAKE ANOTHER TRANSACTION?')
                    status_transaksi = str(input('Confirmation (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 
                else :
                    print('SORRY YOUR BALANCE IS NOT ENOUGH')
                    print('DO YOU WISH TO MAKE ANOTHER TRANSACTION?')
                    
                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 
            # Menu pembayaran PDAM
            elif (pilih_pembayaran == 3) :
                print('ENTER COMPANY CODE')
                print('FOLLOWED BY YOUR CUSTOMER NUMBER')
                print('EXAMPLE')
                print('Company Code     : 1300')
                print('Customer Number    : 1234567890')
                print('Tekan            : 13001234567890')

                status_kode = str(input('Do you wish to see the water/PDAM codes (y/n)? '))
                os.system('cls' if os.name == 'nt' else 'clear')   
                
                kode_perusahaan = {
                    401 : 'PAM KOTA BOGOR'   , 406 : 'PAM KOTA CIREBON',
                    402 : 'PAM KOTA CIANJUR' , 407 : 'PAM KOTA SUBANG' ,
                    403 : 'PAM KOTA KUNINGAN', 408 : 'PAM KOTA CILEGON',
                    404 : 'PAM KOTA SUMEDANG', 409 : 'PAM KOTA DEPOK'  ,
                    405 : 'PAM KOTA SUKABUMI', 410 : 'PAM KOTA BANDUNG',
                }

                # Menampilkan daftar PDAM
                if (status_kode == 'y') :
                    print('COMPANY CODES LIST')
                    print('PAM KOTA BOGOR               452')
                    print('PAM KOTA CIANJUR             453')
                    print('PAM KOTA KUNINGAN            456')
                    print('PAM KOTA SUMEDANG            458')
                    print('PAM KOTA SUKABUMI            465')
                    print('PAM KOTA CIREBON             476')
                    print('PAM KOTA SUBANG              480')
                    print('PAM KOTA CILEGON             489')
                    print('PAM KOTA DEPOK               494')
                    print('PAM KOTA BANDUNG             499')
                    time.sleep(7)
                    os.system('cls' if os.name == 'nt' else 'clear') 
                
                # Memasukkan data pelanggan
                print('ENTER COMPANY CODE')
                print('FOLLOWED BY YOUR CUSTOMER NUMBER')
                print('EXAMPLE')
                print('Company Code     : 1300')
                print('Customer Number    : 1234567890')
                print('Tekan            : 13001234567890')

                # Inisialisasi dan perhitungan nilai untuk di struk
                nomor_pelanggan = str(input(''))
                os.system('cls' if os.name == 'nt' else 'clear')   
                tagihan       = random.randint(0,saldo-1000)
                biaya_admin   = 1000
                total_bayar   = tagihan + biaya_admin
                 
                print('PLEASE WAIT')
                print('YOUR TRANSACTION IS BEING PROCESSED')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   

                # Konfirmasi data-data transaksi
                print('---------------------------------------------------')
                print('PAYMENT CONFIRMATION')
                print(f'INVOICE {kode_perusahaan[nomor_pelanggan[:3]]}')
                print(f'Customer Number  : {nomor_pelanggan[3:]}')
                print(f'Name             : {nama_lengkap}')
                print(f'Bill             : {tagihan:,}'.replace(',', '.')) 
                print(f'Admin fee        : {biaya_admin:,}'.replace(',', '.')) 
                print(f'TOTAL            : {total_bayar:,}'.replace(',', '.')) 
                print('---------------------------------------------------')
                print('')

                konfirmasi_pembayaran = str(input('Continue Payment (y/n)? '))
                os.system('cls' if os.name == 'nt' else 'clear')

                # Mencetak struk pembayaran PDAM   
                if(konfirmasi_pembayaran == 'y') and (saldo>=total_bayar):
                    print('PLEASE WAIT')
                    print('YOUR TRANSACTION IS BEING PROCESSED')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    waktu = datetime.now().isoformat(' ', 'seconds')

                    print('TRANSACTION COMPLETED')
                    print('Here is your receipt')
                    print('=====================BANK TPB SUKSES======================')
                    print('================WATER / PDAM BILL PAYMENT=================')
                    typing_effect(f'Customer Number     : {nomor_pelanggan}')
                    typing_effect(f'Name                : {nama_lengkap}')
                    typing_effect(f'Bill                : {tagihan}')
                    typing_effect(f'Admin fee           : {biaya_admin:,}'.replace(',', '.')) 
                    typing_effect(f'TOTAL               : {total_bayar:,}'.replace(',', '.')) 
                    typing_effect(f'Transaction Time    : {waktu:,}'.replace(',', '.')) 
                    print('=========Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1=======')
                    print('=================PDAM DECLARES THIS RECEIPT================')
                    print('================AS A VALID PROOF OF PURCHASE===============')
                    print('')
                    print('DO YOU WISH TO MAKE OTHER TRANSACTIONS? (y/n)')
                    lanjut_transaksi = str(input(''))

                    if (lanjut_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 
                elif (konfirmasi_pembayaran == 'y') and (saldo<total_bayar) :
                    print('SORRY YOUR BALANCE IS NOT ENOUGH')
                    print('DO YOU WISH TO MAKE OTHER TRANSACTIONS? ')
                    print('')
                    status_transaksi = str(input('Confirmation (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                        os.system('cls' if os.name == 'nt' else 'clear') 
                    else :
                        pilihan = 10
                        os.system('cls' if os.name == 'nt' else 'clear') 
                else :
                    print('PLEASE WAIT A MOMENT')
                    print('YOU WILL BE DIRECTED TO THE MAIN MENU')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    pilihan = 0

        # Mengubah PIN
        elif (pilihan == 5) :
            status_pin_masuk = False
            while status_pin_masuk == False :
                pin_masuk = str(input('Enter your PIN: '))
                if (pin_masuk == pin) :
                    status_pin_masuk = True
                    status_pin = False 
                    while (status_pin == False) :
                        pin = str(input('Enter your new PIN: '))
                        pin_konfirmasi = str(input('Please confirm your new PIN: '))
                        if (pin == pin_konfirmasi) :
                            os.system('cls' if os.name == 'nt' else 'clear')   
                            status_pin = True
                            print('PIN changed successfully!')
                            print('')
                            
                            # Ingin lanjut bertransaksi?
                            print('Continue Transaction?')
                            print('1. Yes')
                            print('2. No')
                            lanjut = int(input())
                            if lanjut == 1:
                                pilihan = 0
                            else:
                                pilihan = 10
                            os.system('cls' if os.name == 'nt' else 'clear')                               
                        else :
                            print('Wrong PIN entered!')
                else :
                    print('Wrong PIN entered')
                    
    # Keluar dari ATM
    print('Please Take Your Card')
    print('')
    time.sleep(0.3)
    card = [
                "|=============|",
                "|             |",
                "|             |",
                "|    KARTU    |",
                "|     ATM     |",
                "|             |",
                "|             |",
                "|=============|"
            ]
    # Cetak kartu 
    for i in range(len(card)):
        os.system('cls' if os.name == 'nt' else 'clear')
        # Cetak bagian bawah kartu bertahap hingga ke atas
        for line in card[-(i+1):]:
            print(line)
        time.sleep(0.2)

    print('')
    print('Thanks For Using ATM BANK TPB SUKSES')
    time.sleep(3)

