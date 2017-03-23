var map = new Object(); // or var map = {};

var scatterxSel;
var scatterySel;
var scatterzSel;

var histxSel;
var histySel;

var linexSel;
var lineySel;

var heatxSel;
var heatySel;
var heatzSel;

var scatterChart1;
var scatterChart2;
var lineGraph;
var heatChart;
var HistChart;
var multiscatterchart;
var typeRingChart;


var multixSel;
var multiySel;
var multizSel;

var piexSel;
var pieySel;

function initialiseGraphVariables(){
	scatterxSel = '';
	scatterySel = '';
	scatterzSel = '';
	histxSel = '';
	histySel = '';
	linexSel = '';
	lineySel = '';
	heatxSel = '';
	heatySel = '';
	heatzSel = '';
	multixSel = '';
	multiySel = '';
	multizSel = '';
	piexSel = '';
	pieySel = '';
}




function renderGraph(){
	initialiseGraphVariables();
    var $xcoordinateSel = $("#xcoordinate option:selected").text();
    var $ycoordinateSel = $("#ycoordinate option:selected").text();
    var $zcoordinateSel = $("#zcoordinate option:selected").text();

    if($xcoordinateSel == 'Select'){
        alert('Please Select the x coordinate ');
        return;
    }
    if($ycoordinateSel == 'Select'){
      alert('Please Select the y-coordinate ');
      return;
    }
    if( $("#graphtype option:selected").text() == 'Scatter Plot' ||  $("#graphtype option:selected").text() == 'Heat Map' || $("#graphtype option:selected").text() == 'Multi Scatter'){
      if($zcoordinateSel == 'Select'){
        alert('Please Select the z-coordinate for '+$("#graphtype option:selected").text());
        return;
      }
    }

    map[$("#graphtype option:selected").text()] = $xcoordinateSel+","+$ycoordinateSel+","+$zcoordinateSel;
       
	for(var key in map)
	{
		if (key === 'Scatter Plot'){
			scatterxSel = map[key].split(',')[0];
			scatterySel = map[key].split(',')[1];
			scatterzSel = map[key].split(',')[2];	
		}else if (key === 'Line'){
			linexSel = map[key].split(',')[0];
			lineySel = map[key].split(',')[1];
		}else if (key === 'Histogram'){
			histxSel = map[key].split(',')[0];
			histySel = map[key].split(',')[1];
		}else if (key === 'Heat Map'){
			heatxSel = map[key].split(',')[0];
			heatySel = map[key].split(',')[1];
			heatzSel = map[key].split(',')[2];		
		}
		else if (key === 'Multi Scatter'){
		      multixSel = map[key].split(',')[0];
		      multiySel = map[key].split(',')[1];
		      multizSel = map[key].split(',')[2];    
		}		
		     else if (key === 'Pie'){
		      piexSel = map[key].split(',')[0];
		      pieySel = map[key].split(',')[1];  
		}   
	}
	renderAllGraphs();
}

