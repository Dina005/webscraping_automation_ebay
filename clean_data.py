#Import Libraries
import pandas as pd
import numpy as np
import re


def clean_ebay_data(input_file, output_file):
    """ 
    Removes US$, commas, and whitespace
    Replaces original_price with corresponding price
    Turns price and original price to numeric
    Replaces missing shipping information data
    Calculated discount_percentage
    """

    #Load csv file as strings
    df = pd.read_csv(input_file, dtype=str)

    #Removes US$, commas, and whitespaces
    df['price'] = df['price'].str.replace(r'US \$|,|\s', '', regex=True)
    df['original_price'] = df['original_price'].str.replace(r'US \$|,|\s', '', regex=True)  

    #Replace missing original_price
    df['original_price'] = df['original_price'].replace('', pd.NA).fillna(df['price'])

    #Covert price and original_price into float
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['original_price'] = pd.to_numeric(df['original_price'], errors='coerce')

    #Replace missing shipping information
    df['shipping_details'] = df['shipping_details'].replace(['N/A', ' ', pd.NA], 'Shipping info Unavailable')

    #Calculate discount_percentage
    df['discount_percentage'] = round((1 - (df['price'] / df['original_price'])) * 100).round(2)

    #Save cleaned data
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "ebay_tech_deals.csv"
    output_file = "cleaned_ebay_deals.csv"
    clean_ebay_data(input_file, output_file)
    print("Data saved to cleaned_ebay_deals.csv")


    

