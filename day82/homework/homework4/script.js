function RangeArray(start, end) {
    let result = [];
    for (let x = start; x <= end; x ++) {
        result.push(x);
    }

    return result;
}

let start = 5;
let end = 10;
let numbersInRange = RangeArray(start, end);
console.log(numbersInRange);