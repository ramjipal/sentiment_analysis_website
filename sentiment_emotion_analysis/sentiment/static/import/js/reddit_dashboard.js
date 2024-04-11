
// Initialize an empty object to store comments and their count
var sentiCount_dic = {'Positive': 0, 'Negative': 0, 'Neutral': 0};
var barColors = ["green","red","orange"];

// Count the occurrence of each comment
commentsAndSentiment.forEach(function(senti) {
    sentiCount_dic[senti] = (sentiCount_dic[senti] || 0) + 1;
});

sentilabel = Object.keys(sentiCount_dic);
senticount = Object.values(sentiCount_dic);

console.log(sentiCount_dic);



  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: sentilabel,
      datasets: [{
        backgroundColor: barColors,
        label: 'Sentiment Chart',
        data: senticount,
      }],
      
    },
    options: {
      responsive: false,
      title:{
          display: true,
          text: "sentiment chart"
      }
  }

  });



// showing count summery in html

document.getElementById('positive').innerHTML = sentiCount_dic['Positive']
document.getElementById('negative').innerHTML = sentiCount_dic['Negative']
document.getElementById('neutral').innerHTML = sentiCount_dic['Neutral']


