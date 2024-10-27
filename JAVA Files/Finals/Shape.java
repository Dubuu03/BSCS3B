import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

abstract class Shape {
    static BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));

    static double area;
    static double perimeter;
    static double base;
    static double height;
    static double width;
    static double length;
    static double a;
    static double b;
    static double c;

    abstract static class Triangle extends Shape {
        public abstract void calculateArea(double base, double height);

        public abstract void calculatePerimeter(double a, double b, double c);
    }

    abstract static class Rectangle extends Shape {
        public abstract void calculateArea(double length, double width);

        public abstract void calculatePerimeter(double length, double width);
    }

    abstract static class Parallelogram extends Shape {
        public abstract void calculateArea(double base, double height);

        public abstract void calculatePerimeter(double a, double b);
    }

    public static void showShapes() {
        System.out.println("1. Triangle");
        System.out.println("2. Rectangle");
        System.out.println("3. Parallelogram");
        System.out.println("4. Exit");
    }

    public static void main(String[] args) throws IOException {
        boolean loop = true;

        while (loop) {
            showShapes();
            System.out.print("Enter Shape: ");
            int choice = Integer.parseInt(scan.readLine());

            switch (choice) {
                case 1:
                    Triangle triangle = new Triangle() {
                        public void calculateArea(double base, double height) {
                            area = 0.5 * base * height;
                            System.out.println("Area of triangle: " + area);
                        }

                        public void calculatePerimeter(double a, double b, double c) {
                            perimeter = a + b + c;
                            System.out.println("Perimeter of triangle: " + perimeter);
                        }
                    };
                    System.out.print("Enter base of triangle: ");
                    base = Double.parseDouble(scan.readLine());
                    System.out.print("Enter height of triangle: ");
                    height = Double.parseDouble(scan.readLine());

                    System.out.print("Enter side 1 of triangle: ");
                    a = Double.parseDouble(scan.readLine());
                    System.out.print("Enter side 2 of triangle: ");
                    b = Double.parseDouble(scan.readLine());
                    System.out.print("Enter side 3 of triangle: ");
                    c = Double.parseDouble(scan.readLine());

                    System.out.println();
                    triangle.calculateArea(base, height);
                    triangle.calculatePerimeter(a, b, c);
                    System.out.println();
                    break;

                case 2:
                    Rectangle rectangle = new Rectangle() {
                        public void calculateArea(double length, double width) {
                            area = length * width;
                            System.out.println("Area of rectangle: " + area);
                        }

                        public void calculatePerimeter(double length, double width) {
                            perimeter = 2 * (length + width);
                            System.out.println("Perimeter of rectangle: " + perimeter);
                        }
                    };
                    System.out.print("Enter length of rectangle: ");
                    length = Double.parseDouble(scan.readLine());
                    System.out.print("Enter width of rectangle: ");
                    width = Double.parseDouble(scan.readLine());

                    System.out.println();
                    rectangle.calculateArea(length, width);
                    rectangle.calculatePerimeter(length, width);
                    System.out.println();
                    break;

                case 3:

                    Parallelogram parallelogram = new Parallelogram() {

                        public void calculateArea(double base, double height) {
                            area = base * height;
                            System.out.println("Area of parallelogram: " + area);
                        }

                        public void calculatePerimeter(double a, double b) {
                            perimeter = 2 * (a + b);
                            System.out.println("Perimeter of parallelogram: " + perimeter);
                        }
                    };
                    System.out.print("Enter base of parallelogram: ");
                    base = Double.parseDouble(scan.readLine());
                    System.out.print("Enter height of parallelogram: ");
                    height = Double.parseDouble(scan.readLine());
                    System.out.print("Enter side 1 of parallelogram: ");
                    a = Double.parseDouble(scan.readLine());

                    System.out.println();
                    parallelogram.calculateArea(base, height);
                    parallelogram.calculatePerimeter(a, base);
                    System.out.println();
                    break;

                case 4:
                    System.out.println("Completed.");
                    loop = false;
                    break;
                default:
                    System.out.println("\nInvalid choice.");
                    break;
            }
        }
    }
}
