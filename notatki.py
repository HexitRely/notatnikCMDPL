# Aplikacja do notatek

notes = {}

def dodaj_notatke():
    tytul = input("Podaj tytuł notatki: ")
    tresc = input("Podaj treść notatki: ")
    notes[tytul] = tresc
    print("Notatka dodana.")

def przegladaj_notatki():
    if not notes:
        print("Brak notatek do przeglądania.")
    else:
        print("Dostępne notatki:")
        for tytul in notes.keys():
            print(tytul)
        wybor = input("Podaj tytuł notatki do przeglądania: ")
        if wybor in notes:
            print(f"Tytuł: {wybor}")
            print(f"Treść: {notes[wybor]}")
        else:
            print("Brak notatki o podanym tytule.")

def main():
    while True:
        print("Wybierz opcję:")
        print("1. Dodaj notatkę")
        print("2. Przeglądaj notatki")
        print("3. Zakończ")

        wybor = input("Twój wybór: ")

        if wybor == '1':
            dodaj_notatke()
        elif wybor == '2':
            przegladaj_notatki()
        elif wybor == '3':
            print("Aplikacja zostanie zakończona.")
            break
        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()
