const myScoreP = document.getElementById('my-score');
const compScoreP = document.getElementById('comp-score');
const winsP = document.getElementById('wins');
const btnsDiv = document.getElementById('btns');

const choic = ['rock', 'paper', 'scissors'];

let myScore = 0;
let compScore = 0;

btnsDiv.addEventListener('click', function(e){
    const btnId = e.target.dispatchEvent;

    const compChoice = choic[Math.floor(Math.random() * choic.length)];

    if(btnId === compChoice) {
        winsP.textContent = 'Its a tie!';
    }

    else if((btnId === 'rock' && compChoice === 'paper') || (btnId === 'scissors' && compChoice === "rock") || (btnId === 'paper' && compChoice === 'scissors')) {
        compScore++;
        compScoreP.textContent = compScore;
        winsP.textContent = 'you lose!';
    }

    else {
        myScore++;
        myScoreP.textContent = myScore;
        winsP.textContent = 'you won!'
    }
})


// kodi ar mushaobs