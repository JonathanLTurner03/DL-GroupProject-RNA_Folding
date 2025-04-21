import plotly.graph_objects as go
import pandas as pd
import numpy as np

data = pd.read_csv("./data_comparison.csv")

x_pred, y_pred, z_pred = [], [], []
x_true, y_true, z_true = [], [], []

for idx, row in data.iterrows():
    x_pred.append(row[0])
    y_pred.append(row[1])
    z_pred.append(row[2])

    x_true.append(row[4])
    y_true.append(row[5])
    z_true.append(row[6])

use_normalized: bool = True

x_true = np.array(x_true)
y_true = np.array(y_true)
z_true = np.array(z_true)

x_pred = np.array(x_pred)
y_pred = np.array(y_pred)
z_pred = np.array(z_pred)

# Optionally normalize
if use_normalized:
    x_true = (x_true - x_true.mean()) / x_true.std()
    y_true = (y_true - y_true.mean()) / y_true.std()
    z_true = (z_true - z_true.mean()) / z_true.std()

    x_pred = (x_pred - x_pred.mean()) / x_pred.std()
    y_pred = (y_pred - y_pred.mean()) / y_pred.std()
    z_pred = (z_pred - z_pred.mean()) / z_pred.std()

# Marker traces (dots only)
trace_pred_markers = go.Scatter3d(
    x=x_pred, y=y_pred, z=z_pred,
    mode='markers',
    marker=dict(size=6, color='blue'),
    name='Model Prediction'
)

trace_true_markers = go.Scatter3d(
    x=x_true, y=y_true, z=z_true,
    mode='markers',
    marker=dict(size=6, color='red'),
    name='Ground Truth'
)

# Line traces (connects points in order)
trace_pred_lines = go.Scatter3d(
    x=x_pred, y=y_pred, z=z_pred,
    mode='lines',
    line=dict(color='grey', width=2),
    name='Prediction Backbone'
)

trace_true_lines = go.Scatter3d(
    x=x_true, y=y_true, z=z_true,
    mode='lines',
    line=dict(color='lightgrey', width=2),
    name='Ground Truth Backbone'
)

# Combine all into one figure
fig = go.Figure(data=[trace_pred_markers, trace_pred_lines, trace_true_markers, trace_true_lines])

fig.update_layout(
    scene=dict(
        xaxis_title='X (Å)',
        yaxis_title='Y (Å)',
        zaxis_title='Z (Å)'
    ),
    title='3D Structure Comparison: Model vs Ground Truth'
)

fig.show()
