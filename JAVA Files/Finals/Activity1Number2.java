import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Activity1Number2 {
      public static void main(String[] args) throws IOException {
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter a string: ");
        String phrase = scan.readLine();
        char[] charArray=phrase.toCharArray();

        int upper=0;
        int lower=0;
        int number=0;
        int special=0;
        
        for (char c : charArray) {
            if(Character.isDigit(c))  {
                number++;
             }
            else if(Character.isUpperCase(c)) {
                upper++;
            }
            else if(Character.isLowerCase(c)) {
                lower++;
            }
            else if(c!=' '){
                special++;

        }
        }
        System.out.println("Uppercase: " + upper);
        System.out.println("Lowercase: " + lower);
        System.out.println("Number: " + number);
        System.out.println("Special Character: " + special);
    
    }
}



