public class Developer extends Employee {
    private int overtimeHours;
    private double overtimePayRate;

    public Developer(String name, int id, double salary, int overtimeHours, double overtimePayRate) {
        super(name, id, salary);
        this.overtimeHours = overtimeHours;
        this.overtimePayRate = overtimePayRate;

    }

    public double calculateSalary() {
        return Salary + (overtimeHours * overtimePayRate);
    }

    public String getDetails() {
        return super.getDetails() + "\nOvertime Hours:" + overtimeHours + " \nOvertime Pay Rate:" + overtimePayRate;
    }
}
