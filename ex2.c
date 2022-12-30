#include <stdio.h>

// int main() {
  
//   double testScore = 95.7;
//   int displayScore = 0;

//   displayScore = (int) testScore;


//   // No need to change below here
//   printf("Great work, you got a %d%% on your test\n", displayScore);

// }


// int main() {
  
//   char targetChar;
//   int sourceInt = 99;
//   double sourceDouble = 55.67;

// //   targetChar = (char) sourceInt;
//   targetChar = sourceDouble;


//   // No need to change below here
//   printf("source int %d, source double, %.2f, target %c\n", sourceInt, sourceDouble, targetChar);

// }

// int main() {
  
//   // Variables set for you, do not change here
//   int booksSold = 100;
//   double bookCost = 9.99;
//   double totalSalesValue;

//   // Make your changes here
//   booksSold = booksSold + 200;
//   totalSalesValue = bookCost * booksSold;
//   totalSalesValue = totalSalesValue/2;

//   // Output logic, no need to change this
//   printf("You sold %d books and your take home was $%.2f\n", booksSold, totalSalesValue);
// }

// int main() {
//   int bagsBought = 300;
//   double bagsCost = 3.98;
//   double moneySpent;

//   bagsBought = bagsBought + 239;
//   moneySpent = bagsBought * bagsCost;
  

//   printf("I bought %d bags and I spent $%.1f on bags only!", bagsBought, moneySpent);
// }


// int main() {
  
//   int endingDayOfWeek = 0;
//   int daysThatPass = 44;
//   int daysInWeek = 7;

//   endingDayOfWeek = daysThatPass % daysInWeek;

//   printf("You started on the 1st (0) day of the week, went %d days from this, so it is now the %d day of the week\n", daysThatPass, endingDayOfWeek);
// }

// int main() {
//   int n = 13;
//   int m = 10;

//   m--; // // reduces m by 1
//   n++; // // increases n by 1
  
//   printf("m = %d\n", m);
//   printf("n = %d\n", n);
  
// }

// int main() {
  
//   int timesServerCrashed = 5;
//   double losses = 500.95;

//   losses *= timesServerCrashed;   //this is the same as losses = losses * timesServerCrashed;
//   losses /= 2;   //this is the same as losses = losses/2;

//   printf("Total Losses: $%.2f\n", losses);
// }

// int main() {
  
//   int x = 5;
//   int y = 42;

//   if (x < y) {
//    printf("Congratulations on setting up a comparison correctly!");
//   }

// }

// If you are checking to see if two or more parts are true you can use && between them. If you want to see if any of the parts is true you can use ||

// int main() {
// int a = 2;
// int b = 3;
// if (a == b && a == 2) {
//   printf("both are true\n");
// }
// if (a == b || a == 2) {
//   printf("one or both are true\n");
// }
// if (!(a == b)) {
//   printf("they are not equal\n");
// }

// }

// int main() {
  
//   int x = 1;
//   int y = 27;

//   if (x != y) {
//     printf("Congratulations on setting up a comparison correctly!");
//   } else {
//     printf("Please try again!");
//   }

// }


// int main() {
  
//   int x = 1;
//   int y = 27;

//   if (x == y) {
//     printf("Congratulations on setting up a comparison correctly!");
//   } else {
//     printf("Please try again!");
//   }

// }


// int main() {
  
//   int x;
//   int y;

//   x = (2 + 3) * 5;
//   y = 2 / (4 + 6);

//   printf("x is: %d\n", x);
//   printf("y is: %d\n", y);
// }


// int main() {
//     int m;
//     int x;

//     x = 2 + 98;
//     m = 78/2;

//     if (x == m) {
//         printf("GLORRY!!!");
        
//     } else {
//         printf("There is still hope!");
//     }
// }

// int main() {
//     int a;
//     double b;

//     a = 30/2;
//     b = 66/7;

//     if (a > b) {
//         printf("more room for improvement");
//     } else {
//         printf("oops!");
//     }
// }

// int main() {

//   int grade1 = 90;
//   int grade2 = 59;
  
//   if (grade1 > 60) {
//     printf("Pass\n");
//   }
//   if (grade2 < 60) {
//     printf("Fail");
//   }
// }


// &&-AND, ||-OR, !-NOT 


// int main() {

//   int a = 10;
//   int b = -5;

//   if (a > 0 && b > 0) {
//     printf("Positive\n");
//   }
// }
// prints the sentence only if both the conditions are true


// int main() {

//   int a = 10;
//   int b = -5;

//   if (a > 0 || b > 0) {
//     printf("Positive\n");
//   }
// }
// prints even if one of the conditions are true.


// int main() {

//   int a = 10;
//   int b = -5;

//   if (a > 0 || b > 0) {
//     printf("Positive\n");
//   }
//   if (a > 0 && !(b > 0)) {
//     printf("Positive\n");
//   }
// }


// int main() {

//   int grade1 = 59;
//   int grade2 = 90;

//   if (grade1 > 60) {
//     printf("Pass\n");
//   } else {
//     printf("Fail\n");
//   }

// }


// int main() {

//   int grade1 = 59;
//   int grade2 = 90;

//   if (grade1 > 60) {
//     printf("Pass\n");
//   } else {
//     printf("Fail\n");
//   }

//   if (grade2 > 60) {
//     printf("Pass\n");
//   } else {
//     printf("Fail\n");
//   }

// }

// else if operator can be used so many times after if operator which is used only once and before the else operator which is used only once.


// int main() {
 
