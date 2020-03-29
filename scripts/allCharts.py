# Modify Chart[i].py scripts before running the script
import chart1
import chart2
import chart3

print("""
<!-- HTML starts -->
<div class="chartWrapper">
    <div class="container container-fluid chartAreaWrapper" style="position: relative; height:350px; width: 90vw; margin-left:2px;">
        <canvas id="myChart1" height="300" width="350"></canvas>
    </div>
    <div class="container container-fluid chartAreaWrapper" style="position: relative; height:350px; width: 90vw; margin-left:2px;">
        <canvas id="myChart2" height="300" width="350"></canvas>
    </div>
    <div class="container container-fluid chartAreaWrapper" style="position: relative; height:710px; width: 90vw; margin-left:2px;">
        <canvas id="myChart3" height="680" width="350"></canvas>
        <p style="font-size: 0.65em;">* Please refer to the update date and time on the <a href="/">homepage</a></p>
    </div>
    <p><i><small>Note: The above Graphs/Charts are for the representation purpose only.</small></i></p>
</div>

<!-- HTML ends -->


<!-- Javascript Starts -->
<script>""")

# temp_yAxisData = [chart1.yAxisData , chart2.yAxisData]
# temp_xAxisData = [chart1.xAxisData , chart2.xAxisData]

for i in range(1,4):
    yAxisData = eval('chart' + str(i) + '.' + 'yAxisData')
    xAxisData = eval('chart' + str(i) + '.' + 'xAxisData')
    legendTitle = eval('chart' + str(i) + '.' + 'legendTitle')
    chartTitle = eval('chart' + str(i) + '.' + 'chartTitle')
    colorsGenerated = eval('chart' + str(i) + '.' + 'colorsGenerated')

    typeOfChart = eval('chart' + str(i) + '.' + 'typeOfChart')
    axis = eval('chart' + str(i) + '.' + 'axis')

    print(f"""
    var yAxisValues{i} = { yAxisData };
    var legendTitle{i} = "{ legendTitle }";
    var xAxisValues{i} = { xAxisData };
    var chartTitle{i} = "{ chartTitle }";
    var colorsGenerated{i} = { colorsGenerated };
    
    //Assigning the values for chart 
    var data{i} = {{
            labels: yAxisValues{i},
            datasets: [{{
                label: legendTitle{i},
                data: xAxisValues{i},   
                backgroundColor: colorsGenerated{i}           
            }}]
        }};


    var ctx = document.getElementById('myChart{i}').getContext('2d');
    
    var myChart{i} = new Chart(ctx, {{
        type: '{ typeOfChart }',
        data: data{i},
        
        options: {{
            title: {{
                display: true,
                text: chartTitle{i}
            }},
            maintainAspectRatio: false,
            responsive: false,
            scales: {{
                { axis }: [{{
                    ticks: {{
                        fontSize: 10,
                        beginAtZero: true
                    }}
                }}]
            }}
        }}
    }});
    """)
