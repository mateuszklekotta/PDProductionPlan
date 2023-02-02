import plotly.express as px
import pandas as pd

import dbconnection

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
fig1 = px.timeline(dbconnection.data, x_start="Start", x_end="Finish", y="Task")
fig1.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig1.show()
