#include <stdio.h>
// int main(void)
// {
//     puts("Hello, World");
//     return 0;
// }
// // will be right back

/* this is a comment*/

// int main(void)
// {
//     printf("This is Nana Yaa");
//     return 0;
// }


// int main(void)
// {
//     puts("Hey Aziz!");
//     return 0;

// }

// int main()
// {
//     printf("Hello, World!\n");
//     return 0;
// }

// int main()
// {
//     printf("Hi Frederick!\n");
// }

// int main()
// {
//     printf("my\tname\tis\tNana");
// }

// int main()
// {
//     printf("My\nPet");
// }

// int main()
// {
//     printf("hello\tDaddy");
// }

// int main() {
//   // Simple Recipe
//   printf("2 Cups: All Purpose Flour\n");
//   printf("1 Cups: Unsalted Butter\t(Room Temperature)");
//   printf("\n2/3 Cups: Granulated Sugar");
  
// }

// int main() {
//   //I really love them, they are very tasty
//   printf("Chocolate chip cookies are way better than oatmeal raisin cookies.\n");
  
// /*I am learning this lanaguage next semester*/ 
//   printf("Learning the C programming language is an exciting adventure!\n");
// }


// int main() {
  
//   int number;
//   int test_value;
//   int example;
//   float floatExample;
//   printf("Hello World!\n");

// }


// int main() {
  
//  int ageLearnedToRide = 5;


//  printf("I was %d years old when I learned to ride a bike.\n", ageLearnedToRide);
//  printf("I hope I still remember how to ride.");
// }

// int main() {
//     int numOfMangoes = 10;

//     printf("Mama bought %d mangoes from Madina Market.", numOfMangoes);
//     printf("\nThese mangoes are delicious!");
// }

//when declaring char you need a single quote around it 

// int main() {
  
//   int numOfBooks = 10;
//   char favLetter = 'N';
//   char favDigit = '7';
//   double costOfCandyBar = 12.34678;

//   printf("Number of books: %d\n", numOfBooks);
//   printf("Your Favorite Letter is: %c\n", favLetter);
//   printf("Your Favorite Digit is: %c\n", favDigit);
//   printf("You expect to pay $%.2f for a candy bar.\n", costOfCandyBar);
// }
// // the .2  or any ".a number" like .3 ,tells the compiler to print the two digits after the point



// int main() {
  
//   // These variables were created and had a starting value for you, no need to change
//   char bookVersionReview = 'A';
//   char movieVersionReview = 'B';
//   double ticketPrice = 10.25;
//   double bookPrice = 19.99;

// // below this line is what has being updated 
//   bookVersionReview = 'B';
//   movieVersionReview = 'C';
//   ticketPrice = bookPrice;


//   // No need to change below here
//   printf("The book version has a review score of %c and costs $%.2f\n", bookVersionReview, bookPrice);
//   printf("The movie version has a review score of %c and costs $%.2f\n", movieVersionReview, ticketPrice);
// }



// It is also a best practice to use all upper case letters when declaring a constant
int main() {
  
// Speed of light is 1.86e5 mi/s or 186000 mi/s we will store 1.86 and do the multiplicaiton later.
    const double SPEEDOFLIGHT = 1.86;
    int timeTraveledInSeconds = 30;


    //  No need to change below here
//   printf("Light would travel %.2f miles in %d seconds\n", SPEEDOFLIGHT * 100000 * timeTraveledInSeconds, timeTraveledInSeconds);

}

int main() {
    int pin = 0;
    int tries = 0;

    printf("BANK OF CODECADEMY:\n");
    printf("Enter your PIN: ");
    scanf("%d", &pin);

    tries++;

    while (pin != 1234 && tries < 3) {
    printf("Enter your PIN: ");
    scanf("%d", &pin);
    tries++;
}

    if (pin == 1234) {
    printf("PIN accepted!\n");
    printf("You now have access.\n");
    }
}

