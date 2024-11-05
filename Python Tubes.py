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
            
