
bldgTransactions <- read.csv("~/Desktop/355-1st.csv")
summary(bldgTransactions)
numRows = nrow(bldgTransactions)
regressionSize = 5
#chartMin <- min(bldgTransactions$Initial.Price)
chartMin <- 0
chartMax <- max(bldgTransactions$Resale.Price)
g_range <- range(chartMin, chartMax)

for(x in regressionSize+1:numRows) {
  regressionStart = x - regressionSize
  regressionEnd = x-1 
  regressionRange <- bldgTransactions[regressionStart:regressionEnd,]
  par(mfrow	=	c(1,1))	
  plot(regressionRange$Initial.Price, 
       regressionRange$Resale.Price,
       ylim=g_range,
       xlim=g_range,
       ylab="Resale Price",
       xlab="Initial Price")
  title(bldgTransactions[x,]$Resale.Date)
  for(y in 1:regressionStart-1)
  {
#      myColor = paste("gray",y*2, sep='')
      points(bldgTransactions[y,]$Initial.Price, 
             bldgTransactions[y,]$Resale.Price,
             col="gray86")
  }
  
  points(bldgTransactions[x,]$Initial.Price, 
         bldgTransactions[x,]$Resale.Price,
         col="red")

  myRegression <- lm(regressionRange$Resale.Price ~ 
       0 + regressionRange$Initial.Price)
  abline(myRegression, col = "blue")  
  
  readline(prompt="Press [enter] to continue")
  
}