// prevent error: "0: 'optionChanged' is not defined"
optionChanged = () => {}
samples = {}

// 1. Use the D3 library to read in samples.json.
d3.json("samples.json").then(data => {
	samples = data

	// populate "Test Subject ID No."
	samples.names.forEach(function(name) {
		option = d3.select("#selDataset").append("option")
		option.text(name)
		option.node().value = name
	})

	metadata()
	bar_chart()
	bubble_chart()
	gauge_chart()
})

// 2. Create a horizontal bar chart with a dropdown menu to display the top 10 OTUs found in that individual.
//    * Use sample_values as the values for the bar chart.
//    * Use otu_ids as the labels for the bar chart.
//    * Use otu_labels as the hovertext for the chart.
bar_chart = function() {
	value = d3.select("#selDataset").node().value
	data = samples.samples.filter((data) => {return data.id == value})[0]
	data = d3.zip(data.otu_ids, data.sample_values, data.otu_labels)
	top10 = data.sort((a,b) => b[1]-a[1]).slice(0,10).sort((a,b) => (a[1]-b[1]) || a[0]-b[0])

	var layout = {}

	var data = [{
		type: "bar",
		orientation: 'h',
		x: top10.map(d => d[1]),
		y: top10.map(d => "OTU " + d[0]),
		text: top10.map(d => d[2])
	  }]

	  Plotly.newPlot("bar", data, layout);
}

// 3. Create a bubble chart that displays each sample.
//    * Use otu_ids for the x values.
//    * Use sample_values for the y values.
//    * Use sample_values for the marker size.
//    * Use otu_ids for the marker colors.
//    * Use otu_labels for the text values.
bubble_chart = function() {
	value = d3.select("#selDataset").node().value
	data = samples.samples.filter((data) => {return data.id == value})[0]
	data = d3.zip(data.otu_ids, data.sample_values, data.otu_labels)

	var layout = {}

	var data = [{
		mode: "markers",
		y: data.map(d => d[1]),
		x: data.map(d => d[0]),
		marker: {size: data.map(d => d[1]*0.75), color: data.map(d => d[0]), colorscale: 'Earth'},
		text: data.map(d => d[2])
	  }]

	  Plotly.newPlot("bubble", data, layout);
}

// 4. Display the sample metadata, i.e., an individual's demographic information.
metadata = function() {
	value = d3.select("#selDataset").node().value
	data = samples.metadata.filter((data) => {return data.id == value})[0]
	d3.select(".panel-body").html("")
	p = d3.select(".panel-body").append("p")
	keys = Object.keys(data)
	keys.forEach(function(key) {
		p.html(p.html() + key + ": " + data[key] + "<br>");
	})
}

// 5. Display each key-value pair from the metadata JSON object somewhere on the page.
// These instructions are the same as step 4

// 6. Update all of the plots any time that a new sample is selected.
d3.select("#selDataset").on("change", () => {
	metadata();
	bar_chart();
	bubble_chart();
	gauge_chart();
})

// Advanced Challenge Assignment (Optional)
// The following task is advanced and therefore optional.
// * Adapt the Gauge Chart from https://plot.ly/javascript/gauge-charts/ to plot the weekly washing frequency of the individual.
// * You will need to modify the example gauge code to account for values ranging from 0 through 9.
// * Update the chart whenever a new sample is selected.

// Will be skipping this part, as gauge plots are highly customized pie charts,
// and implementations are not standardized.
gauge_chart = function() {}