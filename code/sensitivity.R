library(sensitivitymv)

#file with matched pairs of focal persons
dat = read.csv("Sensitivity analysis/table_matched.csv", header = TRUE)

#compute p-value
senmv(dat, gamma = 1.17, method = NULL, inner = 0, trim = 2.5, lambda = 1/2,
      tau = 0, TonT=FALSE)

#amplification of sensitivity
amplify(1.17, 3)

vector=numeric(0)
for(i in 1:1000)
{vector[i]<-(amplify(1.17, seq(1.45, 5, length.out = 1000)[i]))}

x<- seq(1.45, 5, length.out = 1000)

