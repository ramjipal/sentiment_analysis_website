
// Initialize an empty object to store comments and their count
var sentiCount = {'Positive': 0, 'Negative': 0, 'Neutral': 0};

// Count the occurrence of each comment
commentsAndSentiment.forEach(function(senti) {
    sentiCount[senti] = (sentiCount[senti] || 0) + 1;
});

sentilabel = Object.keys(sentiCount);
senticount = Object.values(sentiCount);

console.log(sentiCount);



  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: sentilabel,
      datasets: [{
        label: 'Setiment count',
        data: senticount,
      }],
      backgroundColor: [
          'rgb(54, 162, 235)',
          'rgb(25, 99, 132)',
          'rgb(255, 205, 86)'
        ],
    },
    options: {
      responsive: false,
      title:{
          display: true,
          text: "Color test"
      }
  }

  });



// showing count summery in html

document.getElementById('positive').innerHTML = sentiCount['Positive']
document.getElementById('negative').innerHTML = sentiCount['Negative']
document.getElementById('neutral').innerHTML = sentiCount['Neutral']


