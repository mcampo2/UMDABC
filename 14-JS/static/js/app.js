// from data.js
var tableData = data;

// YOUR CODE HERE!

// Using the UFO dataset provided in the form of an array of 
// JavaScript objects, write code that appends a table to your
// web page and then adds new rows of data for each UFO sighting.
for(var i = 0; i < tableData.length; i++) {
	tr = d3.select("tbody").append("tr")
	tr.append("td").html(tableData[i].datetime)
	tr.append("td").html(tableData[i].city)
	tr.append("td").html(tableData[i].state)
	tr.append("td").html(tableData[i].country)
	tr.append("td").html(tableData[i].shape)
	tr.append("td").html(tableData[i].durationMinutes)
	tr.append("td").html(tableData[i].comments)
}

// Use a date form in your HTML document and write JavaScript 
// code that will listen for events and search through the 
// date/time column to find rows that match user input.

// do not redirect on "enter"
d3.select("form").on("submit", e => d3.event.preventDefault())

// Part 1
/*d3.select("input").on("change", e => {
	// clear table
	d3.select("tbody").html("")
	// filter data
	tableData = data.filter(d => d.datetime == d3.event.target.value)
	// print data to table
	for(var i = 0; i < tableData.length; i++) {
		tr = d3.select("tbody").append("tr")
		tr.append("td").html(tableData[i].datetime)
		tr.append("td").html(tableData[i].city)
		tr.append("td").html(tableData[i].state)
		tr.append("td").html(tableData[i].country)
		tr.append("td").html(tableData[i].shape)
		tr.append("td").html(tableData[i].durationMinutes)
		tr.append("td").html(tableData[i].comments)
	}
})*/

// Level 2: Multiple Search Categories (Optional)
// Using multiple `input` tags and/or select dropdowns, write JavaScript code 
// so the user can to set multiple filters and search for UFO sightings

filter = function() {
	// clear table
	d3.select("tbody").html("")

	// filter data
	tableData = data.filter(d => {
		return d.datetime.toLowerCase().includes(datetime.property("value").toLowerCase()) &&
		d.city.toLowerCase().includes(city.property("value").toLowerCase()) &&
		d.state.toLowerCase().includes(state.property("value").toLowerCase()) &&
		d.country.toLowerCase().includes(country.property("value").toLowerCase()) &&
		d.shape.toLowerCase().includes(shape.property("value").toLowerCase())
	})
	
	// print data to table
	for(var i = 0; i < tableData.length; i++) {
		tr = d3.select("tbody").append("tr")
		tr.append("td").html(tableData[i].datetime)
		tr.append("td").html(tableData[i].city)
		tr.append("td").html(tableData[i].state)
		tr.append("td").html(tableData[i].country)
		tr.append("td").html(tableData[i].shape)
		tr.append("td").html(tableData[i].durationMinutes)
		tr.append("td").html(tableData[i].comments)
	}
}

form = d3.select(".list-group")

// 1. `date/time`
datetime = d3.select("input")
datetime.on("change", e => {
	filter()
})

// 2. `city`
city = form.append("li")
city.classed("filter list-group-item", true)
city.append("label").text("Enter a City")
city = city.append("input")
city.classed("form-control", true)
city.on("change", e => {
	filter()
})

// 3. `state`
state = form.append("li")
state.classed("filter list-group-item", true)
state.append("label").text("Enter a State")
state = state.append("input")
state.classed("form-control", true)
state.on("change", e => {
	filter()
})

// 4. `country`
country = form.append("li")
country.classed("filter list-group-item", true)
country.append("label").text("Enter a Country")
country = country.append("input")
country.classed("form-control", true)
country.on("change", e => {
	filter()
})

// 5. `shape`
shape = form.append("li")
shape.classed("filter list-group-item", true)
shape.append("label").text("Enter a Shape")
shape = shape.append("input")
shape.classed("form-control", true)
shape.on("change", e => {
	filter()
})