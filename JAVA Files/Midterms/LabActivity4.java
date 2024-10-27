import java.io.*;

public class LabActivity4 {
    public static void main(String[] args) throws IOException {
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("\nActivity 1");
        System.out.print("Enter Starting Number: ");
        int start=Integer.parseInt(scan.readLine());

        System.out.print("Enter rows: ");
        int rows=Integer.parseInt(scan.readLine());

        for(int i=rows;i>=1;i--){
            for(int j=1;j<=i;j++){
                System.out.print(start);
            }
            start--;
            System.out.println();
        }

        System.out.println("\nActivity 2");
        for(int i=1;i<=11;i++){
            for(int j=1;j<=10;j++){
                if(i==1 || j==12-i)
                    System.out.print("*");
                else 
                    System.out.print(" ");

                
            }
           
            System.out.println();
        }

        System.out.println("\nActivity 3");
        for (int i = 1; i <= 4; i++) {
            for (int a = 1; a <= 4- i; a++) {
                System.out.print(" ");
            }

            for (int j = 1; j <= i; j++) {             
                if (j==1 || j==i)
                    System.out.print( "* " );
                else
                    System.out.print("  " );
            }
            System.out.println();
        }

        for(int x=3;x>=1;x--)
        {
            for (int b = 1; b <= 4-x; b++) {
                System.out.print(" ");
            }

            for(int y=1;y<=x;y++){
                if (y==1 || x==y)
                    System.out.print( "* " );
                else
                    System.out.print("  " );
            }
            System.out.println();
        }
        
    }
}