import java.util.Scanner;

class trial {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        
        String [] email=new String[3];
        String [] user=new String[3];
        String [] pass=new String[3]; 
        
        for(int i=0; i<email.length;i++)
        {
            System.out.print("Enter Email " +(i+1)+" : " );
            email[i]=scan.nextLine();

            System.out.print("Enter Username " +(i+1)+" : " );
            user[i]=scan.nextLine();

            System.out.print("Enter Password " +(i+1)+" : " );
            pass[i]=scan.nextLine();
            System.out.println();
        }

        System.out.print("Enter an index (1-3): ");
        int index = scan.nextInt();

        switch (index) {
            case 1:
                System.out.println("Email    : "+ email[0]);
                System.out.println("Username : "+ user[0]);
                System.out.println("Password : "+ pass[0]);
                break;

            case 2:
                System.out.println("Email    : 1"+ email[1]);
                System.out.println("Username : "+ user[1]);
                System.out.println("Password : "+ pass[1]);
                break;

            case 3:
                System.out.println("Email    : "+ email[2]);
                System.out.println("Username : "+ user[2]);
                System.out.println("Password : "+ pass[2]); 
                break;

            default:
            System.out.println("Invalid Index!");
                break;
        }
        System.out.println();
        for (String mail : email) {
            System.out.println(mail);
        }
        
    }
}