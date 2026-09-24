## Customer Shopping Data Cleaning using Python
## Project Overview

This project focuses on cleaning and analyzing a customer shopping dataset using Python.

The dataset contains customer information such as names, age, gender, email, city, purchase amount, purchase date, and ratings.

The main goal of this project is to identify and handle missing values, duplicate records, invalid data, inconsistent text,
incorrect data types, and invalid values before performing analysis.

## Objectives
Clean and preprocess raw customer shopping data
Handle missing and invalid values
Remove duplicate records
Standardize text data
Validate email addresses
Clean and validate customer ages
Clean purchase amounts and ratings
Standardize purchase dates
Perform basic exploratory analysis
Create meaningful visualizations
Export the cleaned dataset as a CSV file

# #Technologies & Libraries Used
Python
Pandas
NumPy
Matplotlib
Seaborn

## Dataset Columns
Column	Description
Customer_ID	Unique customer identification number
Name	Customer name
Age	Customer age
Gender	Customer gender
Email	Customer email address
City	Customer's city
Purchase_Amount	Amount spent by the customer
Purchase_Date	Date of purchase
Rating	Customer rating from 1 to 5

## Data Cleaning Performed
1. Text Cleaning
Removed unnecessary spaces from names and cities
Standardized multiple spaces
Converted gender abbreviations:
M → Male
F → Female

3. Age Cleaning
Converted age values to numeric format
Converted text values such as thirty to 30
Identified invalid ages
Replaced invalid/missing ages with the median age

4. Email Validation
Checked email addresses using a regular expression
Invalid email addresses were treated as missing values
5. Purchase Amount Cleaning
   
6.Converted purchase amounts to numeric format
Identified negative purchase amounts
Replaced invalid/missing amounts using the median

7. Date Cleaning
Converted purchase dates into datetime format
Handled invalid/missing dates

9. Rating Cleaning
Converted ratings to numeric values
Validated ratings between 1 and 5
Replaced invalid/missing ratings using the median

11. Duplicate Removal
Identified duplicate records
Removed exact duplicate rows

## Analysis Performed
After cleaning the dataset, the following analysis was performed:

Total number of unique customers
Total purchase amount
Average purchase amount
Average customer rating
Total purchase amount by city
Average rating by gender

## Visualizations
1. Total Purchase Amount by City

A bar chart was created to compare the total purchase amount across different cities.

2. Customer Age Distribution

A histogram was created to understand the distribution of customer ages.
