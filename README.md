# webscraping_automation_ebay
# webscraping_automation_ebay
## Assignment Overview
The goal of this assignmnet, "Lab Assignment 5: Scraping, Cleaning, and  Analyzing eBay Tech Deals," was to automate the scraping process using github actions and implment data cleaning and  visualization technique to extract information from the present data.

## Methodology
### Web Scraping
1. Library Import: The most important library used for scraping was selenium
2. Scrolling: Infinite scrolling was implemented as a to load all the products in the website
3. Extraction: Scraping function was used to extract necessary product details, including: title, price, original price, shipping details, item url, and timestamp.
4. Data Storage: Data was saved in a CSV file for later usage

### Automation
The file was pushed into the relevant github repository in which github actions was used to automate scraping for 3 hour intervals for 2 days.

Errors: simple changes made to the scraper.py file caused errors in the automation process that were fixed afterwards, but delayed the scraping process

### Data Cleaning
Created a function to clean the scraped data. The function included:
Removing unnecessary symbols such as US$, commas, and whitespaces from prices
Replacing missing information for each the original prices and shipping details
Coverting prices into floats for easy visualization
Adding a new column to calculate discount percentages

### Visualization
1. Set up a Jupyter notebook and imported pandas, seaborn, and matplotlib for data plotting
2. Loaded the csv file and inspected the first few rows using the display(df.head()) function. While inspecting the data I realized that the headers were being considered as rows which disrupted the visualization process. Therefore a skiprows=1 was implmented to fix this problem and ensure effective visualization.
3. Conducted analysis and visualization on: deal frequency, price frequency and difference, shipping information availability, product titles frequency, cost different analysis, and discount rates.

## Key Findings
### Deal Frequency
According to the bar chart, we can observe that hour 12 had a significant spike in deals. This could be attributed to a promotional event or rush hour. Further investigation should be conducted to observe the products that were purchased during this time to infer the reasoining behind this spike and to formulate proper strategies.

### Price Distribution
When visualizing the price distribution I realized the there were empty or missing prices. Therefore they were replaced by the median which showed that most prices were between 200 and showed a numer of outliers. It is important to note that before this cleaning process was taken, the histogram showed a positive skewness to the right and outliers represented prices above the range of $0 to $400. Further investigation should be done to ensure better price extraction.

### Original Price
There is a positive correlation between both price and original price. Further investigation should be conducted to discover if this relationship is weak or strong to infer the correlation between the two.

### Discounts
There were little to few discounts, however some of them reached to 70%, which infers that some products were undergoing a clearance sale probably due to a lack of demand.

### Shipping Details
Most items extracted has no shipping details (1000) with few having free shipping options. Further investigation can be done to discover the factors that affect this

### Product Keywords
Most common keywords in the product titles were "Apple" and "iPhone", which should be combined under a common title. Nonetheless, this indicates that these were products were much higher in demand. However, more investigation sgoyld be conducted

## Challenges
## XPath Extraction
There were difficulties when extracting the original prices and shipping details at first.
## Variable Naming Conventions
Using capital letters for dictionary names and the column names in the scraper.py caused some issues in the initial output but were later on fixed

## Product Loading
Loading all products was troublesome which did not provide accurate representation of the data

## Missing Price 
When creating visualizations for the price, several null spaces were detected and replaced by the median price to represent a more accurate representation of the dataset


