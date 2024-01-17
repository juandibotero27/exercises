//exercise 1 
document.getElementById('container')

//exercise 2
document.querySelector('#container')

//exercise 3
document.querySelectorAll('.second')

//exercise 4
document.querySelectorAll('ol .third')

//exercise 5 
let newText = document.querySelector('#container')
newText.innerText = 'hello'

//exercise 6
let newClass = document.querySelector('.footer')
newClass.classList.add('main')

//exercise 7 
let removeClass = document.querySelector('.footer')
removeClass.classList.remove('main')

//exercise 8
let newLi = document.createElement('li')

//exercise 9
newLi.innerText = 'four'

//exercise 10
let ul = document.querySelector('ul')
ul.append(newLi)


//exercise 11
let insideOl = document.querySelectorAll('ol li')
for(let li of insideOl){
    li.style.backgroundColor = 'green'
}

//exercise 12
let removeDiv = document.querySelector('.footer')
removeDiv.remove()