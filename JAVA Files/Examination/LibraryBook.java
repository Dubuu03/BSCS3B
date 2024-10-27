
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class LibraryBook {
    static BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));

    private String title;
    private String author;
    private String ISBN;
    private int numberOfPages;
    static int choice;
    private boolean isCheckedOut = false;
    static boolean loop = true;

    public LibraryBook(String bookTitle, String bookAuthor, String bookISBN, int bookNumberOfPages) {
        title = bookTitle;
        author = bookAuthor;
        ISBN = bookISBN;
        numberOfPages = bookNumberOfPages;
        isCheckedOut = false;

    }

    public void checkOutBook() {
        if (!isCheckedOut) {
            isCheckedOut = true;
            System.out.println(title + " by " + author + " is checked out\n");
        } else {
            System.out.println(title + " by " + author + " is already checked out\n");
        }
    }

    public void returnBook() {
        if (isCheckedOut) {
            isCheckedOut = false;
            System.out.println(title + " by " + author + "  is returned\n");
        } else {
            System.out.println(title + " by " + author + " was not checked out\n");
        }
    }

    public void displayBookInfo() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("ISBN: " + ISBN);
        System.out.println("Number of Pages: " + numberOfPages);
        if (isCheckedOut == true) {

        }
        System.out.println("Checked Out: " + isCheckedOut);
        System.out.println();
    }

    public static void displayChoices() {
        System.out.println("1| Checkout ");
        System.out.println("2| Return ");
        System.out.println("3| Display ");
        System.out.println("4| Exit ");
    }

    public static void main(String[] args) throws IOException {

        LibraryBook book = new LibraryBook("Diary of a Wimpy Kid", "Jeff Kinney3", " 978-1439582633", 103);

        while (loop) {
            displayChoices();
            System.out.print("Enter a number: ");
            choice = Integer.parseInt(scan.readLine());
            System.out.println();

            switch (choice) {
                case 1:
                    book.checkOutBook();
                    break;
                case 2:
                    book.returnBook();
                    break;
                case 3:
                    book.displayBookInfo();
                    break;
                case 4:
                    System.out.println("Completed...");
                    loop = false;
                    break;
                default:
                    System.out.println("Enter a correct number");
                    break;
            }
        }

    }

}
