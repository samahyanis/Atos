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
	new Chart(document.getElementById("chart7"), {
		type: 'horizontalBar',
		data: {
			labels: ["ISUTI056-ISU_HIST_CONSO_ANN", "ISUTI086-ISU_MDR_ECHE1_DETEC", "ISUTI66K-ISU_IDENT_IBAN_ANONYM", "ISUTI502-FICA_TRAN_PIEC_FIGL", "ISUTI042B-ISU_OPTI_TURPE","ISUTI086-ISU_MDR_ECHE1_DETEC","ISUTI495-ISU_CALCUL_FACTURAT_ES","ISUTI66L-ISU_ANONYM_IBAN","NDEBJCHG",
			"NDATE001-ISU_MAJ_ZDATE_NA", "ISUTI50Q-ISU_PRE_ANLYSE_NA", "ISUTI02W-ISU_GO_NA_HORS_HEBDO", "ISUTI400-ISU_NO_GO_NACOMP", "ISUTI440-ISU_SPLIT4_D21", "ISUTI4A9-ISU_INT_IND_G",
			"ISUTI411-ISU_CALCUL_FACTURAT", "ISUTI412-ISU_FACTURATION_ISU", "ISUTI071-ISU_INT_MODIF_CONT", "ISUTI025-ISU_ITF_GINKO14", "ISUTI62T-ISU_ITF_G14_GAZ","ISUTI420-ISU_ITF_GINKO13",
			"ISUTI421-ISU_ITF_GINKO10","ISUTI40K-ISU_MDR_SOUSC_G","ISUTI054-FICA_RAPPROCHM_AUTO","ISUTI00Y-ISU_MDR_AF_PROC_PART","ISUTI069-FICA_CYCLE_RELANCE_PROP","ISUTI057-FICA_CYCLE_RELANCE_ACT",
			"ISUTI01Z-ISU_PROG_AL_DFKKKOBW", "ISUTI01E-FICA_MARQ_CREAN_DOU","ISUTI01F-FICA_TRAN_CREAN_DOU","ISUTI065-FICA_ENCAISS_DECAISS1","ISUTI42V-EDIT_ISU_SP_B_NRJ_XML",
			"ISUTI42W-EDIT_CONCAT_FACT_XML","EDITE673","EDITESGL","ISUTI018-ISU_PROG_MAJ_BP"],
			datasets: [{
				label: "Durée (Secondes)",
				backgroundColor: ["#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7",, "#673ab7", "#673ab7", "#673ab7", "#673ab7"
				, "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7"
				, "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7", "#673ab7"],
				data: [3680, 5268, 7345, 78441, 43312, 85214, 4589, 9865, 2500, 4521, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589, 4589
				, 4539, 45452, 4239, 459, 489, 45639, 789, 4599, 45559]
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
	});
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