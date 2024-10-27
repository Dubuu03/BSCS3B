
public class Manager extends Employee {
    private double bonus;

    public Manager(String name,int id,double salary, double bonus){
        super(name, id, salary);
        this.bonus = bonus;
    }

    public double calculateSalary(){
        return Salary+bonus;
    }
    public String getDetails(){
        return super.getDetails()+ "\nBonus:"+ bonus;
    }
}
    
