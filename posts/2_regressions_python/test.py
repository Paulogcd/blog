# libraries : 
import numpy
import sklearn.linear_model
import pandas
import scipy

# initializing variables : 
x,y,z,w = [numpy.random.rand(100) for _ in range(4)]
a = numpy.ones(len(x))
model = sklearn.linear_model.LinearRegression()

data = {"c1": [a],"c2": [x],"c3": [y]}
regressors = pandas.DataFrame(data)

z = numpy.array([[z]])

X1 = numpy.array([[a]])
X2 = numpy.array([a,x])
X3 = numpy.array([a,x,y])

X1.shape
X2.shape
X3.shape

x.shape
a.shape
len(regressors)
regressors.shape
z.shape

test = regressors.reshape(100,3)
X = numpy.matrix(a,x,y)

regressors = numpy.column_stack((a, x, y))

# scipy.stats.linregress(regressors,z)

# does not work : 
model.fit(regressors,z)
model.coef_
model.intercept_
sklearn.metrics.classification_report(y_pred = model, y_true = z)

# To display results : 

import statsmodels.api

# Create the object :
model = statsmodels.api.OLS(z,regressors)
# Run the model :
results = model.fit()

# Print the regression table : 
print(results.summary())

results.params

Y = z
X1 = x
X2 = y
X3 = w

import statsmodels.api as sm

X = np.column_stack((X1, X2, X3))

# Add a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(Y, X).fit()
print(model.summary())

# Get the coefficients
intercept, coef1, coef2, coef3 = model.params


import numpy as np

# Create a mesh grid for the independent variables
X1_range = np.linspace(X1.min(), X1.max(), 10)
X2_range = np.linspace(X2.min(), X2.max(), 10)
X1_grid, X2_grid = np.meshgrid(X1_range, X2_range)

# Calculate the predicted values using the regression coefficients
Y_grid = intercept + coef1 * X1_grid + coef2 * X2_grid + coef3 * (X3.mean())

import plotly.graph_objects as go

# Create a 3D scatter plot of the original data points
scatter = go.Scatter3d(
    x=X1, y=X2, z=Y,
    mode='markers',
    marker=dict(size=5, color=Y, colorscale='Viridis')
)

# Create a 3D surface plot of the regression plane
surface = go.Surface(
    x=X1_grid, y=X2_grid, z=Y_grid,
    colorscale='Viridis', opacity=0.5
)

# Combine the scatter plot and surface plot
fig = go.Figure(data=[scatter, surface])

# Set plot titles and axis labels
fig.update_layout(
    title='3D Visualization of Multinomial Linear Regression',
    scene=dict(
        xaxis_title='X1',
        yaxis_title='X2',
        zaxis_title='Y'
    )
)

# Show the plot
fig.show()