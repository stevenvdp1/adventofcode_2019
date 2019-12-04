const fs = require('fs')

const input = fs.readFileSync('./Day1/input1.txt', 'utf-8').split('\r\n')

calculateFuel = (mass) =>{
    return Math.floor(mass/3) - 2
}

getTotalFuel = (rockets) =>{
    let totalFuel = 0;
    for(let mass of rockets){
        fuelToAdd = calculateFuel(mass)
        while(fuelToAdd > 0 ){
            totalFuel += fuelToAdd
            fuelToAdd = calculateFuel(fuelToAdd)
        }
    }
    return totalFuel
}

console.log(getTotalFuel(input))

