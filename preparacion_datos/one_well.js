var var_names = ["DailyProdOil", "DailyProdGas", "DailyProdWater", "DailyPressureBHP", "DailyWaterInjVolume", "DailyGasInjVolume", "DailyInjPressureBHP"]
var var_colors = ["#4F7942", "#CC0000", "#1034A6", "#DAA520", "#1034A6", "#CC0000","#DAA520"]
var dataset = "";
var window_number = 1;


d3.json("/get-data", function(error, root){
  dataset = root;
  window_number = 1;
  variable_visualization(dataset,window_number);
});


function inc_decrease(value){
  window_number = window_number+value;
  if(window_number<=0){
    window_number = 2
  }
  if(window_number>2){
    window_number = 1
  }
  updateDiv(window_number);
}

function updateDiv(attribute){
  window_number = attribute;
  variable_visualization(dataset,attribute);
}


function variable_visualization(data,attribute){
  d3.select("#my_dataviz").selectAll("svg").remove();
  if(attribute==1){
    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 10, bottom: 10, left: 65},
    width = 1050 - margin.left - margin.right,
    height = 700 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    var svg = d3.select("#my_dataviz")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Add X axis --> it is a date format
    var x = d3.scaleTime()
    .domain(d3.extent(data, function(d) { return d3.timeParse("%Y-%m-%d")(d.date); }))
    .range([ 0, width]);
    svg.append("g")
    .attr("transform", "translate(0," + (height-10)+ ")")
    .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear()
    .domain([d3.min(data, function(d) { return +d.original_value; }), d3.max(data, function(d) { return +d.original_value; })])
    .range([ (height-10), 0 ]);
    svg.append("g")
    .call(d3.axisLeft(y));

    // Add the area
    svg.append("path")
    .datum(data)
    .attr("fill", "#cce5df")
    .attr("stroke", "#69b3a2")
    .attr("stroke-width", 1.5)
    .attr("d", d3.area()
    .x(function(d) { return x(d3.timeParse("%Y-%m-%d")(d.date)) })
    .y0(y(0))
    .y1(function(d) { return y(d.original_value) }));

    // Add the area
    svg.append("path")
    .datum(data)
    .attr("stroke", "gray")
    .attr("stroke-width", 1.5)
    .attr("class", "line")
    .style("stroke-dasharray", ("3, 3"))
    .attr("fill", "none")
    .attr("d", d3.line()
    .x(function(d) { return x(d3.timeParse("%Y-%m-%d")(d.date)) })
    .y(function(d,i) { return y(d.highlighted_value) }));

    // add circles to svg
    svg.selectAll("circle")
    .data(data).enter()
    .append("circle")
    .attr("cx", function (d) { return x(d3.timeParse("%Y-%m-%d")(d.date)); })
    .attr("cy", function (d) {  return y(d.original_value); })
    .attr("r", function (d,i) {
      if(d.outlier_flag!="0"){
        return "3px";
      }
      else{
        return "0px";
      }
    })
    .attr("fill", function (d,i) {
      if(d.outlier_flag==="-1"){
         return "blue";
       }
       else if (d.outlier_flag==="1") {
         return "red";
       }
    })
    .attr("stroke", "none")
   }
   else{
     var selected_var =  $('#variableSelect').selectpicker().val();
     var pos_height = (selected_var.length * 110) + 350;

     // set the dimensions and margins of the graph
     var margin = {top: 10, right: 10, bottom: 10, left: 65},
      width = 1050 - margin.left - margin.right,
      height = pos_height - margin.top - margin.bottom;

     // append the svg object to the body of the page
     var svg = d3.select("#my_dataviz")
     .append("svg")
     .attr("width", width + margin.left + margin.right)
     .attr("height", height + margin.top + margin.bottom)
     .append("g")
     .attr("transform","translate(" + margin.left + "," + margin.top + ")");

    // Add X axis --> it is a date format
    var x = d3.scaleTime()
    .domain(d3.extent(data, function(d) { return d3.timeParse("%Y-%m-%d")(d.date); }))
    .range([ 0, width]);

    svg.append("g")
    .attr("transform", "translate(0," + 10+ ")")
    .call(d3.axisBottom(x));

    // Add Y axis
    var y_0 = d3.scaleLinear()
    .domain([d3.min(data, function(d) { return +d.original_value; }),
    d3.max(data, function(d) { return +d.original_value; })])
    .range([ 150, 50 ]);
    let xAxisLeftGenerator0 = d3.axisLeft(y_0);
    xAxisLeftGenerator0.ticks(5);
    svg.append("g")
    .call(xAxisLeftGenerator0);

    // Add the area
    svg.append("path")
    .datum(data)
    .attr("fill", "#B2BEB5")
    .attr("stroke", "#3B444B")
    .attr("stroke-width", 1.5)
    .attr("d", d3.area()
    .x(function(d) { return x(d3.timeParse("%Y-%m-%d")(d.date)) })
    .y0(y_0(0))
    .y1(function(d) { return y_0(d.original_value) }));

    // Y axis label:
    // text label for the y axis
    svg.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left+15)
    .attr("x",0 - 100)
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .text("Projected");

    // Add Y axis
    var y_1 = d3.scaleLinear()
    .domain([d3.min(data, function(d) { return +d.highlighted_value; }),
    d3.max(data, function(d) { return +d.highlighted_value; })])
    .range([ 260, 160 ]);

    let xAxisLeftGenerator1= d3.axisLeft(y_1);
    xAxisLeftGenerator1.ticks(5);
    svg.append("g").call(xAxisLeftGenerator1);

    // Add the area
    svg.append("path")
    .datum(data)
    .attr("stroke", "gray")
    .attr("stroke-width", 1.5)
    .attr("class", "line")
    .style("stroke-dasharray", ("3, 3"))
    .attr("fill", "none")
    .attr("d", d3.line()
    .x(function(d) { return x(d3.timeParse("%Y-%m-%d")(d.date)) })
    .y(function(d,i) { return y_1(d.highlighted_value) }));

    // add circles to svg
    svg.selectAll("circle")
    .data(data).enter()
    .append("circle")
    .attr("cx", function (d) { return x(d3.timeParse("%Y-%m-%d")(d.date)); })
    .attr("cy", function (d) {  return y_1(d.highlighted_value); })
    .attr("r", function (d,i) {
      if(d.outlier_flag!="0"){
        return "1px";
      }
      else{
        return "0px";
      }
    })
    .attr("fill", function (d,i) {
      if(d.outlier_flag==="-1"){
        return "blue";
      }
      else if (d.outlier_flag==="1") {
        return "red";
      }
    })
    .attr("stroke", "none");

    // Y axis label:
    svg.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left+15)
    .attr("x",0 - 210)
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .text("Highlighted");

    var i;
    for (i = 0; i < selected_var.length; i++) {
      var var_index = -1;

      try{
        var_index = var_names.indexOf(selected_var[i]);
        var_color = var_colors[var_index];
      }
      catch(error){
        var_color = "#7F7F7F";
      }

      // Add Y axis
      var y_var = d3.scaleLinear()
      .domain([d3.min(data, function(d) { return +d.multidim_original[i]; }),
      d3.max(data, function(d) { return +d.multidim_original[i]; })])
      .range([ 260 + (100*(i+1)) + (10*(i+1)), 160+ (100*(i+1)) + (10*(i+1))]);

      let xAxisLeftGeneratorVar= d3.axisLeft(y_var);
      xAxisLeftGeneratorVar.ticks(5);
      svg.append("g").call(xAxisLeftGeneratorVar);

      // Add the area
      svg.append("path")
      .datum(data)
      .attr("fill", var_color)
      .attr("stroke", var_color)
      .attr("stroke-width", 1.5)
      .attr("d", d3.area()
      .x(function(d) { return x(d3.timeParse("%Y-%m-%d")(d.date)) })
      .y0(y_var(0))
      .y1(function(d) { return y_var(d.multidim_original[i]) }));

      // Y axis label:
      // Y axis label:
      svg.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left+15)
      .attr("x",0 - (260 + (100*(i+1)) + (10*(i+1))+ 160+ (100*(i+1)) + (10*(i+1)))/2)
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text(selected_var[i]);
    }
  }
}


