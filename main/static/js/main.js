let body = document.querySelector('body')
let samson = document.querySelector('.samson')
let icon = document.querySelector('.bi-moon-fill')

samson.addEventListener('click', ()=>{
    body.classList.toggle('dark')
    if(body.classList.contains('dark')){
        icon.classList.replace('bi-moom-fill', 'bi-brightness-high-fill')
    }
    else{
        icon.classList.replace('bi-brightness-high-fill')
    }
})
