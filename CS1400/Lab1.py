class Main {
  /*-------------------------------------------------------------------------
// AUTHOR: JAZMIN CARLOS
// FILENAME: LAB1.JAVA
// SPECIFICATION: CALCULATE AVERAGE OF 3 GIVEN SCORES
// FOR: CS 1400- Lab #1
// TIME SPENT: 10 MINUTES
//-----------------------------------------------------------*/

import java.util.Scanner; 
	// we must have a main method to run the program
	public static void main(String[] args) {

		// create a Scanner object to get input from the keyboard
		//--> 
		Scanner input = new Scanner(System.in); 


		// declare three integer variables to hold the test scores  
		//--> 
		int testA = 0;
		int testB = 0; 
		int testC = 0; 
		
		
		// declare one integer constant to hold the number of tests  
		//--> 
		int numTests = 3; 
		
		
		// declare one double variable to hold the average  
		//--> 
		double testAv = 0.0; 
		

		// Get the Input
		//-->
		System.out.print("Enter the score on the first test: ");
		testA = input.nextInt(); 
		
		System.out.print("Enter the score on the second test: ");
		testB = input.nextInt(); 
		
		System.out.print("Enter the score on the third test: ");
		testC = input.nextInt(); 


		// Calculate the average
		//--> 
		testAv = (testA + testB + testC) / numTests; 


		// Display Results
		//-->
		System.out.println( "The average test score is "+ testAv); 
		
		
		// Close your Scanner object
		//-->
		java.util.Scanner.close();


	}//end main method
}//end Lab1 class

}