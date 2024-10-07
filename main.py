import streamlit as st

st.title("Activity 3 - CSS145-BM3-Group 2")

st.write("Group Members: Drilon, Rafael Francisco V. - 2021130296 - Remigaraki") 

import pandas as pd
import numpy as np
import os


import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

df = pd.read_csv('Electronic_sales_Sep2023-Sep2024.csv')
df

st.write(df)

#SECTION I

df.info()
df.isna().sum()
df.describe()
df['Customer ID'].value_counts()
df['Age'].value_counts()
df['Gender'].value_counts()
df['Loyalty Member'].value_counts()
df['Product Type'].value_counts()
df['SKU'].value_counts()
df['Rating'].value_counts()
df['Order Status'].value_counts()
df['Payment Method'].value_counts()
df['Total Price'].value_counts()
df['Unit Price'].value_counts()
df['Quantity'].value_counts()
df['Purchase Date'].value_counts()
df['Shipping Type'].value_counts()
df['Add-ons Purchased'].value_counts()
df['Add-on Total'].value_counts()


st.subheader("#SECTION II.")

st.subheader("Jeska Chan")
#insert code here

st.subheader("Kael Herrera")
#insert code here

st.subheader("Rolando Magat")
#insert code here

st.subheader("Rafael Francisco V. Drilon")

def loyalty_member_distribution():
    loyalty_memberships = df['Loyalty Member'].value_counts()
    plt.pie(loyalty_memberships, labels=loyalty_memberships.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Loyalty Members (Yes or No)')
    plt.axis('equal')
    plt.show()
    st.pyplot(plt)
    plt.clf()

loyalty_member_distribution()
st.write("The distribution of loyalty members is shown in the pie chart, where 21.7% of people are loyalty members and 78.3% of people are not. The greater portion, shown in blue, is made up of non-members, showing that the vast majority of people do not use the loyalty program.")

#Rafa Drilon

def bar_chart_product_types():
    colors = ['#ff9999', '#ffcc99', '#99ffcc', '#99ccff', '#c2c2f0']
    product_counts = df['Product Type'].value_counts()
    product_types = product_counts.index
    counts = product_counts.values

    plt.bar(product_types, counts, color=colors[:len(product_types)])
    plt.title('Distribution of Product Types')
    plt.ylabel('Number of Products')
    plt.xlabel('Product Type')
    plt.show()
    st.pyplot(plt)
    plt.clf()

bar_chart_product_types()
st.write("The distribution of product types is depicted in the bar chart, with smartphones having the largest count at about 6,000 units. Smartwatches, laptops, and tablets come in close second with around 4,000 units each. With a total of about 2,000 units, headphones have the lowest quantity. The relative distribution of each type of product is easily visualized thanks to the use of gentle pastel colors in the chart to distinguish between the categories. In this dataset, smartphones are the most common product type overall, while headphones are the least common.")


st.subheader("Nathaniel James Carrillo")

def line_graph_ordertrend():
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

    completed_orders = df[df['Order Status'] == 'Completed']

    purchase_date_counts = completed_orders.groupby('Purchase Date')['Order Status'].count()

    moving_average = purchase_date_counts.rolling(window=7).mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(purchase_date_counts.index, purchase_date_counts.values, label='Original', alpha=0.5, color='red')
    plt.plot(moving_average.index, moving_average.values, label='7-Day Moving Average', color='purple')
    plt.xlabel('Purchase Date')
    plt.ylabel('Number of Orders')
    plt.title('Number of Orders Over Time')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)
    plt.clf()

st.title('Orders Trend Dashboard')
st.header('Completed Orders Over Time')
line_graph_ordertrend()

st.write("This line graph shows the number of orders with respect to the purchase date. The red line shows the original data, while the purple line is the moving average of the number of orders per week. In both cases, there is significant growth around the start of 2024, from an average of 18.17 orders to 43.57. This trend may be due to increasing demand following the end of the global pandemic, new technology and videogame releases, and holiday shopping such as during Christmas. Before 2024, the number of orders peaked at 28 on October 7 and was the lowest at only 8 on October 26. During 2024, orders peaked at 63 on January 28 and was the lowest at 24 on February 8.")

def pie_chart_shippingtype():
    colors = ['blue', 'red', 'yellow', 'green', 'orange']
    shipping_counts = df['Shipping Type'].value_counts()
    plt.pie(shipping_counts, labels=shipping_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Distribution of Shipping Type')
    plt.axis('equal')
    plt.show()
    st.pyplot(plt)
    plt.clf()

st.title('Customer Preferences')
st.header('Preferred Shipping Type')
pie_chart_shippingtype()

st.write('The pie chart above shows the distribution of shipping types used by the customers. The data indicates that the preferred shipping method is Standard at 33.6% followed by Express and Overnight at 16.8%. The least preferred method is Expedited and Same day shipping at 16.4%.')


st.subheader("#SECTION III.")

st.write("Insights from our Data Visualization and Data Analysis:")


st.write("#1. ***Customer Demographics***")
st.write("- The majority of the sales for the electronics company came from the age group of 49 to 51 years, making them the primary market segment for electronic products.")
st.write("- Given the average customer age and the gender of the majority (male), it reinforces the conclusion that middle-aged male adults are significant consumers of electronics.")
st.write("- While both genders are nearly evenly represented in the electronics market, men lead in product purchasing behavior.")
st.write("- Additionally, the data indicates that 21.7% of people are loyalty members, compared to 78.3% who are not. This suggests that even with a relatively low number of loyalty memberships, customers continue to purchase products regardless of their membership status.")


st.write("#2. ***Customer Buying Behavior***")
st.write("- A target market of cost-conscious customers who predominantly prefer prices within the $0 to $4,000 range.")
st.write("- The most common product rating is 3, indicating that the customers are expressing a mediocre satisfaction on the electronic products. Hence, there is still room for improvement in product quality and customer satisfaction.")
st.write("- Given the dataset, the customers bought smartphones the most.")
st.write("- These data could imply that the electronic company should consider developing other high-quality and innovative electronic products, apart from smartphones, that is still within the range of affordability of its consumers.")


st.write("#3. ***Preferred Shipping & Payment Method***")
st.write("- The majority of customers favor credit cards and online banking as their preferred payment methods.")
st.write("- A plurality of the customers use Standard shipping for the delivery of their products at 33.6%, while Expedited and Same Day as their least favored at 16.4%.")


st.write("#4. ***Orders over time***")
st.write("- There was a sizable increase in orders following 2024, which retained its range.")
st.write("- The average before 2024 is 18.17 and the average in 2024 is 43.57.")
st.write("- Overall, the orders peaked at 63 on January 28, 2024 and was the lowest at 8 on October 26, 2023.")
st.write("- The data shows how different product types are distributed, with smartphones leading the pack at 6000 units, followed by tablets, laptops, and smartwatches at about 4000 units, and headphones at 2000 units being the least popular.")