import pandas as pd

#Creating a data frame object
#Data frame is a constructor to create a Data frame object
# print(pd.DataFrame({"Yes":[50,120],"No":[60,70]}))

# print(pd.DataFrame({"Bob":["I liked it","It was awful"], "Sue":["Preety Good","Bland"]},index=['Product A','Product B']))

# print(pd.Series([1,2,3,4,5]))

# pd.read_csv("Users\Asus\Downloads\practice.csv")
df = pd.DataFrame({
    "Name":["Laura","Jothem"],
    "Age":[18,19],
    "Gender":["female","male"]
})

# print(df)
# print(df["Age"])

ages = pd.Series([10,27,87],name = "Age")
# print(ages)
print(df["Age"].max())
print(ages.max())

print(df.describe())

print(df.info())