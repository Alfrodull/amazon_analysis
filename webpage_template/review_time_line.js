$(function () {
        var reviwTLine = new Highcharts.Chart({
            chart: {
                renderTo: 'review_time_line',
                type: 'line',
                marginRight: 130,
                marginBottom: 25
            },
            title: {
                text: '评论-日期折线图',
                x: -20 //center
            },
            xAxis: {
                categories: date_list
            },
            yAxis: {
                min: 0,
                title: {
                    text: '评论数量'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                formatter: function() {
                    return '<b>'+ this.x +':</b>'+
                         Highcharts.numberFormat(this.y, 0) + '个评论';
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
                name: '评论增量走势',
                data: count_list
            }]
        });
    });
