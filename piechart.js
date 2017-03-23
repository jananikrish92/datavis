function renderPieChart(chart,x,y,dim,grp){
	      chart
		    .width(350).height(200)
		    .dimension(dim)
		    .group(grp)
		    .innerRadius(0)	
		    .legend(dc.legend().x(20).y(100).itemHeight(12).gap(5).horizontal(1).legendWidth(90).itemWidth(95));
}