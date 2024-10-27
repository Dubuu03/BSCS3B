import java.io.*;

public class LabActivity2 {
    public static void main(String[] args) throws IOException{
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
        
        System.out.print("Problem 1: ");
        System.out.print("\nArea or Circumference(1/2): ");
        int calc = Integer.parseInt(scan.readLine());
        System.out.print("Enter Radius: ");
        int rad = Integer.parseInt(scan.readLine());
        
        System.out.print(calc == 1 ? "Area: " + (3.14 * (rad*rad)) : "Circumference: " + (2* 3.14 * rad));
        
        System.out.print("\n\nProblem 2: ");
        System.out.print("\nEnter 4 digit number: ");
        int digit = Integer.parseInt(scan.readLine());
        System.out.print("Enter choice to swap: ");
        int choice = Integer.parseInt(scan.readLine());

        int num1= digit / 1000;
        int num2= (digit/100)%10 ;
        int num3= (digit/10)%10 ;   
        int num4 =  digit%10 ;
        double sum =num1 + num2 + num3 + num4;
        double ave= sum/4;

        System.out.print("\nAverage: "+ ave);
        System.out.println("\nReversed OrdeQr: " + num4+num3+num2+num1);
        
        System.out.print(choice == 1? "Swapping 2nd and 4th: " + num1 + num4 + num3 + num2 
                                    : "Swapping 1st and 3rd: "+ num3 + num2 + num1 + num4);

    }
}
