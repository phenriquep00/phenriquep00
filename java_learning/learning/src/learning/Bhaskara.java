package learning;

import java.util.Scanner;

public class Bhaskara {

    public static void main(String[] args){

        System.out.println("---------- BHASKARA CALCULATOR ----------");

        Scanner keyboard = new Scanner(System.in);
        System.out.println("a: ");
        double a = keyboard.nextDouble();
        System.out.println("b: ");
        double b = keyboard.nextDouble();
        System.out.println("c: ");
        double c = keyboard.nextDouble();

        double delta = (Math.pow(b, 2)) - (4 * a * c);

        if (delta >= 0) {
            double x1 = (-b + (Math.sqrt(delta))) / (2 * a);
            double x2 = (-b - (Math.sqrt(delta))) / (2 * a);
            System.out.println("Delta is " + delta);
            System.out.println("x1 = " + x1);
            System.out.println("x2 = " + x2);
        } else {
            System.out.println("Delta lower than 0");
        }
    }
}
