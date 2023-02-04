// this is an in line comment
/* this is a multiline comment */
// the 8 data types are undefined, null, boolean, string,symbol,bigint,number and object.
var myName;
myName = 8;
var myNum;
myNum = myName;  

var myName = 9;
var myFirstName = "Nana Yaa";
// remember we end statements with semicolons, variable names can be made uo of numbers,letters ,$ etc but nay not contain spaces or start with a number 

a = 3;
a = a + 1;
b = 8;
b = b + 1;

c = "I am a";
c = c + 1;

// Javascript is case sensitive, MYVAR is not the same as MyVar nor myvar
// Write variable names in JavaScript in camelCase. In camelCase, multi-word variable names have the first word in lowercase and the first letter of each subsequent word is capitalized.

// var studlyCapVar;
var properCamelCase;
var titleCaseOver;

// Variable assignments
studlyCapVar = 10;
properCamelCase = "A String";
titleCaseOver= 9000;

let catName = "Oliver";
let catSound = "Meow!";
// using let instead of var to update

var camper = "James";
var camper = "David";
console.log(camper);

// using const are read-only. They are a constant value, which means that once a variable is assigned with const, it cannot be reassigned:

const FAV_PET = "Cats";
FAV_PET = "Dogs";

// let is used when you want to change a variable but const is used when you want to make your variable a constant 

const FCC = "freeCodeCamp"; // Change this line
let fact = "is cool!";  // Change this line
fact = "is awesome!";
console.log(FCC, fact);
//output 
//freeCodeCamp is awesome!

const sum = 10 + 10;
//output is 20
const difference = 45 - 33;
//output is 12
const product = 8 * 10;
//output is 80
const quotient = 66 / 33;
//output is 2


let myVar = 87;
// Only change code below this line
// myVar = myVar + 1; 
// OR
myVar ++ ; // when we want to add 1 to a variable 


let myVar = 11;
// Only change code below this line
// myVar = myVar - 1;
myVar--; //when we want to subtract 1 from a number or variable 

const myDecimal = 0.5;
const product = 2.0 * 2.5; //multiplying decimals
const quotient = 4.4 / 2.0; //dividing decimals

const remainder = 11 % 3; // % is used as the remainder operator , to output the remainder 

let myVar = 1;
myVar += 5;
console.log(myVar); // output will be 6


let a = 3;
let b = 17;
let c = 12;
a += 12; //the intial value of a plus 12
b += 9 ;
c += 7;


let a = 11;
let b = 9;
let c = 3;
a -= 6; //the initial value of a minus 6
b -= 15;
c -= 1;


let a = 5;
let b = 12;
let c = 4.6;
a *= 5;
b *= 3; //the intial value of b multiplied by 
c *= 10;

let a = 5;
let b = 12;
let c = 4.6;
a /= 5;
b /= 3;  //the initial value of b divided by 3
c /= 10;


// In JavaScript, you can escape a quote from considering it as an end of string quote by placing a backslash (\) in front of the quote.
eg. const sampleStr = "Alan said, \"Peter is learning JavaScript\".";
//This signals to JavaScript that the following quote is not the end of the string, but should instead appear inside the string. So if you were to print this to the console, you would get:

Alan said, "Peter is learning JavaScript". // the output
// Use backslashes to assign a string to the myStr variable so that if you were to print it to the console, you would see:

const myStr = "I am a \"double quoted\" string inside \"double quotes\"."; // Change this line
//output will be: I am a "double quoted" string inside "double quotes"

const myStr = '<a href="http://www.example.com" target="_blank">Link</a>';

console.log("Hello World!");
// used for debbuding purposes

var foo = "bar";
console.log(foo);

var greet = "Hello", who = "World";
console.log("%s,%s!" )


let lastNameLength = 0;
const lastName = "Lovelace";
lastNameLength = lastName.length;
console.log(lastNameLength);

//output will be 8


let firstLetterOfLastName = "";
const lastName = "Lovelace";
// Only change code below this line
firstLetterOfLastName = lastName[0]; // Change this line
console.log(firstLetterOfLastName );
//output will be the letter L


let myStr = "Jello World";
myStr = "Hello World"
//the output will be updated to Hello World , in javascripts strings are immutable which means you could have changed J to H through myStr[0]="H" but this will be an error it is never possible 


const lastName = "Lovelace";
const thirdLetterOfLastName = lastName[2]; 

const lastName = "Lovelace";
const lastLetterOfLastName = lastName[lastName.length - 1];

const lastName = "Lovelace";
const lastLetterOfLastName = lastName[lastName.length - 1];

const myNoun = "dog";
const myAdjective = "big";
const myVerb = "ran";
const myAdverb = "quickly";
const wordBlanks ="The" + " " + myAdjective +" " + myNoun +" " + myVerb +" "+ myAdverb +" "+ "yesterday" + "."; // Change this line
// Only change code above this line