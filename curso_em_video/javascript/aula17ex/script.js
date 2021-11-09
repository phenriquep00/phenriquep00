function sum(arr){
    let sum = 0
    for (var c of arr){
        sum += Number(c)
    }
    return sum
}

arr = []

var res = document.querySelector("div#res")

function adicionarNumero(){

    res.innerHTML = ''

    let numero = Number(document.querySelector('input#numero').value)
    document.querySelector('input#numero').value = ''

    let select = document.querySelector('select#select')
    let option = document.createElement('option')

    if (numero > 100 || numero <= 0) {
        alert('Número inválido')
    } else if (arr.indexOf(numero) != -1) {
        alert('Número já adicionado na lista')
    } else {
        arr.push(numero)
        option.innerText = `O número ${numero} foi adicionado`
        select.appendChild(option)
    }
}

function finalizar(){
    if (arr.length == 0) {
        alert('Nenhum valor adicionado!')
    } else {
    let paragrafo = document.createElement('p')

        paragrafo.innerHTML += `<p>O total de números adicionados foi ${arr.length}</p>`
        paragrafo.innerHTML += `<p>O maior número informado foi ${arr.sort()[arr.length -1]}</p>`
        paragrafo.innerHTML += `<p>O menor número informado foi ${arr.sort()[0]}</p>`
        paragrafo.innerHTML += `<p>A soma dos números informados é ${sum(arr)}</p>`
        paragrafo.innerHTML += `<p>A média dos valores é ${sum(arr)/arr.length}</p>`
        
        res.appendChild(paragrafo)
    }
    
    
}