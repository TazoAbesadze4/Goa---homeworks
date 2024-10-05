const button = document.getElementById('btn');

button.addEventListener('click', function(){
    let randomNum = Math.trunc(Math.random() * 1000);

    let newP = document.createElement('p');
    newP.textContent = "random: " + randomNum;

    document.body.appendChild(newP)
})