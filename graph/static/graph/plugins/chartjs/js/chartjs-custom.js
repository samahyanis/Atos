$(function () {
	"use strict";
	// chart 1
	var ctx = document.getElementById('chart1').getContext('2d');
	var myChart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: ['14/05/2022', '16/05/2022', '19/05/2022', '23/05/2022', '24/05/2022', '25/05/2022', '26/05/2022'],
			datasets: [{
				label: 'Temps exécution en secondes',
				data: [10800, 9720, 5620, 11120, 10800, 10800, 10800],
				backgroundColor: "transparent",
				borderColor: "#673ab7",
				pointRadius: "0",
				borderWidth: 4
			}, {
				label: 'Moyenne exécution',
				data: [10800, 10800, 10800, 10800, 10800, 10800, 10800],
				backgroundColor: "transparent",
				borderColor: "#32ab13",
				pointRadius: "0",
				borderWidth: 4
			}]
		},
		options: {
			maintainAspectRatio: false,
			legend: {
				display: true,
				labels: {
					fontColor: '#585757',
					boxWidth: 40
				}
			},
			tooltips: {
				enabled: false
			},
			scales: {
				xAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true,
						color: "rgba(0, 0, 0, 0.07)"
					},
				}],
				yAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true,
						color: "rgba(0, 0, 0, 0.07)"
					},
				}]
			}
		}
	});
	// chart 2
	var ctx = document.getElementById("chart2").getContext('2d');
	var myChart = new Chart(ctx, {
		type: 'bar',
		data: {
			labels: ['14/05/2022', '15/05/2022', '16/05/2022', '20/05/2022', '21/05/2022', '22/05/2022', '23/05/2022'],
			datasets: [{
				label: 'Date de debut',
				data: [141132, 141132, 141132, 141132, 141132, 141132, 141132],
				barPercentage: .5,
				backgroundColor: "#673ab7"
			}, {
				label: 'date de fin',
				data: [173205, 173205, 173205, 173205, 173205, 173205, 173205],
				barPercentage: .5,
				backgroundColor: "#bf9bff"
			}]
		},
		options: {
			maintainAspectRatio: false,
			legend: {
				display: true,
				labels: {
					fontColor: '#585757',
					boxWidth: 40
				}
			},
			tooltips: {
				enabled: true
			},
			scales: {
				xAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true,
						color: "rgba(0, 0, 0, 0.07)"
					},
				}],
				yAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true,
						color: "rgba(0, 0, 0, 0.07)"
					},
				}]
			}
		}
	});
	// chart 3
	var ctx = document.getElementById('chart3').getContext('2d');
	var myChart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: ['14/05/2022', '16/05/2022', '19/05/2022', '23/05/2022', '24/05/2022', '25/05/2022', '26/05/2022'],
			datasets: [{
				label: 'Temps exécution en secondes',
				data: [10800, 9720, 5620, 11120, 10800, 10800, 10800],
				backgroundColor: "transparent",
				borderColor: "#673ab7",
				pointRadius: "0",
				borderWidth: 4
			}, {
				label: 'Moyenne exécution',
				data: [10800, 10800, 10800, 10800, 10800, 10800, 10800],
				backgroundColor: "transparent",
				borderColor: "#32ab13",
				pointRadius: "0",
				borderWidth: 4
			}]
		},
		options: {
			maintainAspectRatio: false,
			legend: {
				display: true,
				labels: {
					fontColor: '#585757',
					boxWidth: 40
				}
			},
			tooltips: {
				enabled: false
			},
			scales: {
				xAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true,
						color: "rgba(0, 0, 0, 0.07)"
					},
				}],
				yAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true,
						color: "rgba(0, 0, 0, 0.07)"
					},
				}]
			}
		}
	});
	// chart 4
	new Chart(document.getElementById("chart4"), {
		type: 'radar',
		data: {
			labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
			datasets: [{
				label: "1950",
				fill: true,
				backgroundColor: "rgba(179,181,198,0.2)",
				borderColor: "rgba(179,181,198,1)",
				pointBorderColor: "#fff",
				pointBackgroundColor: "rgba(179,181,198,1)",
				data: [8.77, 55.61, 21.69, 6.62, 6.82]
			}, {
				label: "2050",
				fill: true,
				backgroundColor: "rgba(255,99,132,0.2)",
				borderColor: "rgba(255,99,132,1)",
				pointBorderColor: "#fff",
				pointBackgroundColor: "rgba(255,99,132,1)",
				pointBorderColor: "#fff",
				data: [25.48, 54.16, 7.61, 8.06, 4.45]
			}]
		},
		options: {
			maintainAspectRatio: false,
			title: {
				display: true,
				text: 'Distribution in % of world population'
			}
		}
	});
	// chart 5
	new Chart(document.getElementById("chart5"), {
		type: 'polarArea',
		data: {
			labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
			datasets: [{
				label: "Population (millions)",
				backgroundColor: ["#673ab7", "#32ab13", "#f02769", "#ffc107", "#198fed"],
				data: [2478, 5267, 734, 784, 433]
			}]
		},
		options: {
			maintainAspectRatio: false,
			title: {
				display: true,
				text: 'Predicted world population (millions) in 2050'
			}
		}
	});
	// chart 6
	new Chart(document.getElementById("chart6"), {
		type: 'doughnut',
		data: {
			labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
			datasets: [{
				label: "Population (millions)",
				backgroundColor: ["#673ab7", "#32ab13", "#f02769", "#ffc107", "#198fed"],
				data: [2478, 5267, 734, 784, 433]
			}]
		},
		options: {
			maintainAspectRatio: false,
			title: {
				display: true,
				text: 'Predicted world population (millions) in 2050'
			}
		}
	});
	// chart 7
	let optionJob = {
		type: 'horizontalBar',
		data: {
			labels: [],
			datasets: [{
				label: "Durée (Secondes)",
				backgroundColor: ["#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7",, "#673ab7", "#673ab7", "#673ab7", "#673ab7"
				, "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7"
				, "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7"],
				data: []
			}]
		},
		options: {
			maintainAspectRatio: false,
			legend: {
				display: false
			},
			title: {
				display: true,
				text: 'Durée execution job'
			}
		}
	}
	async function prettyGraph7() {

    const res = await $.ajax({
    type: "GET",
    url: "http://127.0.0.1:8000/graph/graph/index6",
    async : true,
    success: function( response ) {
            let dataParsed = JSON.parse(response)
            let dataObj = Object.values(dataParsed[0])[0]
            $.each(dataObj, function(key, val){
                let jobName = Object.keys(val)[0]
                let durationJob = Object.values(val)[0]
                optionJob.data.labels.push(jobName)
                optionJob.data.datasets[0].data.push(parseInt(durationJob))
            })
    }
    })
    return res;
}
async function displayGraph7() {
        await prettyGraph7()
}

