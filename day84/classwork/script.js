// function person(firstname, lastname) {
//     this.firstname = firstname;
//     this.lastname = lastname;
// }

// const person1 = new person("tazo", "abesadze");
// console.log(person1)

// const person2 = new person("nika", "abesadze")
// console.log(person2)

function person(firstname, lastname, age) {
    this.firstname = firstname;
    this.lastname = lastname;
    this.age = age
}

const person1 = new person("tazo", "abesadze", 16);
console.log(person1);

const person2 = new person("nika", "abesadze", 13);
console.log(person2)