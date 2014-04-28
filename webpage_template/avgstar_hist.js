$(function () {
		
        var avgstarHist = new Highcharts.Chart({
            chart: {
                renderTo: 'avgstar_hist',
                type: 'column'
            },
            title: {
                text: '商品平均评分柱状图'
            },
            xAxis: {
                categories: asin_list
            },
            yAxis: {
                min: 0,
                title: {
                    text: '平均评分'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.lf} 分</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                name: '评分',
                data: avgstar_list
    
            }]
        });
    });
