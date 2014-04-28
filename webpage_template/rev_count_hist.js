$(function () {
		
        var revNoHist = new Highcharts.Chart({
            chart: {
                renderTo: 'rev_count_hist',
                type: 'column'
            },
            title: {
                text: '商品评论数柱状图'
            },
            xAxis: {
                categories: asin_list
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
                    '<td style="padding:0"><b>{point.y:.lf} </b></td></tr>',
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
                name: '评论数',
                data: rev_count_list
    
            }]
        });
    });
