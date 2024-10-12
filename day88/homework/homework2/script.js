const btn1 = document.getElementById('btn1');
const btn2 = document.getElementById('btn2');

const img1 = document.getElementById('img1');

const arr = ['/images/photo/Geo subaru impreza - second photo.jpg', 'day88/homework/homework2/imgs/Geo subaru legacy.jpg']

let counter = 0

btn1.addEventListener('click', function(){
    img1.src = arr[counter]

    if(counter === 0){
        img1.src = 'day88/homework/homework2/imgs/Geo subaru legacy.jpg'
        counter += 1
    } else if (counter === 1){
        img1.src = '/images/photo/Geo subaru impreza - second photo.jpg'
        counter -= 1
    }
})

btn2.addEventListener('click', function(){
    img1.src = arr[counter]

    if(counter === 0){
        img1.src = '/day88/homework/homework2/Geo subaru legacy.jpg'
        counter += 1
    } else if (counter === 1){
        img1.src = '/images/photo/Geo subaru impreza - second photo.jpg'
        counter -= 1

    }
})