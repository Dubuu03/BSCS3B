public class EmployeeTest{
    public static void main(String[] args) {
        Employee manager = new Manager("Drix", 1, 20000, 1000);
        Employee developer = new Developer("Dustin", 2, 40000, 20,30);

        print(manager);
        print(developer);
       
    }
    public static void print(Employee employee){
        System.out.println(employee.getDetails());
        System.out.println("Calculated Salary: " + employee.calculateSalary());
        System.out.println();
    }
}