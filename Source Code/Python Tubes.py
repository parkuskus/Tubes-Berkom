import os
import time
import random
import sys
from datetime import datetime


#Fungsi Fade Text di Terminal
def scrolling_text(text, delay=0.02):
    for i in range(len(text) + 1):
        os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan terminal
        print(text[:i])  # Cetak sebagian teks
        time.sleep(delay)

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
    pin_konfirmasi = str(input(('Masukkan kembali PIN yang telah anda buat: ')))
    if (pin == pin_konfirmasi) :
        status_pin = True
    else :
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
'''
os.system('cls' if os.name == 'nt' else 'clear')
typing_effect('Berikut adalah data-data pribadi anda!')
typing_effect(f'Nama Lengkap    : {nama_lengkap}')
typing_effect(f'Tanggal Lahir   : {tanggal_lahir}')
typing_effect(f'PIN             : {pin}')
typing_effect(f'Saldo Awal      : Rp{saldo:,}'.replace(',', '.'))
time.sleep(4)
'''
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
    # Mengecek PIN yang dimasukkan
    os.system('cls' if os.name == 'nt' else 'clear')
    counter = 2
    status_pin_masuk = False
    while (counter>= 0) and (status_pin_masuk == False) :
        pin_masuk = str(input('Masukkan PIN anda: '))
        if (pin_masuk == pin) and (counter>0) :
            status_pin_masuk = True
            print('Anda berhasil masuk')
        elif (counter == 0) :
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('Akun anda telah dikunci. Silahkan atur ulang PIN anda.')
            print('Silakan konfirmasi kembali data pribadi anda.')
            nama_lengkap_konfirmasi = str(input('Nama Lengkap: '))
            tanggal_lahir_konfirmasi = str(input('Tanggal Lahir: '))
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
                        os.system('cls' if os.name == 'nt' else 'clear') 
            else :
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
        else :
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
               
        elif (pilihan == 1) :
            print('HARAP MENUNGGU')
            print('TRANSAKSI ANDA SEDANG DIPROSES')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')            
            print('SALDO REKENING ANDA')
            print(f'RP.{saldo:,}'.replace(',', '.'))
            print('')
            print('Lanjut Transaksi?')
            print('1. Ya')
            print('2. Tidak')
            lanjut = int(input())
            if lanjut == 1:
                pilihan = 0
            else:
                pilihan = 10
            os.system('cls' if os.name == 'nt' else 'clear')   
            
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
            
        elif (pilihan == 3) :
            typing_effect('===================ATM TRANSFER===================')
            typing_effect('==============MASUKKAN KODE BANK DAN==============')
            typing_effect('============NOMOR REKENING TUJUAN ANDA============')
            print('No. Kode Bank Diikuti Oleh No. Rek Tujuan')
            print('3 nomor diawal kode bank diikuti dengan 5 nomor rekening bank')
            print('Cth. 42612345')

            print('Apakah anda ingin melihat kode bank terlebih dahulu (y/n)?')
            cek_kode_bank = str(input(''))

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

        elif (pilihan == 4) :
            print('----------------------SILAHKAN PILIH----------------------')
            print('---------------JENIS PEMBAYARAN/PEMBELIAN-----------------')
            print('1. Telepon/HP')
            print('2. Listrik/PLN')
            print('3. Air/PDAM')
            pilih_pembayaran = int(input(''))
            os.system('cls' if os.name == 'nt' else 'clear')   

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


                os.system('cls' if os.name == 'nt' else 'clear')   
                print('===========PEMBELIAN PULSA PRABAYAR===========')
                print(f'Nomor Handphone     : {nomor_hp}')
                print(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))
                print(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
                print('')
                print('PROSES TRANSAKSI (y/n)? ')
                proses_transaksi = str(input(''))
                os.system('cls' if os.name == 'nt' else 'clear')   

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
                else :
                    print('MOHON TUNGGU SEBENTAR')
                    print('ANDA AKAN DIALIHKAN KE MENU UTAMA')
                    time.sleep(1)
                    pilihan = 0
            elif (pilih_pembayaran == 2) :
                print('MASUKKAN NOMOR METER ANDA')
                nomor_meter     = int(input(''))
                id_pelanggan    = random.randint(100000000000,999999999999)

                print('HARAP TUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')   

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
                print('PILIH JUMLAH NOMIMAL')
                print('1. 20.000            5. 500.000')
                print('2. 50.000            6. 1.000.000')
                print('3. 100.000           7. 5.000.000')
                print('4. 200.000           8. 10.000.000')
                print('BIAYA ADMIN RP 1.000')

                nominal_isi_ulang = str(input(''))
                admin_bank = 1000
                total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank
                os.system('cls' if os.name == 'nt' else 'clear')   

                if (saldo>=total_isi_ulang) :
                    print('HARAP MENUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')  

                    waktu = datetime.now().isoformat(' ', 'seconds')
                    print('TRANSAKSI TELAH BERHASIL')
                    print('BERIKUT ADALAH STRUK ANDA')
                    print('')
                    print('=====================BANK TPB SUKSES======================')
                    print('============STRUK PEMBELIAN LISTRIK PRABAYAR==============')
                    typing_effect(f'Nomor meter         : {nomor_meter}')
                    typing_effect(f'IDPEL               : {id_pelanggan}')
                    typing_effect(f'Nama Lengkap        : {nama_lengkap}')
                    typing_effect(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))                    
                    typing_effect(f'Total Bayar         : {total_isi_ulang:,}'.replace(',', '.'))
                    typing_effect(f'Stroom/Token        : {random.randint(1000,9999)}, {random.randint(1000,9999)}, {random.randint(1000,9999)}, {random.randint(1000,9999)}')
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
                    
                print('MASUKKAN KODE PERUSAHAAN')
                print('DIIKUTI NOMOR PELANGGAN ANDA')
                print('CONTOH')
                print('Kode Perusahaan  : 1300')
                print('No Pelanggan     : 1234567890')
                print('Tekan            : 13001234567890') 
                print('')
                nomor_pelanggan = str(input(''))
                os.system('cls' if os.name == 'nt' else 'clear')   
                tagihan       = random.randint(0,saldo-1000)
                biaya_admin   = 1000
                total_bayar   = tagihan + biaya_admin
                 
                print('HARAP MENUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')   

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
                if(konfirmasi_pembayaran == 'y') and (saldo>=total_bayar):
                    print('HARAP MENUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    waktu = datetime.now().isoformat(' ', 'seconds')

                    print('TRANSAKSI TELAH BERHASIL')
                    print('Berikut adalah struk anda')
                    print('=====================BANK TPB SUKSES======================')
                    print('================STRUK PEMBAYARAN AIR/PDAM===============')
                    typing_effect(f'Nomor meter         : {nomor_pelanggan}')
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
