import java.io.BufferedReader;
import java.io.InputStreamReader;

public class CoffeeHaven {

     public static void main (String[] args) throws Exception{
        BufferedReader scan = new BufferedReader (new InputStreamReader(System.in));
        boolean askUser = true;
        double totalCost = 0.0;

        System.out.println("\nWelcome to Coffee Haven!!"); 
        displayMenu();
        while (askUser) {
            totalCost += displaySwitch();
            System.out.print("\nWould you like to add more items to your order? (yes/no): ");
            String answer = scan.readLine();

            if (answer.equalsIgnoreCase("yes")) {
                askUser = true;
                displayMenu();
            } else {
                askUser = false;
                displayOrderSummary(totalCost);

                System.out.print("\n\nEnter amount of payment: ");
                double totalPaid = Integer.parseInt(scan.readLine());
                double change = Change(totalPaid, totalCost);
                System.out.println("\nYour change: PHP " + change);
                System.out.println("\nThank you for ordering at Coffee Haven!\n" );
            }
           
        }
     }

     public static void displayMenu(){
        System.out.println("\nMenu:\n"); 
        System.out.println("1. Espresso - PHP 140.00"); 
        System.out.println("2. Latte - PHP 150.00"); 
        System.out.println("3. Cappuccino - PHP 160.00"); 
        System.out.println("4. Americano - PHP 145.00"); 
        System.out.println("5. Mocha - PHP 170.00"); 
        System.out.println("6. Pastries:"); 
        System.out.println("    a. Croissant - PHP 100.00"); 
        System.out.println("    b. Blueberry Muffin - PHP 120.00"); 
        System.out.println("    c. Chocolate Chip Cookie - PHP 90.00"); 
        System.out.println("7. Snacks:"); 
        System.out.println("    a. Mixed Nuts - PHP 100.00"); 
        System.out.println("    b. Granola Bar - PHP 85.00"); 
        System.out.println("    c. Yogurt Parfait - PHP 110.00"); 
            
       
     }
     public static double displaySwitch() throws Exception{
        BufferedReader scan = new BufferedReader (new InputStreamReader(System.in));
        int num;
        double itemCost = 0.0;
        String orderName="";
        
        System.out.print("\nPlease enter the number of the item you'd like to order: ");
        int order = Integer.parseInt(scan.readLine());
        
        switch (order) {
                    case 1:
                    System.out.print("How many Espresso(s)  would you like? ");
                    num = Integer.parseInt(scan.readLine());
                    itemCost = 140.00 * num;
                    System.out.println("\nYou've added "+ num +" Espresso(s)  on your order.");
                        break;

                    case 2:
                    System.out.print("How many Latte(s) would you like? ");
                    num = Integer.parseInt(scan.readLine());
                    itemCost = 150.00 * num;
                    System.out.println("\nYou've added "+ num +" Latte(s) on your order.");
                        break;
                        
                    case 3:
                    System.out.print("How many Cappuccino(s) would you like? ");
                    num = Integer.parseInt(scan.readLine());
                    itemCost = 160.00 * num;
                    System.out.println("\nYou've added "+ num +" Cappuccino(s) on your order.");
                        break;
        
                    case 4:
                    System.out.print("How many Americano(s)  would you like? ");
                    num = Integer.parseInt(scan.readLine());
                    itemCost = 145.00 * num;
                    System.out.println("\nYou've added "+ num +" Americano(s)  on your order.");
                            break;
                    case 5:
                    System.out.print("How many Mocha(s) would you like? ");
                    num = Integer.parseInt(scan.readLine());
                    itemCost = 170.00 * num;
                    System.out.println("\nYou've added "+ num +" Mocha(s) on your order.");
                            break;    
                    case 6:
                        System.out.println("    a. Croissant - PHP 100.00"); 
                        System.out.println("    b. Blueberry Muffin -PHP 120.00"); 
                        System.out.println("    c. Chocolate Chip Cookie - PHP 90.00"); 
                        System.out.print("\nWhat Pastries do you like?: ");
                        String pastry = scan.readLine();

                        switch (pastry) {
                            case "a":
                            System.out.print("How many Croissant(s)  would you like? ");
                            num = Integer.parseInt(scan.readLine());
                            itemCost = 100.00 * num;
                            System.out.println("\nYou've added "+ num +" Croissant(s) on your order.");
                                break;

                            case "b":
                            System.out.print("How many Blueberry Muffin(s)  would you like? ");
                            num = Integer.parseInt(scan.readLine());
                            itemCost = 120.00 * num;
                            System.out.println("\nYou've added "+ num +" Blueberry Muffin(s) on your order.");
                                break;

                            case "c":
                            System.out.print("How many Chocolate Chip Cookie(s)  would you like? ");
                            num = Integer.parseInt(scan.readLine());
                            itemCost = 90.00 * num;
                            System.out.println("\nYou've added "+ num +" Chocolate Chip Cookie(s) on your order.");
                                break;
                            default:
                            System.out.println("Enter valid input!\n");
                            System.out.print("\nWhat Pastries do you like?: ");
                            
                        }
                        break;

                    case 7:
                    System.out.println("    a. Mixed Nuts - PHP 100.00"); 
                    System.out.println("    b. Granola Bar - PHP 85.00"); 
                    System.out.println("    c. Yogurt Parfait - PHP 110.00");
                    System.out.print("\nWhat Snacks do you like?: ");
                    String snack = scan.readLine();
 
                    switch (snack) {
                        case "a":
                        System.out.print("How many Mixed Nuts  would you like? ");
                        num = Integer.parseInt(scan.readLine());
                        itemCost = 100.00 * num;
                        System.out.println("\nYou've added "+ num +" Mixed Nuts on your order.");
                            break;

                        case "b":
                        System.out.print("How many Granola Bar(s)  would you like? ");
                        num = Integer.parseInt(scan.readLine());
                        itemCost = 85.00 * num;
                        System.out.println("\nYou've added "+ num +" Granola Bar(s) on your order.");
                            break;

                        case "c":
                        System.out.print("How many Yogurt Parfait(s)  would you like? ");
                        num = Integer.parseInt(scan.readLine());
                        itemCost = 110.00 * num;
                        System.out.println("\nYou've added "+ num +" Yogurt Parfait(s) on your order.");
                            break;
                       
                        default:
                        System.out.println("Enter valid input!\n");
                        displaySwitch();
                        
                    }
                        break;

                    default:
                    System.out.println("Enter valid input!");
                    return 0.0;
                }
            return itemCost;
     }

     public static void displayOrderSummary(double totalCost) {
        System.out.print("\nYour order summary:");
        System.out.print("\nTotal cost: PHP " + totalCost);
     }

     public static double Change(double totalPaid, double totalCost) {
        return totalPaid - totalCost;
        
    }
}
