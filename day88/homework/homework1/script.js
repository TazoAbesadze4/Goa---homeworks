const myScore = document.getElementById('myScore')
const compScore = document.getElementById('compScore')

const btn = document.getElementById('btn')

const rock = document.getElementById('rock')
const paper = document.getElementById('paper')
const scissors = document.getElementById('scissors')


let words = ['rock', 'paper', 'scissors'] 
console.log('Comp Scores: ')
console.log('')

rock.addEventListener('click', function(){
    let randomWord = words[Math.trunc(Math.random() * 3)]

    if(randomWord === 'paper') {
        compScore.innerHTML = Number(compScore.innerHTML) + 1
    } else if(randomWord === 'scissors') {
        myScore.innerHTML = Number(myScore.innerText) + 1
    }

    console.log(randomWord)
})

paper.addEventListener('click', function(){
    let randomWord = words[Math.trunc(Math.random() * 3)]

    if(randomWord === 'rock') {
        myScore.innerHTML = Number(myScore.innerHTML) + 1
    } else if(randomWord === 'scissors') {
        compScore.innerHTML = Number(compScore.innerText) + 1
    }

    console.log(randomWord)
})

scissors.addEventListener('click', function(){
    let randomWord = words[Math.trunc(Math.random() * 3)]

    if(randomWord === 'paper') {
        myScore.innerHTML = Number(myScore.innerHTML) + 1
    } else if(randomWord === 'rock') {
        compScore.innerHTML = Number(compScore.innerText) + 1
    }

    console.log(randomWord)
})