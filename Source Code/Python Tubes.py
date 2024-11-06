import os
import time
from datetime import datetime

#Fungsi Fade Text di Terminal
def scrolling_text(text, delay=0.05):
    for i in range(len(text) + 1):
        os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan terminal
        print(text[:i])  # Cetak sebagian teks
        time.sleep(delay)

#Menyambut pengguna
print('SELAMAT DATANG DI BANK PERMATA SARI')
time.sleep(2)

# Membuat akun 
print('Silahkan masukkan data-data di bawah ini!')
nama_lengkap    = str(input('Nama Lengkap : '))
tanggal_lahir   = str(input('Tanggal Lahir (DD/MM/YYYY): '))
os.system('cls' if os.name == 'nt' else 'clear')

#Membuat PIN 
status_pin = False 
while (status_pin == False) :
    pin = str(input('Masukkan PIN anda: '))
    pin_konfirmasi = str(input(('Masukkan kembali PIN yang telah anda buat: ')))
    if (pin == pin_konfirmasi) :
        status_pin = True
    else :
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('PIN yang anda masukkan belum sama. Silahkan masukkan kembali PIN anda')

#Mengisi saldo awal
os.system('cls' if os.name == 'nt' else 'clear')
saldo = int(input('Masukkan jumlah saldo awal yang anda ingin masukkan (Minimum saldo awal adalah 50.000): '))
while (saldo<50000) :
    saldo = int(input('Masukkan jumlah saldo awal yang anda ingin masukkan (Minimum saldo awal adalah 50.000): '))
    if (saldo<50000) :
        print('Mohon maaf, saldo awal yang anda masukkan belum mencukupi batas minimal')
        saldo = int(input('Masukkan kembali saldo awal anda (Minimum saldo awal adalah 50.000): '))


