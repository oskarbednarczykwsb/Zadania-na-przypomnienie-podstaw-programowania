end = True

def przelicznik(choice):
    if choice.title() == 'C': 
        temp = float(input("Podaj temperaturę w stopniach Fahrenheita:\n"))
        change = (temp - 32)/1.8
        print(f"Temperatura po konwersji wynosi {change} stopni Celsjusza.")
    elif choice.title() == 'F':
        temp = float(input("Podaj temperaturę w stopniach Celsjusza:\n"))
        change = temp * 1.8 + 32
        print(f"Temperatura po konwersji wynosi {change} stopni Fahrenhaita.")
    else:
        print("Podano nieprawidłową opcję!")

while(end):
    choice = input("Wybierz operację:\nC.Przeliczanie na stopnie Celsjusza.\nF.Przeliczanie na stopnie Fahrenheita \nE.Zakończenie programu\n")
    if choice.title() == 'E':
        end = False
    else:
        przelicznik(choice)