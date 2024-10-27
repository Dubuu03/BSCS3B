import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BankAccount {
    static String accountNumber = "1020304050";
    static double currentBalance = 500;
    static BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));

    public static void deposit() throws IOException {
        System.out.print("Enter deposit amount: ");
        double deposit = Double.parseDouble(scan.readLine());
        currentBalance += deposit;
        System.out.println("Deposit Successful");
    }

    public static void withdraw() throws IOException {
        System.out.print("Enter amount to withdraw: 3");
        double withdraw = Double.parseDouble(scan.readLine());

        if (withdraw > currentBalance) {
            System.out.println("Insufficient Balance");
        } else {
            currentBalance -= withdraw;
            System.out.println("Withdrawal Successful");
        }
    }

    public static void getBalance() {
        System.out.println("Current balance of " + accountNumber + ": " + currentBalance);
    }

    public static void showOption() {
        System.out.println("1. Deposit");
        System.out.println("2. Withdraw");
        System.out.println("3. Get Balance");
        System.out.println("4. Annual Interest");
        System.out.println("5. Exit");
    }

    public static void main(String[] args) throws IOException {

        boolean check = true;

        while (check) {
            showOption();
            System.out.print("Enter Action: ");
            int action = Integer.parseInt(scan.readLine());

            switch (action) {
                case 1:
                    deposit();
                    break;
                case 2:
                    withdraw();
                    break;
                case 3:
                    getBalance();
                    break;
                case 4:
                    SavingsAccount.calculateAnnualInterest();
                    break;
                case 5:
                    check = false;
                    System.out.println("Transaction Complete");
                    break;
                default:
                    System.out.println("Invalid Action");
                    break;
            }
        }

    }
}

class SavingsAccount extends BankAccount {
    private static double annualInterestRate = 0.02;

    public static void calculateAnnualInterest() {
        double interest = currentBalance * annualInterestRate;
        currentBalance += interest;
        System.out.println("Annual interest: " + interest);
    }
}