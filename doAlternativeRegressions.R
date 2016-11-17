bldgTransactions <- read.csv("~/Desktop/CentreCt.csv")
summary(bldgTransactions)
numRows = nrow(bldgTransactions)
regressionSize = 4
for(x in regressionSize+1:numRows) {
  regressionStart = x - regressionSize
  regressionEnd = x-1 
  regressionRange <- bldgTransactions[regressionStart:regressionEnd,]
  ordinaryLeastSq <- lm(regressionRange$Resale.Price ~ 
                          regressionRange$Initial.Price)
  ordinaryLeastSqSummary <- summary(ordinaryLeastSq)
#  print(ordinaryLeastSqSummary$coefficients[,1])
  
  percentageLeastSq <- lm(regressionRange$Resale.Price ~ 
                          regressionRange$Initial.Price, 
                          weights = 1/regressionRange$Resale.Price^2)    

    percentageLeastSqSummary <- summary(percentageLeastSq)
#  print(percentageLeastSqSummary$coefficients[,1])
      
  #include quantreg package
  leastAbsoluteDev = rq(regressionRange$Resale.Price ~ 
                          regressionRange$Initial.Price)
  leastAbsoluteDevSqSummary <- summary(leastAbsoluteDev)
  print(leastAbsoluteDevSqSummary$coefficients[,1])
 
  #include mcr package
#  deming <- mcreg(regressionRange$Initial.Price, 
#                regressionRange$Resale.Price, 
#                method.reg = "Deming")
#  print(deming@para[,1])
  
  paBa <- mcreg(regressionRange$Initial.Price, 
                  regressionRange$Resale.Price, 
                  method.reg = "PaBa")
  print(paBa@para[,1])
  
#  readline(prompt="Press [enter] to continue")
  
}  




#myPredictions <- data.frame(resaleDate = as.Date(character()),
#                            actualPrice = integer(0), 
#                            ordinaryLeastSq = integer(0),
#                            percentageLeastSq = integer(0),
#                            leastAbsoluteDev = integer(0)
#                            ) 