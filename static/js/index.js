
function display_chart() {
    // This call should get all of the necessary infos to create the chart
    // : company name, dates and closing price
    
    // TODO 
    // Add datapoints and create the stock chart
    // Convert epnoch time to date 
    // Find out how to customize stock chart to my likings
    var dataPoints = [];
    var company_name = ''

    fetch_stock(stock => {
        company_name = stock['stock_name']
        for(let date_and_price in stock['prices_history']){
            var date_obj = new Date(date_and_price[0])
            // var year = date_obj.getUTCFullYear
            // var month = date_obj.getUTCMonth
            // var day = date_obj.getUTCDay
            // var date = year + "-" + month + "-" + day

            // console.log(date.toString())

            dataPoints.push({x: date_obj, y: date_and_price[1]});
          }
    })

    var stockChart = new CanvasJS.StockChart("chart_container",{
        title: {
            text: company_name
        },
        charts: [{      
            data: [{        
                type: "line", //Change it to "spline", "area", "column"
                dataPoints : dataPoints
            }]
        }],
        navigator: {
            slider: {
                minimum: new Date(2021,04, 01),
                maximum: new Date(2022,01, 01)
            }
        }
    }); 

    // Append dataPoints with date and close price

    stockChart.render();
}


function fetch_stock(callback) {
    var search_textfield = document.querySelector('.text_input')
    var ticker = search_textfield.value

    fetch('/get_stock_info/'+ ticker)
    .then(response => response.json()) // parses JSON response into native JavaScript objects Returns js promise object
    .then(data => {
        callback(data)
    })
    .catch(error => {
        alert("There was an error fething : " + ticker + "\nPlease check your ticker");
    })
}

