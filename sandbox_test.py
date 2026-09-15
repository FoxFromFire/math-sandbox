import sympy as sp
import numpy as np
import plotly.graph_objects as go
from sympy.parsing.sympy_parser import parse_expr

x, y = sp.symbols('x y')

while True:
    formula_str = input("Введи формулу от x и y: ")
    if formula_str.strip().lower() in ('выход', 'exit', 'quit'):
        print("Пока!")
        break

    try:
        expr = parse_expr(formula_str, transformations="all")
    except (sp.SympifyError, SyntaxError):
        print("Ошибка: не могу разобрать формулу. Проверь синтаксис.")
        continue

    f = sp.lambdify((x, y), expr, 'numpy')

    x_vals = np.linspace(-5, 5, 50)
    y_vals = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x_vals, y_vals)

    Z = f(X, Y)
    if np.isscalar(Z):
        Z = np.full_like(X, Z)
    Z = np.array(Z, dtype=float)
    Z = np.where(np.isfinite(Z), Z, np.nan)

    fig = go.Figure(data=[go.Surface(
        x=X, y=Y, z=Z,
        colorscale='Viridis',
        contours_z=dict(show=True, usecolormap=True, project_z=True))])

    fig.update_layout(
        title=formula_str,
        scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
        autosize=True,
        margin=dict(l=0, r=0, b=0, t=40)
    )
    fig.show()