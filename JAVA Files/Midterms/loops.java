import java.io.*;

public class loops {
    
    public static void main(String[] args) throws IOException{
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));

        // System.out.print("Enter Starting Number: ");
        // int start=Integer.parseInt(scan.readLine());

        // System.out.print("Enter rows: ");
        // int rows=Integer.parseInt(scan.readLine());

        // for(int i=1;i<=rows;i++){
        //     for(int j=1;j<=i;j++){
        //         System.out.print(start);
        //     }
        //     start++;
        //     System.out.println();
        // }

        // System.out.print("Enter rows: ");
        // int num=Integer.parseInt(scan.readLine());

        // for(int i=1;i<=rows;i++){
        //     for(int j=1;j<=rows;j++){
        //         if (i == 1 || i == num || j == 1 || j == num ) {
        //             System.out.print("#");
        //         } else {
        //             System.out.print(" ");
        //         }
        //     }
        //     System.out.println();
        // }
            System.out.print("Enter decimal number: ");
            int num=Integer.parseInt(scan.readLine());
            int rem=0;
            String output="";
            char[] hex= {'0', '1', '2', '3', '4','5', '6', '7', '8','9','A','B','C','D','E','F'};
            do {
                rem = num % 16;
                output = hex[rem] + output;
                num /= 16;
            } while (num > 0);
    
            System.out.println("Hexa: " + output);
        
        
    }
}
    