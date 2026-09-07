import sympy as sp
import numpy as np
import plotly.graph_objects as go

formula_str = input("Введи формулу от x и y: ")

x, y = sp.symbols('x y')

expr = sp.sympify(formula_str)

f = sp.lambdify((x, y), expr, 'numpy')

x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)

Z = f(X, Y)

# 7. Построить график
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])
fig.update_layout(
    title=formula_str,
    scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z')
)
fig.show()