// display graph async execution with then
displayGraph7().then(() => {
          new Chart(document.getElementById("chart7"), optionJob  )
    })
	new Chart(document.getElementById("chart7"), );


	// chart 8
	new Chart(document.getElementById("chart8"), {
		type: 'bar',
		data: {
			labels: ["1900", "1950", "1999", "2050"],
			datasets: [{
				label: "Africa",
				backgroundColor: "#673ab7",
				data: [133, 221, 783, 2478]
			}, {
				label: "Europe",
				backgroundColor: "#f02769",
				data: [408, 547, 675, 734]
			}]
		},
		options: {
			maintainAspectRatio: false,
			title: {
				display: true,
				text: 'Population growth (millions)'
			}
		}
	});
	// chart 9
	new Chart(document.getElementById("chart9"), {
		type: 'bar',
		data: {
			labels: ["1900", "1950", "1999", "2050"],
			datasets: [{
				label: "Europe",
				type: "line",
				borderColor: "#673ab7",
				data: [408, 547, 675, 734],
				fill: false
			}, {
				label: "Africa",
				type: "line",
				borderColor: "#f02769",
				data: [133, 221, 783, 2478],
				fill: false
			}, {
				label: "Europe",
				type: "bar",
				backgroundColor: "rgba(0,0,0,0.2)",
				data: [408, 547, 675, 734],
			}, {
				label: "Africa",
				type: "bar",
				backgroundColor: "rgba(0,0,0,0.2)",
				backgroundColorHover: "#3e95cd",
				data: [133, 221, 783, 2478]
			}]
		},
		options: {
			maintainAspectRatio: false,
			title: {
				display: true,
				text: 'Population growth (millions): Europe & Africa'
			},
			legend: {
				display: false
			}
		}
	});
	// chart 10
	new Chart(document.getElementById("chart10"), {
		type: 'bubble',
		data: {
			labels: "Africa",
			datasets: [{
				label: ["China"],
				backgroundColor: "#673ab7",
				borderColor: "#673ab7",
				data: [{
					x: 21269017,
					y: 5.245,
					r: 15
				}]
			}, {
				label: ["Denmark"],
				backgroundColor: "#198fed",
				borderColor: "#198fed",
				data: [{
					x: 258702,
					y: 7.526,
					r: 10
				}]
			}, {
				label: ["Germany"],
				backgroundColor: "#ffc107",
				borderColor: "#ffc107",
				data: [{
					x: 3979083,
					y: 6.994,
					r: 15
				}]
			}, {
				label: ["Japan"],
				backgroundColor: "#f02769",
				borderColor: "#f02769",
				data: [{
					x: 4931877,
					y: 5.921,
					r: 15
				}]
			}]
		},
		options: {
			maintainAspectRatio: false,
			title: {
				display: true,
				text: 'Predicted world population (millions) in 2050'
			},
			scales: {
				yAxes: [{
					scaleLabel: {
						display: true,
						labelString: "Happiness"
					}
				}],
				xAxes: [{
					scaleLabel: {
						display: true,
						labelString: "GDP (PPP)"
					}
				}]
			}
		}
	});
});