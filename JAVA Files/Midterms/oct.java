import java.io.*;

public class oct {
    public static void main(String[] args) throws IOException {
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
        

        System.out.print("Enter Octal Value: ");
        String num = scan.readLine();
        
        int dec = Integer.parseInt(num, 8);
        String hex = Integer.toHexString(dec).toUpperCase();
        
       
        System.out.print(hex);
        scan.close();


    }
}