function convertDataToStringOrNumber(d,coordinate){
    if(isNaN(d[coordinate]))
      return d[coordinate];
    else
      return +d[coordinate];
}
function renderAllGraphs(){
	d3.csv("dataset.csv", function(error, data) {
		 data.forEach(function(x) {
			   if(scatterxSel != '' && scatterySel != '' && scatterzSel != ''){
				    x[scatterxSel] = convertDataToStringOrNumber(x,scatterxSel);
				    x[scatterySel] = convertDataToStringOrNumber(x,scatterySel);
				    x[scatterzSel] = convertDataToStringOrNumber(x,scatterzSel);
			   }
			   if(heatxSel != '' && heatySel != '' && heatzSel != ''){
				    x[heatxSel] = convertDataToStringOrNumber(x,heatxSel);
				    x[heatySel] = convertDataToStringOrNumber(x,heatySel);
				    x[heatzSel] = convertDataToStringOrNumber(x,heatzSel);
			   }
			   if(linexSel != '' && lineySel != ''){
				    x[linexSel] = convertDataToStringOrNumber(x,linexSel);
				    x[lineySel] = convertDataToStringOrNumber(x,lineySel);
			   }
			   if(histxSel != '' && histySel != ''){
				    x[histxSel] = convertDataToStringOrNumber(x,histxSel);
				    x[histySel] = convertDataToStringOrNumber(x,histySel);
			   }

         if(multixSel != '' && multiySel != '' && multizSel != ''){
            x[multixSel] = convertDataToStringOrNumber(x,multixSel);
            x[multiySel] = convertDataToStringOrNumber(x,multiySel);
            x[multizSel] = convertDataToStringOrNumber(x,multizSel);
         }

          if(piexSel != '' && pieySel != ''){
            x[piexSel] = convertDataToStringOrNumber(x,piexSel);
            x[pieySel] = convertDataToStringOrNumber(x,pieySel);
         }
		});
		
		var ndx = crossfilter(data),
		scatterDim1 =  ndx.dimension(function(d){return loadMultiDimensions(d,scatterxSel,scatterySel);}),
		scatterDim2 =  ndx.dimension(function(d){return loadMultiDimensions(d,scatterxSel,scatterzSel);}),
		scatterGroup1 = scatterDim1.group(),
		scatterGroup2 = scatterDim2.group(),
		lineDim = ndx.dimension(function(d) {return loadDimensions(d,linexSel);}),
		lineGroup = lineDim.group().reduceSum(function(d) {return loadDimensions(d,lineySel);}),
		histDim = ndx.dimension(function(d) {return loadDimensions(d,histxSel);}),
    	histGroup = histDim.group().reduceCount(function(d){return loadDimensions(d,histySel);}),
        typeDim  = ndx.dimension(function(d) {return loadDimensions(d,piexSel);}),
        likePertype = typeDim.group().reduceSum(function(d) {return loadDimensions(d,pieySel);}),
        multiscatterDim =  ndx.dimension(function(d){return loadMultiDimensions(d,multizSel,multixSel);}),
        multiscatterGroup = multiscatterDim.group().reduceSum(function(d) {return loadDimensions(d,multiySel);})
        runDim = ndx.dimension(function(d) { return [+d[heatxSel], +d[heatySel]]; }),
        runGroup = runDim.group().reduceSum(function(d) { return +d[heatzSel]; });
    	var symbolScale = d3.scale.ordinal().range(d3.svg.symbolTypes);
		var symbolAccessor = function(d) {return symbolScale(d.key[0]); };
	  

   		if(scatterxSel!='' && scatterySel !=''){
			scatterChart1 = dc.scatterPlot("#scatter1");	
			renderScatter(scatterChart1,scatterxSel,scatterySel,scatterDim1,scatterGroup1);
		}
		if(scatterxSel !='' && scatterzSel != ''){
			scatterChart2 = dc.scatterPlot("#scatter2");	
			renderScatter(scatterChart2,scatterxSel,scatterzSel,scatterDim2,scatterGroup2);	
		}
		if(linexSel!='' && lineySel !=''){
			lineGraph = dc.lineChart("#line");
			renderLine(lineGraph,linexSel,lineySel,lineDim,lineGroup);
		}
		if(histxSel != '' && histySel != ''){
			HistChart  = dc.barChart("#HistChart");
			renderHistogram(HistChart,histxSel,histySel,histDim,histGroup);
		}
	    if(multixSel != '' && multiySel != '' && multizSel != ''){
	      multiscatterchart = dc.seriesChart("#multiscatter");
	      renderMultiscatter(multiscatterchart,multixSel,multiySel,multizSel,multiscatterDim,multiscatterGroup,symbolAccessor);
	    }
	   if(heatxSel != '' && heatySel != '' && heatzSel != ''){
	      heatChart = dc.heatMap("#heatMapChart");  
	      heatChart  .width(45 * 20 + 80)
	    .height(45 * 5 + 40)
	    .dimension(runDim)
	    .group(runGroup)
	    .keyAccessor(function(d) { return +d.key[0]; })
	    .valueAccessor(function(d) { return +d.key[1]; })
	    .colorAccessor(function(d) { return +d.value; })
	    .title(function(d) {
	        return heatxSel+":   " + d.key[0] + "\n" +
	               heatySel+":  " + d.key[1] + "\n" +
	               heatzSel+": " + d.value + " $";})
	    .colors(["#ffffd9","#edf8b1","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0","#225ea8","#253494","#081d58"])
	    .calculateColorDomain();
	  
	    }
	    if(piexSel != '' && pieySel != '')
	    {
	      typeRingChart   = dc.pieChart("#chart-ring-year")
	      renderPieChart(typeRingChart,piexSel,pieySel,typeDim,likePertype)
	    }
	  
    	dc.renderAll();
	});	
}

