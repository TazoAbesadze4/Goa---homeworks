// შექმენით ინეტრვალი, გადაცემულ ფუნციაში ყოველ ჯერზე შექმენით date ობიექტი, როცა ამჟამინდელი წუთი გაუტოლდება 35,
// უნდა გაითიშოს ინეტრვალი

// ეს დავალება მოგვიანებით გავაკეთე და დროები სხვა შევურჩიე

let times = 11;

const date = setInterval(function(){
    times++;
    console.log(times);

    if(times === 13) {
        clearInterval(date)
        console.log('stopp!')
    }
}, 60000)