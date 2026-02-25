//Day 1: Secret Entrance
//input: sequence of rotations ``[L/R] + steps + \n``
//Safe password rotating 0 to 99
//Starting pointing from 50
//Actual password: the number of times the dial is left pointing at 0 after any rotation in the sequence

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Safe {
    private String[] input;
    private static int password = 0;
    private static int currentNumber = 50;

    public Safe(String[] input, int password, int currentNumber){
        this.input = input;
    }

    public boolean isOpened(int currentNumber){
        return currentNumber == 0;
    }

    public void updateCurrentNumber(String nthInput){
        char first = nthInput.charAt(0);
        int num = Integer.parseInt(nthInput.substring(1));
        if (first == 'L'){
            currentNumber = ((currentNumber - num) % 100 + 100) % 100;
        }
        else {
            currentNumber = (currentNumber + num) % 100;
        }
    }

    public void incrementPassword(){
        password++;
    }

    public int getCurrentNumber(){
        return currentNumber;
    }

    public int getPassword(){
        return password;
    }

    public static void main(String[] args) {
        List<String> lines = new ArrayList<>();
        try (Scanner scanner = new Scanner(System.in)){
            while (scanner.hasNextLine()) {
            String line = scanner.nextLine().trim();
            if (!line.isEmpty()) lines.add(line);
            }
        }
        String[] input = lines.toArray(new String[0]);
        Safe safe = new Safe(input, 0 ,50);
        
        for (String line: input){
            safe.updateCurrentNumber(line);
            if (safe.isOpened(safe.getCurrentNumber())){
                safe.incrementPassword();
        }
        }

        System.out.println(safe.getPassword());
    }
}

//main loop: check if it isOpened

