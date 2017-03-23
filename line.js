function renderLine(chart,x,y,dim,grp){
 chart
      .width(500)
      .height(500)
      .x(d3.scale.linear().domain([0,12]))
      .renderArea(false)
      .brushOn(true)
      .renderDataPoints(true)
      .clipPadding(10)
      .yAxisLabel(y)
      .dimension(dim)
      .group(grp).brushOn(true)
      .margins({left:100,right:5,top:10,bottom:30});
}
