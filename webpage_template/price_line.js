$(function () {
        var priceLine = new Highcharts.Chart({
            chart: {
                renderTo: 'price_line',
                type: 'line',
                marginRight: 130,
                marginBottom: 25
            },
            title: {
                text: '价格-日期折线图',
                x: -20 //center
            },
            xAxis: {
                categories: date_list
            },
            yAxis: {
                min: 0,
                title: {
                    text: '商品价格'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                formatter: function() {
                    return '<b>'+ this.x +':</b> $'+
                         Highcharts.numberFormat(this.y, 0);
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: [{
                name: '价格走势',
                data: price_list
            }]
        });
    });
