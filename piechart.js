function renderPieChart(chart,x,y,z,dim,grp){
chart
.width(200)
    .height(400)
    .dimension(alarmLevels_dim)
    .group(alarmsPerLevel)
    .legend(dc.legend().x(0).y(0).itemHeight(12).gap(5).horizontal(1).legendWidth(90).itemWidth(95));
}