function distribution_visualization(data){
   lineDistributionData = data;
   try{
     strategyName = document.getElementById("strategySelect").value;
   }
   catch(e){
     strategyName = ""
   }
   try{
     neg_value = document.getElementById("negAnomaliesInput").value;
   }
   catch(e){
     neg_value = -5;
   }
   try{
     pos_value = document.getElementById("posAnomaliesInput").value;
   }
   catch(e){
     pos_value = 5;
   }
   // append the svg object to the body of the page
   var svg_distribution = d3.select("#my_distribution")
   .append("svg")
   .attr("width", 350)
   .attr("height", 200)
   .append("g");

   // add the x Axis
   var x_distribution = d3.scaleLinear()
   .domain([-5, 5])
   .range([0, 350]);
   svg_distribution.append("g")
   .attr("transform", "translate(0,178)")
   .call(d3.axisBottom(x_distribution));

   max_y = Math.max.apply(Math,lineDistributionData.map(function(o){return o.y;}));

   // add the y Axis
   var y_distribution = d3.scaleLinear()
   .domain([max_y,1])
   .range([5, 180]);
   svg_distribution.append("g")
   .attr("transform", "translate(175,0)")
   .call(d3.axisLeft(y_distribution));

   // Add the area;
   svg_distribution.append("path")
   .attr("class", "mypath")
   .datum(lineDistributionData)
   .attr("fill", "#69b3a2")
   .attr("opacity", ".8")
   .attr("stroke", "#000")
   .attr("stroke-width", 1)
   .attr("stroke-linejoin", "round")
   .attr("d",  d3.line().curve(d3.curveBasis)
       .x(function(d) { return x_distribution(d.x); })
       .y(function(d) { return y_distribution(d.y); })
   );
   if (strategyName=="moving_zscore"){
     svg_distribution.append("rect")
             .attr("x", x_distribution(-5))
             .attr("y", y_distribution(max_y))
             .attr("width", x_distribution(neg_value))
             .attr("height", 200)
             .attr("opacity", 0.3)
             .attr("fill", "blue");
     svg_distribution.append("rect")
             .attr("x", x_distribution(pos_value))
             .attr("y", y_distribution(max_y))
             .attr("width", x_distribution(5))
             .attr("height", 200)
             .attr("opacity", 0.3)
             .attr("fill", "red");
    svg_distribution.append("line")          // attach a lin
             .style("stroke", "blue")  // colour the line
             .attr("x1", x_distribution(neg_value))     // x position of the first end of the line
             .attr("y1", y_distribution(0))      // y position of the first end of the line
             .attr("x2", x_distribution(neg_value))     // x position of the second end of the line
             .attr("y2", y_distribution(max_y));    // y position of the second end of the line
    svg_distribution.append("line")          // attach a line
             .style("stroke", "red")  // colour the line
             .attr("x1", x_distribution(pos_value))     // x position of the first end of the line
             .attr("y1", y_distribution(0))      // y position of the first end of the line
             .attr("x2", x_distribution(pos_value))     // x position of the second end of the line
             .attr("y2", y_distribution(max_y));    // y position of the second end of the line
  }
}
