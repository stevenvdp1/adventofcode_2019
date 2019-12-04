const fs = require('fs')

const lines = fs.readFileSync('./Day3/input.txt', 'utf-8').split('\r\n')
const wire_1 = lines[0].split(',')
const wire_2 = lines[1].split(',')

let x_pos = 0
let x_max = 0
let x_min = 0
let y_pos = 0
let y_max = 0
let y_min = 0
for (let step of wire_1) {
    let direction = step.substr(0, 1)
    let distance = parseInt(step.substr(1))
    switch (direction) {
        case ('R'):
            x_pos += distance
            x_max = Math.max(x_max, x_pos)
            break;
        case ('L'):
            x_pos -= distance
            x_min = Math.min(x_min, x_pos)
            break;
        case ('U'):
            y_pos += distance
            y_max = Math.max(y_max, y_pos)
            break;
        case ('D'):
            y_pos -= distance
            y_min = Math.min(y_min, y_pos)
            break
    }
}
x_pos = 0
y_pos = 0
for (let step of wire_2) {
    let direction = step.substr(0, 1)
    let distance = parseInt(step.substr(1))
    switch (direction) {
        case ('R'):
            x_pos += distance
            x_max = Math.max(x_max, x_pos)
            break;
        case ('L'):
            x_pos -= distance
            x_min = Math.min(x_min, x_pos)
            break;
        case ('U'):
            y_pos += distance
            y_max = Math.max(y_max, y_pos)
            break;
        case ('D'):
            y_pos -= distance
            y_min = Math.min(y_min, y_pos)
            break
    }
}

console.log(`x_min: ${x_min}`)
console.log(`x_max: ${x_max}`)
console.log(`y_min: ${y_min}`)
console.log(`y_max: ${y_max}`)

let width = x_max - x_min
let height = y_max - y_min
let start = { x: '', y: '' }
console.log(`width: ${width}`)
console.log(`height: ${height}`)

let grid = new Array(width).fill('.').map(() => new Array(height).fill('.'))


