function renderPieChart(chart,x,y,dim,grp){
      chart
	    .width(500).height(300)
	    .dimension(dim)
	    .group(grp)
	    .innerRadius(0);
	if(x=="Post Month"){
	    chart.legend(dc.legend().x(20).y(20).itemHeight(12).gap(5).horizontal(1).legendWidth(90).itemWidth(95).legendText(function (d) {

		var index = d.name;
		return Months[index]+":"+d.data;
	   }));
	}else if(x =="Post Weekday"){
		chart.legend(dc.legend().x(20).y(20).itemHeight(12).gap(5).horizontal(1).legendWidth(90).itemWidth(95).legendText(function (d) {

		var index = d.name;
		return Weekday[index]+":"+d.data;
	   }));
	}else{
		chart.legend(dc.legend().x(20).y(20).itemHeight(12).gap(5).horizontal(1).legendWidth(90).itemWidth(95).legendText(function (d) {

		var index = d.name;
		return d.name+":"+d.data;
	   }));
	}
}
