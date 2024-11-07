import os
import time
import random
from datetime import datetime


#Fungsi Fade Text di Terminal
def scrolling_text(text, delay=0.05):
    for i in range(len(text) + 1):
        os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan terminal
        print(text[:i])  # Cetak sebagian teks
        time.sleep(delay)

#Menyambut pengguna
print('SELAMAT DATANG DI BANK TPB SUKSES')
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
                        print('PIN tidak sesuai!')
                        
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
            print(f'RP. {saldo:,}'.replace(',', '.'))
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
                    print('Anda telah berhasil menarik Rp 50.000')
                    print(f'Sisa saldo di rekening anda adalah Rp {saldo:,}'.replace(',', '.'))
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
                    print(f'Sisa saldo di rekening anda adalah Rp {saldo:,}'.replace(',', '.'))
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
                    print(f'Sisa saldo di rekening anda adalah Rp {saldo:,}'.replace(',', '.'))
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
                    print(f'Sisa saldo di rekening anda adalah Rp {saldo:,}'.replace(',', '.'))
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
                    print(f'Sisa saldo di rekening anda adalah Rp {saldo:,}'.replace(',', '.'))
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
                pilihan = 10
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
        elif (pilihan == 4) :
            print('SILAHKAN PILIH')
            print('JENIS PEMBAYARAN/PEMBELIAN')
            print('1. Telepon/HP')
            print('2. Listrik/PLN')
            print('3. Air/PDAM')
            pilih_pembayaran = int(input(''))

            if (pilih_pembayaran == 1) :
                print('SILAHKAN MASUKKAN')
                print('NOMOR PELANGGAN/NOMOR')
                print('TAGIHAN/KODE PEMBAYARAN/NOMOR HANDPHONE ANDA')
                nomor_hp = int(input(''))

                print('HARAP TUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')

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

                nominal_isi_ulang = int(input(''))
                admin_bank = 1000
                total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank

                print('HARAP TUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')

                print('===========PEMBELIAN PULSA PRABAYAR===========')
                print(f'Nomor Handphone     : {nomor_hp}')
                print(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]}')
                print(f'TOTAL               : {total_isi_ulang}')

                print('PROSES TRANSAKSI (y/n)?: ')
                proses_transaksi = str(input(''))

                if (proses_transaksi == 'y') and (saldo>=total_isi_ulang) :
                    print('HARAP TUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')

                    print('TRANSAKSI BERHASIL')
                    print('BERIKUT ADALAH STRUK ANDA')

                    print('=====================BANK TPB SUKSES======================')
                    print('=================PEMBELIAN PULSA PRABAYAR=================')

                    print(f'Nomor Handphone     : {nomor_hp}')
                    print(f'Voucher Reff        : {random.randint(10000000000,99999999999)}')
                    print(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]}')
                    print(f'TOTAL               : {total_isi_ulang}')

                    print('=========Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1=======')
                    print('===========PROVIDER BERKOM MENYATAKAN STRUK INI===========')
                    print('=============SEBAGAI BUKTI PEMBAYARAN YANG SAH============')

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
                    else :
                        pilihan = 10
                else :
                    print('MOHON TUNGGU SEBENTAR')
                    print('ANDA AKAN DIALIHKAN KE MENU UTAMA')
                    pilihan = 0
            elif (pilih_pembayaran == 2) :
                print('MASUKKAN NOMOR METER ANDA')
                nomor_meter     = int(input(''))
                id_pelanggan    = random.randint(100000000000,999999999999)

                print('HARAP TUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')

                print('===========PEMBELIAN LISTRIK PRABAYAR===========')
                print(f'Nomor Meter         : {nomor_meter}')
                print(f'IDPEL               : {id_pelanggan}')
                print(f'Nama                : {nama_lengkap}')
                print(f'Tarif/Daya          : R1M / 900 VA')

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

                nominal_isi_ulang = int(input(''))
                admin_bank = 1000
                total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank

                if (saldo>=total_isi_ulang) :
                    print('HARAP TUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')

                    print('TRANSAKSI TELAH BERHASIL')
                    print('BERIKUT ADALAH STRUK ANDA')

                    print('=====================BANK TPB SUKSES======================')
                    print('============STRUK PEMBELIAN LISTRIK PRABAYAR==============')
                    print(f'Nomor meter         : {nomor_meter}')
                    print(f'IDPEL               : {id_pelanggan}')
                    print(f'Nama Lengkap        : {daftar_pembelian[nominal_isi_ulang]}')
                    print(f'Total Bayar         : {total_isi_ulang}')
                    print(f'Stroom/Token        : {random.randint(1000,9999)}, {random.randint(1000,9999)}, {random.randint(1000,9999)}, {random.randint(1000,9999)}')
                    print(f'Admin Bank          : {admin_bank}')
                    print('=========Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1=======')
                    print('=================PLN MENYATAKAN STRUK INI=================')
                    print('=============SEBAGAI BUKTI PEMBAYARAN YANG SAH============')

                    print('APAKAH ANDA MAU MELAKUKAN TRANSAKSI LAIN?')
                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                    else :
                        pilihan = 10
                else :
                    print('MOHON MAAF SALDO ANDA TIDAK MENCUKUPI')
                    print('APAKAH ANDA MAU MELAKUKAN TRANSAKSI LAIN?')
                    
                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                    else :
                        pilihan = 10
            elif (pilih_pembayaran == 3) :
                print('MASUKKAN KODE PERUSAHAAN')
                print('DIIKUTI NOMOR PELANGGAN ANDA')
                print('CONTOH')
                print('Kode Perusahaan  : 1300')
                print('No Pelanggan     : 1234567890')
                print('Tekan            : 13001234567890')

                status_kode = str(input('Apakah anda ingin melihat daftar kode air minum/PDAM (y/n)? ')))

                kode_perusahaan = {
                    452 : 'PAM KOTA BOGOR'   , 453 : 'PAM KOTA CIREBON',
                    456 : 'PAM KOTA CIANJUR' , 458 : 'PAM KOTA SUBANG' ,
                    465 : 'PAM KOTA KUNINGAN', 476 : 'PAM KOTA CILEGON',
                    480 : 'PAM KOTA SUMEDANG', 489 : 'PAM KOTA DEPOK'  ,
                    492 : 'PAM KOTA SUKABUMI', 499 : 'PAM KOTA BANDUNG',
                }
                while (status_kode == 'y') :
                    print('DAFTAR KODE PERUSAHAAN')
                    print('PAM KOTA BOGOR               452')
                    print('PAM KOTA CIREBON             453')
                    print('PAM KAB CIANJUR              456')
                    print('PAM KAB SUBANG               458')
                    print('PAM KAB KUNINGAN             465')
                    print('PAM KOTA CILEGON             476')
                    print('PAM KAB SUMENDANG            480')
                    print('PAM KOTA DEPOK               489')
                    print('PAM KOTA SUKABUMI            494')
                    print('PAM KAB BANDUNG              499')
                    status_kode = str(input('Apakah anda ingin melanjutkan transaksi (y/n)? '))

                print('MASUKKAN KODE PERUSAHAAN')
                print('DIIKUTI NOMOR PELANGGAN ANDA')
                print('CONTOH')
                print('Kode Perusahaan  : 1300')
                print('No Pelanggan     : 1234567890')
                print('Tekan            : 13001234567890') 
                nomor_pelanggan = str(input(''))
                tagihan       = random.randint(0,saldo)
                biaya_admin   = 0
                total_bayar   = tagihan + biaya_admin
                 
                print('HARAP TUNGGU')
                print('TRANSAKSI ANDA SEDANG DIPROSES')

                print('KONFIRMASI PEMBAYARAN')
                print(f'TAGIHAN {kode_perusahaan[nomor_pelanggan[:3]]}')
                print(f'No Pelanggan     : {nomor_pelanggan[3:]}')
                print(f'Nama             : {nama_lengkap}')
                print(f'Tagihan          : {tagihan}')
                print(f'Biaya admin      : {biaya_admin}')
                print(f'Total Bayar      : {total_bayar}')

                konfirmasi_pembayaran = str(input('Ingin Melanjutkan Pembayaran (y/n)? '))
                if(konfirmasi_pembayaran == 'y') and (saldo>=total_bayar):
                    print('HARAP TUNGGU')
                    print('TRANSAKSI ANDA SEDANG DIPROSES')

                    print('TRANSAKSI TELAH BERHASIL')
                    print('Berikut adalah struk anda')
                    print('=====================BANK TPB SUKSES======================')
                    print('================STRUK PEMBAYARAN AIR/PDAM===============')
                    print(f'Nomor meter         : {nomor_pelanggan}')
                    print(f'Nama                : {nama_lengkap}')
                    print(f'Tagihan          : {tagihan}')
                    print(f'Biaya admin      : {biaya_admin}')
                    print(f'Total Bayar      : {total_bayar}')
                    print('=========Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1=======')
                    print('=================PDAM MENYATAKAN STRUK INI=================')
                    print('=============SEBAGAI BUKTI PEMBAYARAN YANG SAH============')

                    print('APAKAH ANDA INGIN MELANJUTKAN TRANSAKSI (y/n)?')
                    lanjut_transaksi = str(input(''))

                    if (lanjut_transaksi == 'y') :
                        pilihan = 0
                    else :
                        pilihan = 10
                elif (konfirmasi_pembayaran == 'y') and (saldo<total_bayar) :
                    print('MOHON MAAF SALDO ANDA TIDAK MENCUKUPI')
                    print('APAKAH ANDA MAU MELAKUKAN TRANSAKSI LAIN?')
                    
                    status_transaksi = str(input('Konfirmasi (y/n): '))
                    if (status_transaksi == 'y') :
                        pilihan = 0
                    else :
                        pilihan = 10
                else :
                    print('MOHON TUNGGU SEBENTAR')
                    print('ANDA AKAN DIALIHKAN KE MENU UTAMA')
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
