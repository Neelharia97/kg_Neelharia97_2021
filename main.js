digitToText = {                                 // Map all numbers to text in an object
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three',  '4': 'Four', 
    '5': 'Five', '6': 'Six', '7': 'Seven',  '8': 'Eight', '9': 'Nine'
}

const Args = process.argv.slice(2)              // Get arguments from command, second one onwards

// For every argument, convert each number string to an array of chars, map to corresponding num text, add to new array and join, and then join all the numbers
console.log(Args.map(arg => arg.split('').map(digit => digitToText[digit]).join('')).join(','))