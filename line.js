function renderLine(chart,x,y,dim,grp){
  alert(typeof(x)+":"+typeof(y));
 chart
      .width(500)
      .height(520)
      .x(d3.scale.linear().domain([0,12]))  
      .renderArea(false)
      .brushOn(true)
      .renderDataPoints(true)
      .clipPadding(10)
      .yAxisLabel(y)
      .xAxisLabel(x)
      .dimension(dim)
      .group(grp).brushOn(true)
      .margins({left:100,right:5,top:50,bottom:50})
      .renderLabel(true);
}