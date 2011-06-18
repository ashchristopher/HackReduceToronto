var chart;
$(document).ready(function() {
   var categories = [];
   DATA.forEach(function(item) {
       console.log(item);
   });
   chart = new Highcharts.Chart({
      chart: {
         renderTo: 'placeholder',
         defaultSeriesType: 'column'
      },
      title: {
         text: 'Search by Type'
      },
      xAxis: {
         categories: [
            'First', 
            'Second', 
            'Third' 
         ]
      },
      yAxis: {
         min: 0,
         title: {
            text: 'Rainfall (mm)'
         }
      },
      legend: {
         layout: 'vertical',
         backgroundColor: '#FFFFFF',
         align: 'left',
         verticalAlign: 'top',
         x: 100,
         y: 70,
         floating: true,
         shadow: true
      },
      tooltip: {
         formatter: function() {
            return ''+
               this.x +': '+ this.y +' mm';
         }
      },
      plotOptions: {
         column: {
            pointPadding: 0.2,
            borderWidth: 0
         }
      },
           series: [{
         name: 'Travel',
         data: [49.9, 71.5, 106.4]
   
      }, {
         name: 'Sex',
         data: [83.6, 78.8, 98.5]
   
      }, {
         name: 'Nerd',
         data: [48.9, 38.8, 39.3]
   
      }, {
         name: 'Cooking',
         data: [42.4, 33.2, 34.5]
   
      }]
   });
   
   
});
