<script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('number', 'identical');
        data.addColumn('number', 'halfmatch');
        data.addColumn('number', 'conflict');
        data.addColumn('number', 'interesting_conflict');
        data.addColumn('number', 'pos_not_name_conflict');
        data.addColumn('number', 'pos_only_conflict');
        data.addColumn('number', 'no_match');
        data.addRows(1);
        data.setValue(0, 0, 339572);
        data.setValue(0, 1, 216676);
        data.setValue(0, 2, 2014);
        data.setValue(0, 3, 31552);
        data.setValue(0, 4, 1);
        data.setValue(0, 5, 1);
        data.setValue(0, 6, 3217);


        var dataView = new google.visualization.DataView(data);
        dataView.setColumns([{calc: function(data, row) { return ''; }, type:'string'}, 0, 1, 2, 3, 4, 5, 6]);

        var chart = new google.visualization.BarChart(document.getElementById('chart_divfile-1570234575-28738809'));
        chart.draw(dataView, {width: 400, height: 240,
                              legend:{position: 'none'},
                              colors: ['#b6ffff', '#a0a0ff', '#ffa0a0', '#ff3c3c', '#ffa0a2', '#a1a0a0', '#a2a0a0'],
                         });
      }
    </script><div class="chart" id="chart_divfile-1570234575-28738809"></div><table class="totalnums" >       <tr><td bgcolor="#b6ffff" width="10px">&nbsp;</td><td align="right"> 57% </td><td>identical</td><td align="right"> 339572</td></tr>
       <tr><td bgcolor="#a0a0ff" width="10px">&nbsp;</td><td align="right"> 37% </td><td>halfmatch</td><td align="right"> 216676</td></tr>
       <tr><td bgcolor="#ffa0a0" width="10px">&nbsp;</td><td align="right"> 0% </td><td>conflict</td><td align="right"> 2014</td></tr>
       <tr><td bgcolor="#ff3c3c" width="10px">&nbsp;</td><td align="right"> 5% </td><td>interesting_conflict</td><td align="right"> 31552</td></tr>
       <tr><td bgcolor="#ffa0a2" width="10px">&nbsp;</td><td align="right"> 0% </td><td>pos_not_name_conflict</td><td align="right"> 1</td></tr>
       <tr><td bgcolor="#a1a0a0" width="10px">&nbsp;</td><td align="right"> 0% </td><td>pos_only_conflict</td><td align="right"> 1</td></tr>
       <tr><td bgcolor="#a2a0a0" width="10px">&nbsp;</td><td align="right"> 1% </td><td>no_match</td><td align="right"> 3217</td></tr>
</table>