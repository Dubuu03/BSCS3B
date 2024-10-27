
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Problem2 {
    static BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));

    static String phrase;
    static int sum;

    public static void main(String[] args) throws IOException {
        System.out.print("Enter a phrase: ");
        phrase = scan.readLine();

        for (char ch : phrase.toCharArray()) {
            if (Character.isDigit(ch)) {
                sum += Character.getNumericValue(ch);
            }
        }
        System.out.print("Sum of Digits: " + sum);
        System.out.println();
        System.out.println();

        System.out.print("Enter a word: ");
        String input = scan.readLine();

        String[] words = input.split(" ");
        String pigLatin = "";

        for (String word : words) {
            pigLatin += toPigLatin(word) + " ";
        }

        System.out.println("Pig Latin: " + pigLatin.trim());

    }

    public static String toPigLatin(String word) {
        String vowels = "AEIOUaeiou";
        char firstChar = word.charAt(0);

        if (vowels.indexOf(firstChar) != -1) {
            return word + "way";
        }

        int firstVowelIndex = -1;

        for (int i = 0; i < word.length(); i++) {
            if (vowels.indexOf(word.charAt(i)) != -1) {
                firstVowelIndex = i;
                break;
            }
        }
        
        String prefix = word.substring(0, firstVowelIndex);
        String suffix = word.substring(firstVowelIndex);

        return suffix + prefix + "ay";
    }

}
