const myScoreP = document.getElementById('my-score');
const compScoreP = document.getElementById('comp-score');
const winsP = document.getElementById('wins');
const btnsDiv = document.getElementById('btns');

const well = document.getElementById('well');
const paper = document.getElementById('paper');
const scissors = document.getElementById('scissors');


const arr = ['well', 'paper', 'scissors'];

console.log('Compiuter scores')
console.log('')


well.addEventListener('click', function(){
    let randomWord = arr[Math.trunc(Math.random() * 3)];
    
    if(randomWord === 'scissors') {
        compScoreP.innerHTML = Number(compScoreP.innerText) + 1
    } else if(randomWord === 'paper') {
        myScoreP.innerHTML = Number(myScoreP.innerText) + 1
    } 

    console.log(randomWord)
})

// ფურცელი(paper),  ჭა(well),  მაკრატელი(scissors)

paper.addEventListener('click', function(){
    let randomWord = arr[Math.trunc(Math.random() * 3)];
    
    if(randomWord === 'scissors') {
        myScoreP.innerHTML = Number(myScoreP.innerHTML) + 1
    } else if(randomWord === 'well') {
        compScoreP.innerHTML = Number(compScoreP.innerText) + 1
    }

    console.log(randomWord)
})

scissors.addEventListener('click', function(){
    let randomWord = arr[Math.trunc(Math.random() * 3)];
    
    if(randomWord === 'paper') {
        compScoreP.innerHTML = Number(compScoreP.innerHTML) + 1;
    } else if(randomWord === 'well') {
        myScoreP.innerHTML = Number(myScoreP.innerText) + 1;
    }

    console.log(randomWord)
})