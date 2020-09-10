import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression   #Linear Regression Algorithm
plt.style.use('seaborn-darkgrid')
import yfinance as yf                               #yahoo finance is used to extract data

Df = yf.download('GLD','2019-01-01','2021-08-15',auto_adjust=True)
Df=Df[['Close']]
Df=Df.dropna()                                      #Drop rows with missing value
Df['S_3']=Df['Close'].rolling(window=3).mean()
Df['S_9']=Df['Close'].rolling(window=9).mean()
Df['S_14']=Df['Close'].rolling(window=14).mean()
Df['next-day-price']=Df['Close'].shift(-1)
Df=Df.dropna()
X=Df[['S_3','S_9','S_14']]                          #Independent Variable
Y=Df['next-day-price']                              #Dependent variable
Df.Close.plot(figsize=(14,7),color='r')
t=0.8
t=int(t*len(Df))
#TRAIN DATASET
X_train=X[:t]
Y_train=Y[:t]
#TEST DATASET
X_test=X[t:]
Y_test=Y[t:]

linear=LinearRegression().fit(X_train,Y_train)     #Creating Linear Regression Model
print("Linear Regression Model")
print("Gold ETF Price(y) = %.2f * 3 Days Moving Average(x1) \ + %.2f * 9 Days Moving Average(x2) \ + %.2f * 9 Days Moving Average(x2) +  %.2f (constant)" % (linear.coef_[0],linear.coef_[1],linear.coef_[2],linear.intercept_))

#PREDICTING THE PRICE
predicted_price=linear.predict(X_test)
predicted_price=pd.DataFrame(predicted_price,index=Y_test.index,columns=['price'])
#PLOTTING THE GRAPH BETWEEN PREDICTED PRIZES AND ACTUAL PRIZES
predicted_price.plot(figsize=(14,7))
Y_test.plot()
plt.legend(['predicted_price','actual_price'])
plt.ylabel("Gold ETF Prices")
plt.title("Gold Prices Detection")

r2_score=linear.score(X[:t],Y[:t])*100             #R2-Scored
float("{0:.2f}".format(r2_score))
print(r2_score)

gold = pd.DataFrame()
gold['price']=Df[t:]['Close']
gold['predicted_price_next_day']=predicted_price
gold['actual_price_next_day']=Y_test
gold['gold_returns']=gold['price'].pct_change().shift(-1) #pct_change() calculates percentage change of the current value and the previous value
gold['signal']=np.where(gold.predicted_price_next_day.shift(1) < gold.predicted_price_next_day,1,0)
gold['strategy_returns']=gold.signal * gold['gold_returns']

((gold['strategy_returns']+1).cumprod()).plot(figsize=(14,7),color='g')
plt.ylabel("Cumulative Returns")
plt.show()
data=yf.download('GLD','2019-01-01','2021-08-15',auto_adjust=True)
data['S_3']=data['Close'].rolling(window=3).mean()
data['S_9']=data['Close'].rolling(window=9).mean()
data['S_14']=data['Close'].rolling(window=14).mean()
data=data.dropna()
data['predicted_gold_price']=linear.predict(data[['S_3','S_9','S_14']])
data['signal']=np.where(data.predicted_gold_price.shift(1) < data.predicted_gold_price,"wait for next day","Buy it today")
data.tail(7)
print(data)

