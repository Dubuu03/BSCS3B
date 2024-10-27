public class Employee {
    protected String name;
    protected int id;
    protected double Salary;

    public Employee(String name, int id, double Salary) {
        this.name = name;
        this.id = id;
        this.Salary = Salary;
    }

    public double calculateSalary() {
        return Salary;
    }

    public String getDetails() {
        return "Name: " + name + "\nID: " + id + " \nSalary: " + Salary;
    }
}

