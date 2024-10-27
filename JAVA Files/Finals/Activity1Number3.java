import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Activity1Number3 {
    public static void main(String[] args) throws IOException {
        BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter string 1: ");
        String string1 = scan.readLine().toLowerCase();
        System.out.print("Enter string 2: ");
        String string2 = scan.readLine().toLowerCase();

        boolean Anagram =check(string1, string2);
        if(Anagram){
            System.out.println("Strings are the SAME");
        }
        else{
            System.out.println("Strings are the DIFFERENT");
        }
    }
    public static boolean check(String string1, String string2){
        
        if(string1.length()!=string2.length()){
            return false;
        }

        int [] counter1 = new int[256];
        int [] counter2 = new int[256];

        for(int i = 0; i < string1.length(); i++){
            counter1[string1.charAt(i)] ++;
        }
        for (int j=0; j <  string2.length(); j++){
            counter2[string2.charAt(j)]++;
        }

        for(int a=0; a < 256; a++){
            if(counter1[a]!=counter2[a]){
                return false;
            }
        }
        return true;

        
    }
}
