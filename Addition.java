// Command Line Argument program that you have to provide input during execution of program.

// e.g java sum 10 20

import java.io.*;

public class Addition {
    public static void main(String args[]) {
        for(int i=0; i<args.length; i++){
            String inputdata = args[i];
            String[] data = inputdata.split(" ");
            int x= Integer.parseInt(data[0]);
            int y= Integer.parseInt(data[1]);
            int z=x+y;

            System.out.println("Sum of x+y = " + z);
        } 
    }
}