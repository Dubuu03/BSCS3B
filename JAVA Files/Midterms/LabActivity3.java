import java.io.*;

public class LabActivity3 {
    public static void main(String[] args) throws IOException {
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));

       
        int bill=0; System.out.print("Enter your Name: ");
        String name = scan.readLine();
        System.out.print("No. of Gallons used: ");
        int gallons = Integer.parseInt(scan.readLine());
        int rem=0;

        if(gallons>50&&gallons<=100){
            rem = gallons-50;
            bill+= 500 + (rem*10);
            System.out.println(bill);
     
        }
        else if(gallons>100&&gallons<=200){
            
           rem = gallons-100;
           bill+= 1000 + (rem*20);
           System.out.println(bill);
     
        }
        else if (gallons>200){
            rem = gallons-200;
            bill+= 2000 + (rem*30);
            System.out.println(bill);
        }
        else{
            System.out.println("Invalid Gallons");
        }

        System.out.println();

        System.out.print("Enter month of birth: ");
        int month = Integer.parseInt(scan.readLine());
        System.out.print("Enter day of birth: ");
        int day = Integer.parseInt(scan.readLine());

        if ((month==12 && day >= 22 && day <= 31) || (month==1 && day >= 1 && day <= 19))
            System.out.print("Capricorn");
        else if ((month==1 && day >= 20 && day <= 31) || (month==2 && day >= 1 && day <= 18))
            System.out.print("Aquarius");
        else if ((month==2 && day >= 19 && day <= 28) || (month==3 && day >= 1 && day <= 20))
            System.out.print("Pisces");
        else if ((month==3 && day >= 21 && day <= 31) || (month==4 && day >= 1 && day <= 19))
            System.out.print("Aries");
        else if ((month==4 && day >= 20 && day <= 30) || (month==5 && day >= 1 && day <= 20))
            System.out.print("Taurus");
        else if ((month==5 && day >= 21 && day <= 31) || (month==6 && day >= 1 && day <= 20))
            System.out.print("Gemini");
        else if ((month==6 && day >= 21 && day <= 30) || (month==7 && day >= 1 && day <= 22))
            System.out.print("Cancer");
        else if ((month==7 && day >= 23 && day <= 31) || (month==8 && day >= 1 && day <= 22))
            System.out.print("Leo");
        else if ((month==8 && day >= 23 && day <= 31) || (month==9 && day >= 1 && day <= 22))
            System.out.print("Virgo");
        else if ((month==9 && day >= 23 && day <= 30) || (month==10 && day >= 1 && day <= 22))
            System.out.print("Libra");
        else if ((month==10 && day >= 23 && day <= 31) || (month==11 && day >= 1 && day <= 21))
            System.out.print("Scorpio");
        else if ((month==11 && day >= 22 && day <= 30) || (month==12 && day >= 1 && day <= 21))
            System.out.print("Gemini");
        else if (month>12 && day>31)
            System.out.print("Invalid Month and Day");
        else if (month>12)
            System.out.print("Invalid Month");
        else
            System.out.print("Invalid Day");
      
    }

}
