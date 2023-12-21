//1
console.log("let's get ready to party with jQuery")
//2
$('article img').addClass('image-center')
//3
$('article p:last-child').remove()
//4
$('#title').css('font-size', Math.random() * 100)
//5
$('ol').append('<li>Hey I just got added</li>')
//6
$('aside')
.empty()
.append('<p>My apologies for this list existence</p>')
//7
$('input').on('keyup',function(){
    let red = $('input').eq(0).val()
    let blue = $('input').eq(1).val()
    let green = $('input').eq(2).val()
    $('body').css('background-color', 'rgb(' + red + ',' + blue + ','+ green+ ')')
    console.log(red,blue,green)

})
//8
$('img').on('click', function(){
    $(this).remove()
})