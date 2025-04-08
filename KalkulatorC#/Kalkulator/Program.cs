using System;

class Program
{
    static void Main()
    {
        Console.Write("Podaj liczbę 1: ");
        double number_1 = double.Parse(Console.ReadLine());

        Console.Write("Podajliczbę 2: ");
        double number_2 = double.Parse(Console.ReadLine());

        Console.Write("Wybierz operację:\n1.Dodawanie \n2.Odejmowanie\n3.Mnożenie\n4.Dzielenie\n");
        double choice = double.Parse(Console.ReadLine());

        if (choice == 1)
            Console.WriteLine("Wynik: " + (number_1 + number_2));
        else if (choice == 2)
            Console.WriteLine("Wynik: " + (number_1 - number_2));
        else if (choice == 3)
            Console.WriteLine("Wynik: " + (number_1 * number_2));
        else if (choice == 4)
            Console.WriteLine("Wynik: " + (number_1 / number_2));
        else
            Console.WriteLine("Nieprawidłowa operacja.");
    }
}