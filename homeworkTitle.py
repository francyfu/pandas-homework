
# Dependencies and Setup
%matplotlib notebook
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv


# Raw data file
file = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase= pd.read_csv(file)

## Player Count

* Display the total number of players


playercounts = purchase.count()
playercounts

print(purchase.columns)
print(purchase.dtypes)

purchase['SN'].count()

purchase['Purchase ID'].head(10)

player_numbers = purchase['SN'].value_counts()
player_numbers

player_numbers = purchase['Purchase ID'].value_counts()
player_numbers

## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


unique_numbers = purchase['Item ID'].value_counts()
unique_numbers

avg_price = purchase['Price'].mean()
avg_price

totalpurchase = purchase['Price'].sum()
totalpurchase

summary = pd.DataFrame({"Number of Unique Items": unique_numbers,
                                    "Average Price": avg_price })
summary.head()

summary["Average Price"] = summary["Average Price"].map("${:.2f}".format)
summary.head()


summary.describe()


## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed




playercounts_bygender = purchase['Gender'].value_counts()
playercounts_bygender

gender_percentage = playercounts_bygender / playercounts['Gender']
gender_percentage

gender_demographic = pd.DataFrame({
                                 "Purchase Counts by Gender": playercounts_bygender,
                                 "Gender Percentage": gender_percentage
                                })
gender_demographic.head()

gender_demographic["Gender Percentage"] = gender_demographic["Gender Percentage"].map("{:,.2%}".format)
gender_demographic.head(10)


## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

purchase_group = purchase.groupby(['Gender'])
print(purchase_group)


purchase_count_gender = purchase_group['Purchase ID'].count()
purchase_count_gender

avg_price_gender = purchase_group['Price'].mean()
avg_price_gender

totalpurchase_gender = purchase_group['Price'].sum() 
totalpurchase_gender

purchase_percent_gender = purchase_group['Price'].sum() / playercounts_bygender
purchase_percent_gender

summary_by_gender = pd.DataFrame({
                                 "Purchase Counts by Gender": purchase_count_gender,
                                 "Average Price by Gender": avg_price_gender,
                                 "Total Purchase Amount by Gender": totalpurchase_gender,
                                 "Total Purchase Percentage by Gender": purchase_percent_gender
                                })
summary_by_gender.head()


summary_by_gender["Total Purchase Amount by Gender"] = pd.to_numeric(summary_by_gender["Total Purchase Amount by Gender"])
summary_by_gender.head()

summary_by_gender["Average Price by Gender"] = summary_by_gender["Average Price by Gender"].map("${:.2f}".format)
summary_by_gender["Total Purchase Amount by Gender"] = summary_by_gender["Total Purchase Amount by Gender"].map("${:.2f}".format)
summary_by_gender["Total Purchase Percentage by Gender"] = summary_by_gender["Total Purchase Percentage by Gender"].map("{:,.2%}".format)
summary_by_gender.head(10)

purchase.describe()

## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


purchase["Age"] = pd.cut(purchase["Age"], age_bins, labels=group_names)
purchase

purchase_group_byage = purchase.groupby("Age")
purchase_group_byage

purchase_count_age = purchase_group_byage['Age'].count()
purchase_count_age

age_percentage = purchase_count_age / playercounts['Age']
age_percentage

age_demographic = pd.DataFrame({
                                 "Purchase Counts by Age": purchase_count_age,
                                 "Age Catergory Percentage": age_percentage
                                })
age_demographic.head()


age_demographic["Age Catergory Percentage"] = age_demographic["Age Catergory Percentage"].map("{:,.2%}".format)
age_demographic.head(10)

## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

avg_price_byage = purchase_group_byage['Price'].mean()
avg_price_byage

totalpurchase_byage = purchase_group_byage['Price'].sum()
totalpurchase_byage

purchase_percent_byage = totalpurchase_byage / purchase_count_age
purchase_percent_byage

summary_by_age = pd.DataFrame({
                                 "Purchase Counts by Age": purchase_count_age,
                                 "Average Price by Age": avg_price_byage,
                                 "Total Purchase Amount by Age": totalpurchase_byage,
                                 "Purchase Percentage by Age": purchase_percent_byage
                                })
summary_by_age.head()


summary_by_age["Average Price by Age"] = summary_by_age["Average Price by Age"].map("${:.2f}".format)
summary_by_age["Total Purchase Amount by Age"] = summary_by_age["Total Purchase Amount by Age"].map("${:.2f}".format)
summary_by_age["Purchase Percentage by Age"] = summary_by_age["Purchase Percentage by Age"].map("{:,.2%}".format)
summary_by_age.head(10)



## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



purchase_group_bysn = purchase.groupby("SN")
purchase_group_bysn

purchase_counts_bysn = purchase_group_bysn['Purchase ID'].count()
purchase_counts_bysn

spender_average_bysn = purchase_group_bysn['Price'].mean()
spender_average_bysn

spender_amount_bysn = purchase_group_bysn['Price'].sum()
spender_amount_bysn

top_spender = pd.DataFrame({
                                 "Purchase Counts by SN": purchase_counts_bysn ,
                                 "Average Price by SN": spender_average_bysn,
                                 "Purchase Amount by SN": spender_amount_bysn                        
                                })
top_spender.head()

top_spender_descending= top_spender.sort_values("Purchase Amount by SN", ascending=False)
top_spender_descending.head()


top_spender_descending["Average Price by SN"] = top_spender_descending["Average Price by SN"].map("${:.2f}".format)
top_spender_descending["Purchase Amount by SN"] = top_spender_descending["Purchase Amount by SN"].map("${:.2f}".format)
top_spender_descending.head(10)

## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



purchase_loc_byid = purchase.loc[:,["Item ID","Item Name","Price"]]
purchase_loc_byid



purchase_counts_byid = purchase_loc_byid.groupby(["Item ID","Item Name"]).count()["Price"]
average_price_byid = purchase_loc_byid.groupby(["Item ID","Item Name"]).mean()["Price"]
total_value_byid = purchase_loc_byid.groupby(["Item ID","Item Name"]).sum()["Price"]

popular_item = pd.DataFrame({
                                 "Purchase Counts by Item": purchase_counts_byid ,
                                 "Item Price": average_price_byid ,
                                 "Total Value by Item": total_value_byid                       
                                })
popular_item.head()

popular_item_descending = popular_item.sort_values("Purchase Counts by Item", ascending=False)
popular_item_descending.head()

popular_item_descending["Item Price"] = popular_item_descending["Item Price"].map("${:.2f}".format)
popular_item_descending["Total Value by Item"] = popular_item_descending["Total Value by Item"].map("${:.2f}".format)
popular_item_descending.head(5)



## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame



profitable_item_descending= popular_item.sort_values("Total Value by Item", ascending=False)
profitable_item_descending.head()


profitable_item_descending["Item Price"] = profitable_item_descending["Item Price"].map("${:.2f}".format)
profitable_item_descending["Total Value by Item"] = profitable_item_descending["Total Value by Item"].map("${:.2f}".format)
profitable_item_descending.head()