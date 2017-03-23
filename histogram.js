function renderHistogram(HistChart,x,y,dim,grp){
 
    HistChart
    	.width(500)
    	.height(500)
        .brushOn(true)
        .dimension(dim)
        .group(grp)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .elasticX(true)
        .elasticY(true) 
        .margins({ top: 10, left: 20, right: 30, bottom: 50 })
        .renderlet(function (chart) {
                          chart.selectAll("g.x text")
                            .attr('dx', '-30')
                            .attr('transform', "rotate(-90)");
                      });
    HistChart.yAxis().ticks(10);
}

function remove_empty_bins(source_group) {
    return {
        all:function () {
            return source_group.all().filter(function(d) {
                return +d.value >= 0;
            });
        }
    };
}