function renderHeatMap(chart,x,y,z,dim,grp,heatkeyAccessor,heatvalueAccessor){
  alert("hello heat");
}
function loadDimensions(d,x){
var m;
	if(x != ''){
     m = convertDataToStringOrNumber(d,x);
		return [m]
	}else{
		return;	
	}
}

function loadMultiDimensions(d,x,y){
	var m,n;
  if(x != '' && y != ''){
      if(isNaN(d[x]))
            m = d[x];
      else
            m = +d[x];

      if(isNaN(d[y]))
            n = d[y];
      else
            n = +d[y];
  		return[m,n]
	}else{
		return []	
	}
}

function loadxCoordinates(){
   var $select = $("#graphtype option:selected").text();
   $.ajax({
      type: 'GET',
      datatype:"jsonp",
      crossDomain: true,
      data: {graphType:$select},
      url: "http://127.0.0.1:5000/fetchxCoordinates",
      success: function (responseData, textStatus, jqXHR) {

          var dbData = JSON.parse(responseData);
          var $xcoordinateSel = $('#xcoordinate');
          $('#xcoordinateDiv').css("display","block");
          $('#xcoordinateDiv').css("visibility","visible");
    	  $xcoordinateSel
          .find('option')
          .remove();

          $xcoordinateSel.append('<option id="Select">Select</option>');
          
          $.each(dbData, function(key, val){
            $xcoordinateSel.append('<option id="' + val.x + '">' + val.x + '</option>');
          });
      }
    });
}

function loadzCoordinates(){
   var $select = $("#graphtype option:selected").text();
   var $xCoordVal = $("#xcoordinate option:selected").text();
   var $yCoordVal = $("#ycoordinate option:selected").text();
   if($select == 'Scatter Plot' || $select == 'Heat Map' || $select == 'Multi Scatter'){
	   $.ajax({
	      type: 'GET',
	      datatype:"jsonp",
	      crossDomain: true,
	      data: {graphType:$select,xCoord:$xCoordVal,yCoord:$yCoordVal},
	      url: "http://localhost:5000/fetchzCoordinates",
	      success: function (responseData, textStatus, jqXHR) {

		  var dbData = JSON.parse(responseData);
		  var $zcoordinateSel = $('#zcoordinate');
		  $('#zcoordinateDiv').css("display","block");
		  $('#zcoordinateDiv').css("visibility","visible");
	    	  $zcoordinateSel
		  .find('option')
		  .remove();

		  $zcoordinateSel.append('<option id="Select">Select</option>');
		  
		  $.each(dbData, function(key, val){
		    $zcoordinateSel.append('<option id="' + val.z + '">' + val.z + '</option>');
		  });
	      }
	    });
   }else{
	  var $zcoordinateSel = $('#zcoordinate');
	  $('#zcoordinateDiv').css("display","none");
	  $('#zcoordinateDiv').css("visibility","hidden");
   }
}

function loadyCoordinates(){
   var $select = $("#graphtype option:selected").text();
   var $xCoordVal = $("#xcoordinate option:selected").text();

   $.ajax({
      type: 'GET',
      datatype:"jsonp",
      crossDomain: true,
      data: {graphType:$select,xCoord:$xCoordVal},
      url: "http://localhost:5000/fetchyCoordinates",
      success: function (responseData, textStatus, jqXHR) {

          var dbData = JSON.parse(responseData);
          var $ycoordinateSel = $('#ycoordinate');
          $('#ycoordinateDiv').css("display","block");
          $('#ycoordinateDiv').css("visibility","visible");
    	  $ycoordinateSel
          .find('option')
          .remove();

          $ycoordinateSel.append('<option id="Select">Select</option>');
          
          $.each(dbData, function(key, val){
            $ycoordinateSel.append('<option id="' + val.y + '">' + val.y + '</option>');
          });
      }
    });
}