//   // double ph = 7.9;
//   // double ph = 4.6;
//   double ph = 7;

//   if (ph > 7) {
//     printf("Basic\n");
//     }
//   else if (ph < 7) {
//     printf("Acidic\n");
//     } else {
//       printf("Neutral\n");
//     }
  

// }

// //else operator prints out if all conditions fail to pass or in others words if all conditions are false and the else condition is true.



//switch statements.

// cc

// int main() {

//   int a = 10;
//   int b = 5;
//   int min;

//   // Print out the smaller number with return
//   min = a < b ? a : b;
//   printf("%d\n", min);

//   // Print out the smaller number without return
//   a < b ? printf("%d\n", a) : printf("%d\n", b);
// }

// confused about the use of ternary operators


// int main() {
//     int myNum = 15;
//     printf( "%d", myNum);
// }

// int main() {
//     int mySum = 21;
//     printf("%d", mySum);
// }

// int main() {
// // Create variables
//     int myNum = 5;             // Integer (whole number)
//     float myFloatNum = 5.99;   // Floating point number
//     char myLetter = 'D';       // Character

// // Print variables
//     printf("%d\n", myNum);
//     printf("%f\n", myFloatNum);
//     printf("%c\n", myLetter);

// }

// int main() {
//     printf("my name is NANA");
// }

// int main () {

//     int myNum = 34;

//     printf("Daddy bought %d oranges\n", myNum);
//     printf("He also bought %d mangoes", myNum);
// }

// int main() {
//     int x = 5;
//     int y = 6;
//     int sum = x + y;
//     printf("%d", sum);

// }

// int main() {
//     int x = 5, y = 6, z = 50;
// printf("%d", x + y + z);
// }

// int main() {
//     int x, y, z;
//     x = y = z = 50;
//     printf("%d", x + y + z);
// }



// // The general rules for naming variables are:

// // Names can contain letters, digits and underscores
// // Names must begin with a letter or an underscore (_)
// // Names are case sensitive (myVar and myvar are different variables)
// // Names cannot contain whitespaces or special characters like !, #, %, etc.
// // Reserved words (such as int) cannot be used as names

// we use constant when we don't want to make any changes so it becomes read only.

// int main() {
//     const int myNum = 12;
//     int = 34;
//     printf("%d", myNum);

// }//// this produces an error because int was constant but i tried modifying it 

// int main() {
//     const int BIRTHYEAR = 1980;
//     printf("%d", BIRTHYEAR);
// }

// int main() {
//     int day = 4;

// switch (day) {
//   case 1:
//     printf("Monday");
//     break;
//   case 2:
//     printf("Tuesday");
//     break;
//   case 3:
//     printf("Wednesday");
//     break;
//   case 4:
//     printf("Thursday");
//     break;
//   case 5:
//     printf("Friday");
//     break;
//   case 6:
//     printf("Saturday");
//     break;
//   case 7:
//     printf("Sunday");
//     break;
// }

// // Outputs "Thursday" (day 4)

// }

// int main() {
//     int day = 4;

// switch (day) {
//   case 6:
//     printf("Today is Saturday");
//     break;
//   case 7:
//     printf("Today is Sunday");
//     break;
//   default:
//     printf("Looking forward to the Weekend");
// }

// Outputs "Looking forward to the Weekend"
// if u put in any other number apart from 6 and 7 u get the last sentence😎
// }


// int main() {
//     int planet = 4; //Little Mac is already on planet Earth.  

// switch (planet) {
//   case 1: // planet 1  is mercury
//     printf("0.38");
//     break;
//   case 2: // planet 2 is Venus
//     printf("0.91");
//     break;
//   case 3: // planet 3 is Mars
//     printf("0.38");
//     break;
//   case 4: //planet 4 is Jupiter
//     printf("2.34");
//     break;
//   case 5: //planet 5 is Saturn
//     printf("1.06");
//     break;
//   case 6: //planet 6 is Uranus
//     printf("0.92");
//     break;
//   case 7: //planet 7 is Neptune
//     printf("1.19");
//     break;
// }


// }


// int main() {
//   int pin = 0;
//   int tries = 0;

//   printf("BANK OF CODECADEMY:\n");
//   printf("Enter your PIN: ");
//   scanf("%d", &pin);

//   tries++;

//   while (pin != 1234 && tries < 3) {

//     printf("Enter your PIN: ");

//     scanf("%d", &pin);
//     tries++;
//   }

//   if (pin == 1234) {
//     printf("PIN accepted!\n");
//     printf("You now have access.\n");
//   }
// }



// int main() {
//   int i = 0;

//   while (i < 5) {
//   printf("%d\n", i);
//   i++;
//   }
// }

// int main() {
//   int i = 0;
//   while (i < 5) {
//     printf("today is my birthday\n");
//     i++;
//   }
// }

// #include <stdio.h>

// int main() {

//   int guess;
//   int tries = 0;

//   printf("I'm thinking of a number in the range 1-10.\n");
//   printf("Try to guess it: ");
//   scanf("%d", &guess);

//   // Write a while loop here:
//  while (guess != 8 && tries < 5 )  {
//    printf("Try to guess it:");
//    scanf("%d", &guess);    
//  }



//   if (guess == 8) {
//     printf("You got it!\n");
//   }
// }

// int main() {
//     // Create an integer variable that will store the number we get from the user
// int myNum;

// // Ask the user to type a number
// printf("Type a number: \n");

// // Get and save the number the user types
// scanf("%d", &myNum);

// // Output the number the user typed
// printf("Your number is: %d", myNum);

// }

