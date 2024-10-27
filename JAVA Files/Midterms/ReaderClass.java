// import java.util.Scanner;
// import java.io.InputStreamReader;
// import java.io.BufferedReader;
import javax.swing.JOptionPane;

public class ReaderClass {
    public static void main (String[] args) {
        //SCANNER READER CLASS
        // Scanner scan=new Scanner(System.in); 

        // System.out.println("Hello, World!\n" );

        // System.out.print("Enter a name: " );
        // String name=scan.nextLine();
        
        // System.out.print("Enter your age: " );
        // int age=scan.nextInt();
        
        // System.out.println("Your name is " + name + ", and your age is "+ age);

        //BUFFERED READER CLASS
        // BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
        // System.out.print("Enter a name: " );
        // String name=scan.readLine();

        // System.out.print("Enter age: " );
        // int age=Integer.parseInt(scan.readLine());

        // System.out.print("Enter amount of money: " );
        // double pera=Double.parseDouble(scan.readLine());

        // System.out.println("\nYour name is: "+ name);
        // System.out.println("Your age is: "+ age);
        // System.out.println("Your money is: "+ pera);

        //JOPTION PANE READER CLASS
        // String name="";
        // name=JOptionPane.showInputDialog("Enter your name: ");
        // String msg="Hello "+name+"!";
        // JOptionPane.showMessageDialog(null, msg);

        int num1,num2;

        num1=Integer.parseInt(JOptionPane.showInputDialog("Enter First Number: "));
        num2=Integer.parseInt(JOptionPane.showInputDialog("Enter Second Number: "));
        
        int sum=num1+num2;

        JOptionPane.showMessageDialog(null, "Sum: "+sum);

    }
}