import java.io.*;

public class LabActivity1 {
    
    public static void main(String[] args) throws IOException{
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
        
        System.out.print("Enter your Name: ");
        String name = scan.readLine();
        System.out.print("Enter your Position: ");
        String position = scan.readLine();
        System.out.print("No. of Hours Worked: ");
        int hours = Integer.parseInt(scan.readLine());
        System.out.print("Rate Per Hour: ");
        int rate = Integer.parseInt(scan.readLine());

        System.out.println("\nName: "+ name);
        System.out.println("Position: "+ position);
        System.out.println("No. of Hours: "+ hours);
        System.out.println("Rate: "+ rate);

        Salary(hours, rate);

    }
    public static void Salary(int hours, int rate) {
        double salary = hours * rate;
        double Tax = (salary * 0.12);
        double GSIS =(salary * 0.09);
        double pagibig = 200.00;
        double philheath =(salary * 0.05);
        double totalDeductions= Tax+GSIS+pagibig+philheath;

        System.out.println("\nBasic Salary: " + salary);
        System.out.println("\nTax(12%): " + Tax);
        System.out.println("GSIS: " + GSIS);
        System.out.println("PAG-IBIG: " + pagibig);
        System.out.println("PhilHeath: " + (philheath));

        System.out.println("\nTotal Deductions: " + totalDeductions);
        System.out.println("\nNetpay: " + (salary-totalDeductions));
        System.out.println();
    }
}
