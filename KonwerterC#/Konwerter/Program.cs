using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.WriteLine("Wybierz operację:\nC.Przeliczanie na stopnie Celsjusza.\nF.Przeliczanie na stopnie Fahrenheita \nE.Zakończenie programu\n");
            string choice = Console.ReadLine().ToUpper();

            if (choice == "E") break;

            Console.WriteLine("Podaj temperaturę:");
            double temp = double.Parse(Console.ReadLine());

            if (choice == "C")
                Console.WriteLine($"Temperatura po konwersji wynosi {(temp - 32) / 1.8} stopni Celsjusza.");
            else if (choice == "F")
                Console.WriteLine($"Temperatura po konwersji wynosi {temp * 1.8 + 32} stopni Fahrenhaita.");
            else
                Console.WriteLine("Podano nieprawidłową opcję!");
        }
    }
}