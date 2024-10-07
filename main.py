import streamlit as st

st.title("Activity 3 - CSS145-BM3-Group 2")

st.subheader("Group Members: Drilon, Rafael Francisco V. AND Patrick Jaso") 

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

def histogram_agedistribution():
  plt.hist(df['Age'], bins=20, color='#ffd447', edgecolor='black')
  plt.xlabel('Age Brackets')
  plt.ylabel('Frequency')
  plt.title('Customer Age Distribution')
  plt.grid(True, color='gray', alpha=0.5, linestyle='--')
  plt.grid(axis='x')
  plt.show()
  st.pyplot(plt)
  plt.clf()

histogram_agedistribution()
st.write("Based on the data shown in the figure, the age bracket with the highest frequency of buyers falls between 49 to 51 years old. On the other hand, the lowest number of buyers is between the ages 46 to 48. The data, as per the description, also indicates that the youngest customer is 18 years old, while the oldest is 80. The average age of the customers is 49.")

# Jeska Chan

def pie_chart_gender():

  gender = df['Gender'].value_counts()
  categories = ['Male','Female']

  colors = ['steelblue','palevioletred']
  plt.pie(gender, labels=categories, autopct='%1.1f%%', colors=colors, startangle=90,
          wedgeprops={'width': 0.7, 'edgecolor': 'black', 'linewidth':1})
  plt.title('Customer Gender Distribution')
  plt.show()
  st.pyplot(plt)
  plt.clf()

pie_chart_gender()
st.write("Looking at the pie chart above, we can observe that the majority of electronic sales come from male buyers, with 50.8% of the customers being male, translating to approximately 10,164 buyers. In comparison, female customers account for 49.2%, or around 9,835 individuals. While the difference between the two groups is not dramatic considering the total population, a study by Koen van Gelder (2023) suggests that 'men are generally more inclined to purchase electronic products online than women.' This finding aligns with the observed data, highlighting a slight yet notable preference among male consumers in the electronics market.")


st.subheader("Kael Herrera")

def bar_chart_productrating():
  colors = ['red', 'orange', 'yellow', 'lightgreen', 'green'] #colors, with accordance from worst to best rating ( worst rating <1> being red, best rating <5> being green )

  rating_counts = df['Rating'].value_counts().sort_index()
  ratings = rating_counts.index
  counts = rating_counts.values

  plt.bar(ratings, counts, color=colors)
  plt.title('Customer Product Ratings (1 - 5)')
  plt.ylabel('Amount')
  plt.xlabel('Rating')
  plt.show()
  st.pyplot(plt)
  plt.clf()

bar_chart_productrating()
st.write("Based on the bar chart above, out of 20,000 customer product ratings, the most frequently selected rating was **3**, with 7,963 customers choosing this rating. Interestingly, the next two most common ratings were very close in count: **2** was given by 3,972 customers, while **5**, indicating full satisfaction, was chosen by 3,969 customers — a difference of only three. These results show that the majority of customers rated their product in the middle range, with a notable number also expressing either dissatisfaction or full satisfaction.")

# Kael Herrera

def pie_chart_productcode():

  colors = plt.cm.Paired.colors
  sku = df['SKU'].value_counts()

  plt.pie(sku, labels=sku.index, autopct='%1.1f%%', colors=colors)
  plt.title('Product Code Distribution')
  plt.axis('equal')
  plt.show()
  st.pyplot(plt)
  plt.clf()

pie_chart_productcode()
st.write("The pie chart you see is the current Product Code Distribution for each product. Each segment represents a unique product code, and the data reveals a relatively balanced distribution among the various codes. On average, each product code accounts for approximately 10.1% of the total distribution, indicating a well-distributed variety of products within the dataset.")



st.subheader("Rolando Magat")

def total_price_distribution():
    plt.hist(df['Total Price'], bins=30, color='lightgreen', edgecolor='black')
    plt.xlabel('Total Price (USD)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Total Prices')
    plt.grid(True, color='gray', alpha=0.5, linestyle='--')
    plt.show()
    st.pyplot(plt)
    plt.clf()

total_price_distribution()
st.write("The distribution chart above illustrates the total prices that customers are willing to pay, along with their corresponding frequencies. It reveals that the majority of customers tend to pay between $0 - $4,000 significantly more often than for prices exceeding $4,000. This suggests that the target market primarily consists of customers who prefer more affordable price ranges, indicating potential opportunities for businesses to focus their offerings and marketing strategies within this price bracket.")

# Rolando Magat

def payment_method_distribution():
    payment_counts = df['Payment Method'].value_counts()
    plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Payment Methods')
    plt.axis('equal')
    plt.show()
    st.pyplot(plt)
    plt.clf()

payment_method_distribution()
st.write("The pie chart above illustrates the distribution of various payment methods utilized by customers. The predominant payment method is Credit Cards, accounting for a substantial 29.3% of transactions. Following closely in second place is Bank Transfer, which represents 16.9% of users, while PayPal ranks third. This data suggests that a significant majority of customers prefer to make payments using credit cards or online banking methods.")



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
st.write("This line graph shows the number of orders with respect to the purchase date. The red line shows the original data, while the purple line is the moving average of the number of orders per week. In both cases, there is significant growth around the start of 2024, from an average of 18.17 orders to 43.57. This trend may be due to increasing demand following the end of the global pandemic, new technology and videogame releases, and holiday shopping such as during Christmas. Before 2024, the number of orders peaked at 28 on October 7 and was the lowest at only 8 on October 26. During 2024, orders peaked at 63 on January 28 and was the lowest at 24 on February 8.")

# Nathaniel James Carrillo

def pie_chart_shippingtype():
  colors = ['blue', 'red', 'yellow', 'green', 'orange']
  shipping_counts = df['Shipping Type'].value_counts()
  plt.pie(shipping_counts, labels=shipping_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
  plt.title('Distribution of Shipping Type')
  plt.axis('equal')
  plt.show()
  st.pyplot(plt)
  plt.clf()

pie_chart_shippingtype()
st.write("The pie chart above shows the distribution of shipping types used by the customers. The data indicates that the preferred shipping method is Standard at 33.6% followed by Express and Overnight at 16.8%. The least preferred method is Expedited and Same day shipping at 16.4%")




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