##employee wages based on items sold

import java.util.*;

class Main {
    public static void main(String[] args) {
        int[] itemsSold = {48,50,37,62,38,70,55,37,64,60};

        int min = itemsSold[0];
        int max = itemsSold[0];
        double sum = 0;
        int numEmployees = itemsSold.length;

        for(int num : itemsSold){
            if(num < min) min = num;
            if(num > max) max = num;
            sum += num;
        }

        double bonusThreshold = (sum - min - max) / (numEmployees - 2);
        System.out.println("Min: " + min + ", Max: " + max + ", Bonus threshold: " + bonusThreshold);

        double[] wages = new double[numEmployees];
        int fixedWage = 10;
        double perItemWage = 1.5;

        for(int i = 0; i < numEmployees; i++){
            double pay = fixedWage + perItemWage * itemsSold[i];
            if(itemsSold[i] >= bonusThreshold){
                pay *= 1.1;  // 10% bonus
            }
            wages[i] = Math.round(pay*100.0)/100.0;
        }

        System.out.println(Arrays.toString(wages));
    }
}
