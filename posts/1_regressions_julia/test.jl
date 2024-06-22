using Plots
using GLM


x = range(0, 1, length=10)
#Generate data : 
f = rand(10) .* x

# Check the data :
size(f)

plot(
	scatter(x,f, label = "data"),
	title = "Generating Random Data",
	ylabel = "Random variable",
	xlabel = "x",
)

model = lm(@formula(f ~ x), (;f, x))
GLM.coeftable(model)
model

coefs = GLM.coef(model)
plot!((x) -> coefs[1] + coefs[2] * x, label="model", 
	title = "Simple linear regression")

using LaTeXStrings
plot(scatter(x,f, label = false),
    (x) -> coefs[1] + coefs[2] * x, label=latexstring("y=$(coefs[1]) + $(coefs[2]) * x"))

plot!(legend=:outerbottom, legendcolumns=1)

X = [ones(length(x)) x] 
(X\f)

# 2 



# Generating random data :
x = range(0,1, length = 10)
w,y,z = (rand(10) for _ in 1:5)

# Plotting the data :
plot(scatter(x, y, z, marker_z = w, label="data"))

plotlyjs()
# We plot :
plot(scatter(x, y, z;
		marker_z = w,
		markersize = 2, 
		label = "data"))

X = [ones(length(x)) x z w]
coefs = X\y

ul= x

u= [s for t in ul, s in ul]
v= [t for t in ul, s in ul]

u

pl= PlotlyJS.Plot(PlotlyJS.surface(x=ul, y=ul, z = ul,
         showscale=true),
         Layout(width=500, height=400, scene_camera_eye=attr(x=1.95, y=1, z=0.75)))


using Plots; plotlyjs()

x = y = range(0,1, length = 10)
X = [ones(length(x)) x y]
coefs = X\z
model = coefs[1] .+ coefs[2] * x .+ coefs[3] * y
plot(x, y, model, st=:surface)

x=range(-2,stop=2,length=100)
y=range(sqrt(2),stop=2,length=100)
f(x,y) = x*y-x-y+1
plot(x,y,f,st=:surface,camera=(-30,30))