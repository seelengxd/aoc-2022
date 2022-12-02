const fs = require('fs');

const data : string = fs.readFileSync('day1.txt', 'utf8');

function day1() {
    let first = 0;
    let second = 0;
    let third = 0;
    let curr = 0;

    function updateTopThree(curr: number) : void {
        if (first < curr) {
            third = second;
            second = first;
            first = curr;
        } else if (second < curr) {
            third = second;
            second = curr;
        } else if (third < curr) {
            third = curr;
        }
    }

    for (const line of data.split("\n")) {
        if (!line) {
            updateTopThree(curr);
            curr = 0;
        } else {
            curr += parseInt(line);
        }
    }
    
    updateTopThree(curr);

    console.log(`Part 1: ${first}`)
    console.log(`Part 2: ${first + second + third}`);
}

day1();
