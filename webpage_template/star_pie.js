$(function () {
        var star_pie = new Highcharts.Chart({
            chart: {
                renderTo: 'star_pie',
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false
            },
            title: {
                text: '商品评分饼状图'
            },
            tooltip: {
        	    pointFormat: '{series.name}: <b>{point.percentage}%</b>',
            	percentageDecimals: 1
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        color: '#000000',
                        connectorColor: '#000000',
                        formatter: function() {
                            return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';
                        }
                    }
                }
            },
            series: [{
                type: 'pie',
                name: '所占百分比',
                data: [
                    ['五星', rate[0] ],
                    {
                        name: '四星',
                        y: rate[1],
                        sliced: true,
                        selected: true
                    },
                    ['三星',  rate[2] ],
                    ['两星',  rate[3] ],
                    ['一星',  rate[4] ]
                ]
            }]
        });
    });