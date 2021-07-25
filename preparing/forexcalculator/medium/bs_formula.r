library(sde)

# define the return and volatility
mu=0.14
sigma=0.25
nt=50
n=2^8

# initial price
P0=1.19542
T=1/12

# generate Brownian motion sample paths of currency price
dt=T/n
t=seq(0, T, by=dt)
B <- matrix(rep(0, length(t)*nt), nrow=nt)
for (i in 1:nt) {
   B[i,]=GBM(x=P0,r=mu,sigma=sigma,T=T,N=n)
}

# plotting the Price Brownian motion sample paths
# boundary for the simulated price
ymax=max(B)
ymin=min(B)
plot(t,B[1,],t='l',ylim=c(ymin, ymax),col=1,ylab="Price S(t)", xlab="Time t")
for (i in 2:nt)
{
    lines(t, B[i,], t='l', ylim=c(ymin, ymax),col=i)
}
