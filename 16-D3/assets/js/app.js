// @TODO: YOUR CODE HERE!

// You need to create a scatter plot between two of the data variables such as
// Healthcare vs. Poverty or Smokers vs. Age.

// Using the D3 techniques we taught you in class, create a scatter plot that
// represents each state with circle elements. You'll code this graphic in the
// app.js file of your homework directory—make sure you pull in the data from
// data.csv by using the d3.csv function. Your scatter plot should ultimately
// appear like the image at the top of this section.

// * Include state abbreviations in the circles.
// * Create and situate your axes and labels to the left and bottom of the chart.
// * Note: You'll need to use python -m http.server to run the visualization.
//   This will host the page at localhost:8000 in your web browser.

// Step 1: Set up our chart
//= ================================
var svgWidth = 800;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Step 2: Create an SVG wrapper,
// append an SVG group that will hold our chart,
// and shift the latter by left and top margins.
// =================================
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Step 3:
// Import data from the data.csv file
// =================================
d3.csv("./assets/data/data.csv").then(function(data) {
  // Step 4: Parse the data
  // Format the data and convert to numerical and date values
  // =================================
  // Format the data
  data.forEach(function(data) {
    data.poverty = +data.poverty;
    data.healthcare = +data.healthcare;
  });

  // Step 5: Create Scales
  //= ============================================
  var xLinearScale = d3.scaleLinear()
    .domain([8, d3.max(data, d => d.poverty)])
    .range([0, width]);

  var yLinearScale = d3.scaleLinear()
    .domain([4, d3.max(data, d => d.healthcare)])
    .range([height, 0]);

  // Step 6: Create Axes
  // =============================================
  var bottomAxis = d3.axisBottom(xLinearScale);//.tickFormat(d3.timeFormat("%d-%b"));
  var leftAxis = d3.axisLeft(yLinearScale);

  
  // Step 7: Append the axes to the chartGroup
  // ==============================================
  // Add bottomAxis
  chartGroup.append("g").attr("transform", `translate(0, ${height})`).call(bottomAxis);

  // Add leftAxis to the left side of the display
  chartGroup.append("g").call(leftAxis);


  // Step 8: append elements to data points
  // ==============================================
  // circles
  var circlesGroup = chartGroup.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "10")
    .attr("fill", "lightblue");

  // text
  var textsGroup = chartGroup.selectAll("texts")
    .data(data)
    .enter()
    .append("text")//.attr("text-anchor", "middle")
    .attr("font-size", "10px")
    .attr("font-weight", "bold")
    .attr("x", d => xLinearScale(d.poverty))
    .attr("y", d => yLinearScale(d.healthcare))
    .attr("dy", "0.35em")
    .attr("text-anchor", "middle")
    .attr("fill", "white")
    .text(d => d.abbr);

  // x-axis label
  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 20})`)
    .attr("text-anchor", "middle")
    .attr("font-size", "16px")
    .attr("font-weight", "bold")
    .text("In Poverty (%)");

  // y-axis label
  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", `${0 - margin.left/2}`)
    .attr("x", `${0 - height / 2}`)
    .attr("text-anchor", "middle")
    .attr("font-size", "16px")
    .attr("font-weight", "bold")
    .text("Lacks Healthcare (%)");

}).catch(function(error) {
  console.log(error);
});