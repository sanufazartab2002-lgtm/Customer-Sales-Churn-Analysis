import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

data = {
    "Customer_ID":[101,102,103,104,105],
    "Age":[25,26,27,29,50],
    "Gender":["Female","Male","Female","Male","Female"],
    "City":["Delhi","Noida","Gurgoan","Bangalore","Mumbai"],
    "Subscription_type":["Basic","Premium","Basic","Premium","Standard"],
    "Monthly_spend":[500,1200,1500,2000,1000],
    "Tenure_Months":[12,24,36,48,60],
    "Total_Purchase":[60,20,5,20,10],
    "Support_Calls":[3,2,5,7,4],
    "Churn":["Yes","No","Yes","No","Yes"],
}

df = pd.DataFrame(data)
print(df)

print("\nTotal Customers:",len(df))
print("\nCustomers Data:")
print(df)

print("\nData Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nChurn Count:")
print(df["Churn"].value_counts())

print("\nAverage Monthly Spend:",df["Monthly_spend"].mean())

print("\nChurn Rate:",(df["Churn"] == "Yes").mean()* 100,"%")

print("\nCustomers by City:")
print(df["City"].value_counts())

print("\nCustomers by Subscription Type:")
print(df["Subscription_type"].value_counts())

print("\nAverage Monthly Spend by Subscription:")
print(df.groupby("Subscription_type")["Monthly_spend"].mean())

print("\nAverage Monthly spend by City:")
print(df.groupby("City")["Monthly_spend"].mean())

print("\nAverage Tenure by Churn:")
print(df.groupby("Churn")["Tenure_Months"].mean())

print("\nAverage Support Calls by Churn:")
print(df.groupby("Churn")["Support_Calls"].mean())

print("\nAverage Monthly spend by Churn:")
print(df.groupby("Churn")["Monthly_spend"].mean())

Churn_subscription = pd.crosstab(df["Subscription_type"],df["Churn"])
print("\nChurn by subscription Type:")
print(Churn_subscription)

Churn_subscription.plot(kind="bar")

plt.title("Churn by subscription Type")
plt.xlabel("Subscription Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()

monthly_spend_churn = df.groupby("Churn")["Monthly_spend"].mean()
monthly_spend_churn.plot(kind="bar")

plt.title("Average Monthly Spend by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Spend")
plt.xticks(rotation=0)
plt.show()

support_churn = df.groupby("Churn")["Support_Calls"].mean()
support_churn.plot(kind="bar")

plt.title("Average Support Calls by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Support Calls")
plt.xticks(rotation=0)
plt.show()

tenure_churn = df.groupby("Churn")["Tenure_Months"].mean()
tenure_churn.plot(kind="bar")

plt.title("Average Tenure by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Tenure (Months)")
plt.xticks(rotation=0)
plt.show()

print("\nFinal Business Insights:")
print("Total Customer:",len(df))
print("Churned Customers:",(df["Churn"] == "Yes").sum())
print("Churn Rate:",(df["Churn"] == "Yes").mean()* 100,"%")
print("Average Monthly Spend:",(df["Monthly_spend"].mean()))

print()



























