// 3) შექმენით ობიექტის კონსტრუქტორი რომელსაც გადაეცემა 4 მნიშვნელობა (თქვენი სურვილით აარჩიეთ თუ რა ტიპის ობიექტს შექმნის კონსტრუქტორი)

function carInfo(model, year, hp, engine) {
    this.model = model;
    this.year = year;
    this.hp = hp;
    this.engine = engine;
}

const car = new carInfo('subaru', '2006', '300+', '2.5T')
console.log(car)