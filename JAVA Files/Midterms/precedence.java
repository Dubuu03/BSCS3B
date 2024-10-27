

class precedence {
    public static void main (String[] args) {
        int x=8;
        int y=4;

        System.out.println(x++);
        System.out.println(--x);
        System.out.println(++y);
        System.out.println(x++ - y++ * ++x);
        System.out.println(++y * --x + y++);
        System.out.println(++x + y--);
        System.out.println(++y *--x);
        System.out.println(x-- + --y * y++);
        System.out.println(x);
        System.out.println(y);
  
    }
}