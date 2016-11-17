
bldgTransactions <- read.csv("~/Desktop/333-1st.csv")
summary(bldgTransactions)
numRows = nrow(bldgTransactions)
regressionSize = 5
g_range <- range(325000, 1300000)

for(x in regressionSize+1:numRows) {
  regressionStart = x - regressionSize
  regressionEnd = x-1 
  regressionRange <- bldgTransactions[regressionStart:regressionEnd,]
  ordinaryLeastSq <- lm(regressionRange$Resale.Price ~ 
                          regressionRange$Initial.Price)

  par(mfrow	=	c(1,1))	
  plot(regressionRange$Initial.Price, regressionRange$Resale.Price,
       ylim=g_range,
       xlim=g_range,
       ylab="Resale Price",
       xlab="Initial Price")
  points(bldgTransactions[x,]$Initial.Price, 
         bldgTransactions[x,]$Resale.Price,
         col="red")
  title(bldgTransactions[x,]$Resale.Date)

#  abline(ordinaryLeastSq)
  ordinaryLeastSqSummary <- summary(ordinaryLeastSq)
  print(ordinaryLeastSqSummary$coefficients[,1])
  
   percentageLeastSq <- lm(regressionRange$Resale.Price ~ 
                          regressionRange$Initial.Price, 
                          weights = 1/regressionRange$Resale.Price^2)    
  #  percentageLeastSqSummary <- summary(percentageLeastSq)
  #  print(percentageLeastSqSummary$coefficients[,1])

#  abline(percentageLeastSq, col = "blue")
  #   
  #include quantreg package
   leastAbsoluteDev = rq(regressionRange$Resale.Price ~ 
                          regressionRange$Initial.Price)
#  leastAbsoluteDevSqSummary <- summary(leastAbsoluteDev)
  #print(leastAbsoluteDevSqSummary$coefficients[,1])
#  abline(leastAbsoluteDev, col = "purple")
  #
  #include mcr package
#  deming <- mcreg(regressionRange$Initial.Price, 
#                  regressionRange$Resale.Price, 
#                  method.reg = "Deming")
#  abline(deming, col = "green")
      #  print(deming@para[,1])
  
#  paBa <- mcreg(regressionRange$Initial.Price, 
#                    regressionRange$Resale.Price, 
#                    method.reg = "PaBa")
#  abline(paBa, col = "brown")
    #  print(paBa@para[,1])
  
  readline(prompt="Press [enter] to continue")
  
}