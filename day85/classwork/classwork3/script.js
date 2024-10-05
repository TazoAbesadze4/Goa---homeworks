// 3) გამოიყენეთ sort მეთოდი რომ დაალაგოთ ელემენტები ზრდადობით შემდეგ კი კლებადობით

const numbers = [11, 22, 32, 34, 15];

numbers.sort(function(a, b){
    return a - b
})

console.log(numbers)


const numberss = [11, 22, 32, 34, 15];

numbers.sort(function(a, b){
    return b - a
})

console.log(numberss)