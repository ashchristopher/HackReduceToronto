var chart;
$(document).ready(function() {
   var categories = [];
   var scores = {cooking: [], nerd: [], sex: [], travel: []}

   DATA.forEach(function(item) {
       categories.push(item.time);

       scores.cooking.push(item.scores.cooking);
       scores.sex.push(item.scores.sex);
       scores.nerd.push(item.scores.nerd);
       scores.travel.push(item.scores.travel);
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
         categories: categories,
      },
      yAxis: {
         min: 0,
         title: {
            text: 'Frequencyy'
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
               this.series.name + ' (' + this.y +' queries), (' + this.x + ')';
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
         data: scores.travel
   
      }, {
         name: 'Sex',
         data: scores.sex
   
      }, {
         name: 'Nerd',
         data: scores.nerd
   
      }, {
         name: 'Cooking',
         data: scores.cooking
   
      }]
   });
   
   
});
