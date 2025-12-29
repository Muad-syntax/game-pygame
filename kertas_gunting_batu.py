import random
import time


def print_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(0.05)
    print("\n")

def game():
    choices = ["batu", "kertas", "gunting"]
    print_slow("Selamat datang di Kertas, Gunting, Batu")
    print_slow("Aturannya sederhana: \nBatu menghancurkan Gunting, Gunting memotong kertas, Kertas, membungkus Batu")
    print_slow("Ayo mulai Permainannya")

    while True:
        print_slow("Apa pilihan anda? (kertas/gunting/batu):")
        player_choice = input().lower()

        if player_choice not in choices:
            print_slow("Pilihan tidak sah. Silahkan di ulang.")
            continue

        print_slow("Pilihanmu " + player_choice + ". Sekarang ")
        time.sleep(1)

        computer_choice = random.choice(choices)
        print_slow("Saya memilih " + computer_choice + ".")

        if player_choice == computer_choice:
            print_slow("hasilnya seri")
        elif (player_choice == "batu" and computer_choice == "gunting") or \
             (player_choice == "gunting" and computer_choice == "kertas") or \
             (player_choice == "kertas" and computer_choice == "batu"):
            print_slow("Kamu Menang!")
        else:
            print_slow("Saya Menang!")

        print_slow("Apakah kamu ingin bermain lagi? (yes/no)")
        play_again = input().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    game()