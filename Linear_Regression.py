"""
https://ithelp.ithome.com.tw/articles/10197248
找出符合資料規律的直線，就叫線性迴歸。
"""
#####
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets

x, y = datasets.make_regression(n_samples=200, n_features=1, n_targets=1, noise=10)
# print(x)
plt.scatter(x, y, linewidths=0.01)  # 繪製散點圖--畫點
# plt.show()
model = LinearRegression()
model.fit(x, y)
predict = model.predict(x[:200])

plt.plot(x, predict, c='red')  # 透過x,y來畫出圖形--畫線
plt.show()
