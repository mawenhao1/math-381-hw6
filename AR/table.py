import plotly.graph_objects as go
import numpy as np

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

value =[['A']]
for j in range(1):
    colomn = []
    for i in range(1):
        contents=""
        with open("stratA vs stratR.txt") as f:
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