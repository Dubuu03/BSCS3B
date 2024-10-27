// class Main{
//    String language;

//    // a constructor with no parameter
//    Main() {
//       this.language="Java";
//    }
//    // a constructor with a single parameter
//    Main(String language) {
//       this.language= language;
//    }
//    public void getName() { 
//       System.out.println("Programming Language: " + this.language);
//    }
//    public static void main(String[] args) {
//       // call the constructor with no parameter
//       Main obj1 = new Main();
//       // call the constructor with single parameter
//       Main obj2 = new Main("Python");

//       obj1.getName();
//       obj2.getName();
//    }
// }
    
public class Main{
   
   public static void main (String[] args) {
      String S1 = "It's not a bug, it's a feature"; 
      String S2 = "Computers have lots of memory but no imagination"; 
      String S3 = "I just wish my mouth had a backspace key";

      System.out.println(S2.charAt(15)); 
      System.out.println(S1.substring(16));
      System.out.println(S1.length());
      String S4 = S2.substring(23, 29);
      System.out.println(S4);
      String S5 = S3.substring(27, 36);
      System.out.println(S5.concat(S4));
      System.out.println(S4.toUpperCase());
      System.out.println(S1.charAt(7));
      System.out.println(S1.endsWith(S4));
      System.out.println(S2.charAt(S1.length()));
      System.out.println(S2.substring(S1.length(), 33));
      System.out.println(S4.compareTo(S2));
      System.out.println(S2.startsWith(S4));
      char S6 = S1.charAt(2);
      System.out.println(Character.isLetter(S6));
      int S7 = S2.length();
      int S8 = S3.length();
      System.out.println(Math.min(S7, S8));
      char S9 = S3.charAt(0);
      System.out.println(Character.isUpperCase(S9));  

    }
  
}