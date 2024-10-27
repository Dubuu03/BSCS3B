import java.io.*;

public class 290424 {
    public static void main(String[] args) throws IOException {
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Send a message or call?: ");
        int choice = Integer.parseInt(scan.readLine());
        
        switch (choice) {
            case 1: {
                System.out.print("Enter a message: ");
                String textMessage = scan.readLine();
                System.out.print("Enter a number: ");
                int contactNumber = Integer.parseInt(scan.readLine());
                SendMessage(contactNumber, textMessage);
            }
          
    }
    public static void SendMessage(String textMessage, int contactNumber){
        System.out.println(textMessage + " is being sent to " + contactNumber);
    }

}
}
