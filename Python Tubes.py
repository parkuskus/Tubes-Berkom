import os
import time

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
print('Berikut adalah data-data pribadi anda!')
scrolling_text(f'Nama Lengkap: {nama_lengkap}')
scrolling_text(f'Tanggal Lahir: {tanggal_lahir}')
scrolling_text(f'PIN : {pin}')
scrolling_text(f'Saldo Awal : {saldo}')


#Memilih Bahasa pada ATM
print('PILIH BAHASA YANG ANDA INGIN GUNAKAN!')
print('1. Indonesia')
print('2. Inggris')
bahasa = int(input(('Pilih bahasa yang anda ingin gunakan!: ')))

# ATM Bahasa Indonesia
if (bahasa == 1) :
    # Mengecek PIN yang dimasukkan
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
    print('SILAHKAN PILIH MENU TRANSAKSI YANG ANDA INGINKAN!')
    print('1. Informasi Saldo')
    print('2. Penarikan Tunai')
    print('3. Transfer')
    print('4. Voucher Isi Ulang')
    print('5. Pembayaran')
    print('6. Ganti PIN')
    print('7. E-Money')
    print('8. Pembelian')
    
    pilihan = str(input('Masukkan menu yang anda inginkan: '))

    # Masuk ke menu-menu yang disediakan 
    while (pilihan == 0) or (pilihan == 1) or (pilihan == 2) or (pilihan == 3) or (pilihan == 4) or (pilihan == 5) or (pilihan == 6) or (pilihan == 7) or (pilihan == 8) :
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
            
            pilihan = str(input('Masukkan menu yang anda inginkan: '))
        elif (pilihan == 1) :
            print('HARAP MENUNGGU')
            print('TRANSAKSI ANDA SEDANG DIPROSES')
            
            print('SALDO REKENING ANDA')
            print(f'RP. {saldo}')
        elif (pilihan == 2) :   
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

            while (status_transfer == 'n') :
                rekening_tujuan = str(input('Nomor Rekening: '))
                kode_bank = rekening_tujuan[:3]
                nama_penerima = str(input('Nama Penerima: '))
                nomimal_transfer = int(input('Masukkan Jumlah Nominal Yang  Akan Ditransfer: '))
                while (nomimal_transfer<saldo) :
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
                print(f'Jumlah Transfer : {nomimal_transfer}')
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
        elif (pilihan == 4) :
        elif (pilihan == 5) :
        elif (pilihan == 6) :
        elif (pilihan == 7) :
        elif (pilihan == 8) :