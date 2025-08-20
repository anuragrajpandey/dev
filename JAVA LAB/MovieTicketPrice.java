import java.util.Scanner;

public class MovieTicketPrice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        System.out.print("Do you have a membership?: ");
        String member = sc.next();

        double price;

        if (age < 12) {
            price = 5;
        } else if (age >= 65) {
            price = 7;
        } else {
            price = 10;
        }

        if (member.equals("yes")) {
            price -= 2;
        }

        System.out.println("Your ticket price is: $" + price);
        sc.close();
    }
}
