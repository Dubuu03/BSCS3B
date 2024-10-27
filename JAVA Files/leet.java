import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class leet {
  public static void main(String[] args) throws IOException {
    BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));

    int x=1213;
    
    String str = String.valueOf(x);
    String rev = "";
    for (int i = str.length() - 1; i > -1; i--) {
      rev += str.charAt(i);
    }

    System.err.println(rev);
    System.err.println(str);
  }

}
