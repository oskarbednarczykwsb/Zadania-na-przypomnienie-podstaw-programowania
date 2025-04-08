end = True

def srednia():
    grades = []
    quantity = int(input("Podaj liczbę ocen:\n"))
    for i in range(1, quantity + 1):
        while True:
            grade = float(input(f"Podaj ocenę nr {i}:\n"))
            if  1<= grade <= 6:
                grades.append(grade)
                break
            else:
                print("Podano nieprawidłową ocenę. Wprowadź ocenę w zakresie 1-6.")
    average = sum(grades) / quantity
    print(f"Średnia: {average}")
    
    if average >= 3.0:
        print("Uczeń zdał.")
    else:
        print("Uczeń nie zdał.")
                  

while(end):
    choice = input("Wybierz operację:\nA.Program średnia\nB.Zakończenie programu\n")
    if choice.title() == 'B':
        end = False
    elif choice.title() == 'A':
        srednia()