$('form').on('submit', function(e){
    e.preventDefault()
    let movie = $('#movie').val()
    let rating = $('#rating').val()
    let movieData = {movie, rating}
    let HTMLtoAppend = createMovie(movieData)
    $('#container').append(HTMLtoAppend)
    $('input').val('')
}) 

$('div').on('click', '#new-div', function(){
    $(this).remove()
})

function createMovie(data){
    return `
    <div id="new-div">
        <li>${data.movie}</li>
         <li>Rating is ${data.rating}</li>
        <button>Delete</button>
    </div>
    `
}