# Menampilkan kembali data-data yang sudah dimasukkan
os.system('cls' if os.name == 'nt' else 'clear')
print('Berikut adalah data-data pribadi anda!')
scrolling_text(f'Nama Lengkap: {nama_lengkap}')
scrolling_text(f'Tanggal Lahir: {tanggal_lahir}')
scrolling_text(f'PIN : {pin}')
scrolling_text(f'Saldo Awal : {saldo:,}'.replace(',', '.'))


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
    counter = 3
    status_pin_masuk = False
    while (counter>= 0) and (status_pin_masuk == False) :
        pin_masuk = str(input('Masukkan PIN anda: '))
        if (pin_masuk == pin) :
            status_pin_masuk = True
            print('Anda berhasil masuk')
        else :
            counter -= 1
            (f'PIN yang dimasukkan salah. Silakan coba lagi. Anda memiliki {counter} kesempatan lagi')
        if (counter == 0) :
            print('Akun anda telah dikunci. Silahkan atur ulang PIN anda.')
            print('Silakan konfirmasi kembali data pribadi anda.')
            nama_lengkap_konfirmasi = str(input('Nama Lengkap: '))
            tanggal_lahir_konfirmasi = str(input('Tanggal Lahir: '))
            if (nama_lengkap == nama_lengkap_konfirmasi) and (tanggal_lahir_konfirmasi == tanggal_lahir) :
                status_pin = False 
                while (status_pin == False) :
                    pin = str(input('Masukkan PIN baru anda: '))
                    pin_konfirmasi = str(input('Konfirmasikan kembali PIN anda: '))
                    if (pin == pin_konfirmasi) :
                        status_pin = True
                        print('PIN berhasil diubah!')
                        counter = 3
                    else :
                        print('PIN anda salah!')
                        
    # Menampilkan menu yang bisa dipilih
    os.system('cls' if os.name == 'nt' else 'clear')     
    print('SILAHKAN PILIH MENU TRANSAKSI YANG ANDA INGINKAN!')
    print('1. Informasi Saldo')
    print('2. Penarikan Tunai')
    print('3. Transfer')
    print('4. Voucher Isi Ulang')
    print('5. Pembayaran')
    print('6. Ganti PIN')
    print('7. E-Money')
    print('8. Pembelian')
    
    pilihan = int(input('Masukkan menu yang anda inginkan: '))
    os.system('cls' if os.name == 'nt' else 'clear')     

    # Masuk ke menu-menu yang disediakan 
    transaksi = True 
    while ((pilihan == 0) or (pilihan == 1) or (pilihan == 2) or (pilihan == 3) or (pilihan == 4) or (pilihan == 5) or (pilihan == 6) or (pilihan == 7) or (pilihan == 8)) and transaksi == True:
        if (pilihan == 0) :
            print('SILAHKAN PILIH MENU TRANSAKSI YANG ANDA INGINKAN!')
            print('1. Informasi Saldo')
            print('2. Penarikan Tunai')
            print('3. Transfer') 
            print('4. Voucher Isi Ulang')
            print('5. Pembayaran')
            print('6. Ganti PIN')
            print('7. E-Money')
            print('8. Pembelian')
            
            pilihan = int(input('Masukkan menu yang anda inginkan: '))
            os.system('cls' if os.name == 'nt' else 'clear')  
               
        elif (pilihan == 1) :
            print('HARAP MENUNGGU')
            print('TRANSAKSI ANDA SEDANG DIPROSES')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')            
            print('SALDO REKENING ANDA')
            print(f'Rp {saldo:,}'.replace(',', '.'))
            print('')
            print('Lanjut Transaksi?')
            print('1. Ya')
            print('2. Tidak')
            lanjut = int(input())
            if lanjut == 1:
                pilihan = 0
            else:
                transaksi = False
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
                    print('Anda telah berhasil menarik Rp 50.000')
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
                    print('Anda telah berhasil menarik Rp 200.000')
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
                    print('Anda telah berhasil menarik Rp 500.000')
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
                    print('Anda telah berhasil menarik Rp 1.000.000')
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
                    print('(DALAM KELIPATAN RP 50.000)')
                    print('MAKSIMAL RP 1.250.000')
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
                        status_tarik = True
                
                if status_tarik == True:
                    saldo -= tunai
                    os.system('cls' if os.name == 'nt' else 'clear')   
                    print(f'Anda telah berhasil menarik Rp {tunai:,}'.replace(',', '.'))
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
                print(f'JUMLAH            : {tunai:,}'.replace(',', '.'))
                print(f'SISA SALDO        : {saldo:,}'.replace(',', '.'))
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
                transaksi = False
            os.system('cls' if os.name == 'nt' else 'clear')   
            
        elif (pilihan == 3) :
            print('ATM TRANSFER')
            print('MASUKKAN KODE BANK DAN')
            print('NOMOR REKENING TUJUAN')
            print('No. Kode Bank Diikuti Oleh No. Rek Tujuan')
            print('3 nomor diawal kode bank diikuti dengan 5 nomor rekening bank')
            print('Cth. 42612345')

            print('Apakah anda ingin melihat kode bank terlebih dahulu (y/n)?')
            cek_kode_bank = str(input(''))
            
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

                print('Transaksi Akan Dilanjutkan')

            print('ATM TRANSFER')
            print('MASUKKAN KODE BANK DAN')
            print('NOMOR REKENING TUJUAN')
            print('No. Kode Bank Diikuti Oleh No. Rek Tujuan')
            print('3 nomor diawal kode bank diikuti dengan 5 nomor rekening bank')
            print('Cth. 00112345')

            status_transfer = 'n'
            while (status_transfer == 'n') :
                rekening_tujuan = str(input('Nomor Rekening: '))
                kode_bank = rekening_tujuan[:3]
                nama_penerima = str(input('Nama Penerima: '))
                nomimal_transfer = int(input('Masukkan Jumlah Nominal Yang  Akan Ditransfer: '))
                while (nomimal_transfer>saldo) :
                    print('MOHON MAAF, SALDO ANDA TIDAK MENCUKUPI')
                    nomimal_transfer = int(input('Masukkan Kembali Nominal  Yang Akan Ditransfer: '))

                print('--------------------------------')
                print('HARAP TUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')
                print('--------------------------------')

                print('---------------------------------------------------')
                print('TRANSFER ATM')
                print(f'Bank            : {kumpulan_bank[kode_bank]}')
                print(f'Tujuan          : {rekening_tujuan}')
                print(f'Penerima        : {nama_penerima}')
                print(f'Jumlah Transfer : {nomimal_transfer:,}'.replace(',', '.'))
                print('---------------------------------------------------')

                status_transfer= str(input(('Apakah data sudah sesuai (y/n)?    :')))
                if (status_transfer == 'y') :
                    print('HARAP TUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')

                    print('TRANSAKSI TELAH SELESAI')
                    print('PERLU TRANSAKSI YANG LAIN?')

                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                    else :
                        pilihan = 10
        # elif (pilihan == 4) :
        # elif (pilihan == 5) :
        # elif (pilihan == 6) :
        # elif (pilihan == 7) :
        # elif (pilihan == 8) :
