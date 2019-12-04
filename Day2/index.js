const fs = require('fs')
let input = fs.readFileSync('./Day2/input.txt', 'utf-8').split(',').map(Number)

getOutput = (input, noun, verb) => {
    _input = [...input]
    _input[1] = noun
    _input[2] = verb

    let index = 0;
    while (true) {
        if (_input[index] == 1) {
            pos_1 = _input[index + 1]
            pos_2 = _input[index + 2]
            pos_3 = _input[index + 3]
            _input[pos_3] = _input[pos_1] + _input[pos_2]
        }
        else if (_input[index] == 2) {
            pos_1 = _input[index + 1]
            pos_2 = _input[index + 2]
            pos_3 = _input[index + 3]
            _input[pos_3] = _input[pos_1] * _input[pos_2]
        }
        else {
            break;
        }
        index += 4
    }
    return _input[0]
}

findValue = (value) => {
    for (let noun = 0; noun < 100; noun++) {
        for (let verb = 0; verb < 100; verb++) {
            let output = getOutput(input, noun, verb)
            if (output == value) {
                return (100 * noun + verb)
            }
        }
    }
}


console.log(findValue('19690720'))




