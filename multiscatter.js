function renderMultiscatter(multiscatterchart,multixSel,multiySel,multizSel,multiscatterDim,multiscatterGroup,symbolAccessor){

 var subChart = function(c) {
    return dc.scatterPlot(c)
        .symbol(symbolAccessor)
        .symbolSize(8)
        .highlightedSize(10)
  };
  multiscatterchart
    .width(800)
    .height(480)
    .chart(subChart)
    .x(d3.scale.linear().domain([0,25]))
    .brushOn(false)
    .yAxisLabel(multiySel)
    .xAxisLabel(multixSel)
    .clipPadding(10)
    .elasticY(true)
    .dimension(multiscatterDim)
    .group(multiscatterGroup)
    .mouseZoomable(true)
    .shareTitle(false) // allow default scatter title to work
    .seriesAccessor(function(d) {return multizSel+":" + d.key[0];})
    .keyAccessor(function(d) {return +d.key[1];})
    .valueAccessor(function(d) {return +d.value;})
    .legend(dc.legend().x(350).y(350).itemHeight(13).gap(5).horizontal(1).legendWidth(140).itemWidth(70));
  //chart.yAxis().tickFormat(function(d) {return d3.format(',d')(d);});
  multiscatterchart.margins().left += 40;
}