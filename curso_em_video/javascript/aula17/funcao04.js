function fatorial(num) {
    let res = 1
    for (var c = num; c > 0; c--){
        res *= c
    }

    return res

}

console.log(fatorial(5))