// გამოიყენეთ კუთვნილებები რომელიც ვისწავლეთ, ამ კუთვნილებების დახმარებით მანიპულაცია მოახდინეთ სხვადასხვა ელემენტებზე აგრეთვე ახსენით რას ემსახურება ყველა კუთვნილება + გამოიყენეთ getElementsByTagname and getElementsByClassname და ახსენით მათი დანიშნულება, რას აბრუნებს და რისგან განსხვავდება სხვა მეთოდებისგან
// კუთვნილებები: parentElement, children, firstElementChild, lastElementChild, previousElementSibling, nextElementSibling 

const div = document.getElementById('div');
const p = document.getElementsByTagName('p');
const a = document.getElementsByClassName('gg');

console.log(a)

console.log(div.children);
// ეს გამოგვიტანს დივში მოქცეულ მელემენტებს

console.log(div.parentElement);
// ეს გამოგვიტანს მშობელ ელემენტს

console.log(div.firstElementChild);
// ეს გამოიტანს დივში მოქცეულ პირველ ელემენტს

console.log(div.lastElementChild);
// ეს გამოიტანს სივში მოქცეულ ბოლო ელემენტს

console.log(div.previousElementSibling);
// ეს გამოიტანს დივამდე ელემენტს

console.log(div.nextElementSibling);
// ეს გამოიტანს დივის შემდეგ ელემენტს