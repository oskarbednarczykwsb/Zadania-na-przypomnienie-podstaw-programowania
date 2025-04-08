end = True

def calc(choice):
    number_1 = int(input("Podaj liczbę 1:\n"))
    number_2 = int(input("Podaj liczbę 2:\n"))
    if choice == 1:
        print(f"Wynik dodawania liczby {number_1} i {number_2} to : {number_1 + number_2}")
    elif choice == 2:
        print(f"Wynik odejmowania liczby {number_1} i {number_2} to : {number_1 - number_2}")
    elif choice == 3:
        print(f"Wynik mnożenia liczby {number_1} i {number_2} to : {number_1 * number_2}")
    elif choice == 4:
        if number_1 == 0 or number_2 == 0:
            print("Nie można dzielić przez 0!")
        else:
            print(f"Wynik dzielenia liczby {number_1} i {number_2} to : {number_1 / number_2}")
    else:
        print("Podano nieprawidłową opcję!")
    
while(end):
    choice = int(input("Wybierz operację:\n1.Dodawanie \n2.Odejmowanie\n3.Mnożenie\n4.Dzielenie\n5.Zakończenie programu\n"))
    if choice == 5:
        end = False
    else:
        calc(choice)