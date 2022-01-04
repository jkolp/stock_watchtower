
function display_chart() {
    // This call should get all of the necessary infos to create the chart
    // : company name, dates and closing price
    fetch_stock(stock_json => {
        alert(stock_json)
    })
}


function fetch_stock(callback) {
    var search_textfield = document.querySelector('.text_input')
    var ticker = search_textfield.value

    fetch('/get_stock_info/'+ ticker)
    .then(response => response.json()) // parses JSON response into native JavaScript objects Returns js promise object
    .then(data => {
        var json = JSON.parse(data) // JSON.parse makes the data object accessible
        callback(json.quoteType.shortName)
    })
    .catch(error => {
        alert("There was an error fething : " + ticker + "\nPlease check your ticker");
    })
}

// function fetch_stock_history(callback) {
//     var search_textfield = document.querySelector('.text_input')
//     var ticker = search_textfield.value

//     fetch('/search_stock_history/'+ ticker)
//     .then(response => response.json()) // parses JSON response into native JavaScript objects Returns js promise object
//     .then(data => {
//         var json = JSON.parse(data) // JSON.parse makes the data object accessible
//         console.log(json.quoteType.prices[0]['0'].volume)
//         callback(json.quoteType.prices)
//     })
//     .catch(error => {
//         alert("There was an error fething : " + ticker + "\nPlease check your ticker");
//         console.log(error)
//     })
// }