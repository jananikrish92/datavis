function renderHeatMap(heatChart,heatxSel,heatySel,heatzSel,heatMapDim,heatMapGroup){
 // alert();
  heatChart
    .width(45 * 20 )
    .height(45 * 5 )
    .dimension(heatMapDim)
    .group(heatMapGroup)
    .xAxisLabel(heatxSel)
    .yAxisLabel(heatySel)
    .keyAccessor(function(d) { return +d.key[0]; })
    .valueAccessor(function(d) { return +d.key[1]; })
    .colorAccessor(function(d) { return +d.value; })
    .title(function(d) {
        return x +" : " + d.key[0] + "\n" +
               y +" : " + d.key[1] + "\n" +
               z +" : " + d.value + " $";})
    .colors(["#22f31e","#edf8b1","#b64747","#b62f63","#41b6c4","#1d91c0","#225ea8","#253494","#081d58"])
    .calculateColorDomain();
}