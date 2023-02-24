import plotly.graph_objects as go
import numpy as np

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

value =[['B14', 'B15', 'B16', 'B17', 'B18','B19']]
for j in range(1):
    colomn = []
    for i in range(14, 20):
        contents=""
        with open("stratB" +str(i) +" vs stratRan.txt") as f:
            contents = f.read()
        contents = contents[1:-1]
        temp = np.fromstring(contents, sep = ",")
        result = [min(temp), max(temp)]
        colomn.append(result)
    value.append(colomn)
 

fig = go.Figure(data=[go.Table(
  header=dict(
    values=[' ','R'],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['left','center'],
    font=dict(color='white', size=12)
  ),
  cells=dict(
    values=value,
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
    align = ['left', 'center'],
    font = dict(color = 'darkslategray', size = 11)
    ))
])

fig.show()