import pandas as pd

data_df = pd.read_csv("E:\Wolftech\wolftech-learning-tirtharaj\data-science-adv-python\CarPricesData.csv",
                      encoding="latin-1")

# print(data_df)
# print(data_df.head(n=5))
# print(data_df.shape)
# x = data_df.shape
# # print('The number of rows is:', x[0])
# # print('The number of columns is:', x[1])
data_df = data_df.drop_duplicates()
# y = data_df.shape
# print(y)
# print('No of duplicate rows deleted:', x[0]-y[0])
print(data_df.shape)
