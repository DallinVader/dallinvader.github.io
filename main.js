let clickCount = 0
let maxClickCount = 0
let explosionCount = localStorage.getItem("Poped Balloons")
height = 120
width = 100
let inflationRate = 25
let maxsize = 250
let RandomMaxSize = 1000
let ClockID = 0
let timeRemaining = 0
let gamelength = 3000
timer = false
var CountDownButton = document.getElementById("countdown")


function inflate(){
    if(timer == true){
        if(maxClickCount <= clickCount){
            maxClickCount = clickCount + 1
            console.log(maxClickCount)
            MaxInflatecouountVar = document.getElementById("MaxInflatecount")
            MaxInflatecouountVar.innerText = maxClickCount
        }
        if(height >= maxsize){
            height = 0
            width = 0
            maxsize = Math.random() * RandomMaxSize
            explosionCount++
            var explosionCountElem = document.getElementById("explosionCount")
            explosionCountElem.innerText = explosionCount
            clickCount = 0
        } 
        height += inflationRate
        width += inflationRate
        var balloonElement = document.getElementById("balloon")
        balloonElement.style.height = height
        balloonElement.style.width = width
        
        clickCount++
        
        var clickCountelem = document.getElementById("counter")
        clickCountelem.innerText = clickCount.toString()
        
    }

}
function StartGame(){
    if (timer == false){
        var counterbutton = document.getElementById("counter")
        CountDownButton.innerText = gamelength / 1000
        timeRemaining = gamelength
        timer = true
        startClock()
        setTimeout(() => {maxsize = 0, inflate(), timer = false, stopClock()}, gamelength)
    }
}
function Reset(){
    localStorage.setItem("Poped Balloons", 0)
    maxClickCount = 0
    explosionCount = 0
    var explosionCountElem = document.getElementById("explosionCount")
    explosionCountElem = explosionCount
}
function startClock(){
ClockID = setInterval(drawClock, 1000)
}

function drawClock(){
    if (timer == true){

        timeRemaining -= 1000
        CountDownButton.innerText = timeRemaining / 1000
        localStorage.setItem("Poped Balloons", explosionCount)
    }
}

function stopClock(){
    clearInterval(ClockID)
    timeRemaining = gamelength
}