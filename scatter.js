function renderScatter(chart,x,y,dim,group){
chart.width(400)
    .height(400)
    .x(d3.scale.linear().domain([0, 20]))
    .yAxisLabel(y)
    .xAxisLabel(x)
    .clipPadding(10)
    .dimension(dim).brushOn(true)
    .excludedOpacity(0.5)
    .group(group);

}
