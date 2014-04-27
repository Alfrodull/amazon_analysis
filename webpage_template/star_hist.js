$(function () {
		
        var starHist = new Highcharts.Chart({
            chart: {
                renderTo: 'star_hist',
                type: 'column'
            },
            title: {
                text: '商品评分柱状图'
            },
            xAxis: {
                categories: [
                    '五星',
                    '四星',
                    '三星',
                    '两星',
                    '一星',
                ]
            },
            yAxis: {
                min: 0,
                title: {
                    text: '评分人次'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.lf} 人次</b></td></tr>',
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
                data: star_list
    
            }]
        });
    });
