import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Activity1Number1 {
      public static void main(String[] args) throws IOException {
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Send a message or call?(1/2): ");
        int choice = Integer.parseInt(scan.readLine());
        
        switch (choice) {
            case 1: {
                System.out.print("Enter a message: ");
                String textMessage = scan.readLine();
                System.out.print("Enter a number: ");
                long contactNumber = Long.parseLong(scan.readLine());
                SendMessage(textMessage,contactNumber);
                break;
            }
            case 2: {
                System.out.print("Enter a number: ");
                long contact = Long.parseLong(scan.readLine());
                call(contact);
                break;
            }
            default: {
                System.out.print("Enter a valid number: ");
            }
          
         }
    }
    public static void SendMessage(String textMessage, long contactNumber){
        System.out.println(textMessage + " is being sent to " + contactNumber);
    }

    public static void call(long contactNumber){
        System.out.println("You are calling " + contactNumber);
    }

}