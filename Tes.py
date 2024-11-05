import time
import os

def scrolling_text(text, delay=0.05):
    for i in range(len(text) + 1):
        os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan terminal
        print(text[:i])  # Cetak sebagian teks
        time.sleep(delay)


# Contoh penggunaan
scrolling_text("Ini adalah efek mengetik teks.")
