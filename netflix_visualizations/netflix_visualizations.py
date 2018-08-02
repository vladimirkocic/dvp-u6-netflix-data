
# coding: utf-8

# # Introduction
# 
# In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the "Netflix Stock Profile" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. 
# 
# For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:
# + The distribution of the stock prices for the past year
# + Netflix's earnings and revenue in the last four quarters
# + The actual vs. estimated earnings per share for the four quarters in 2017
# + A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 
# 
# Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).
# 
# During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.
# 
# After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:
# 
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 
# Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)
# 

# ## Step 1
# 
# Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[2]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2

# Let's load the datasets and inspect them.

# Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.
# 
# Hint: Use the `pd.read_csv()`function).
# 
# Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day.

# In[3]:


netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks)


# Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.
# 
# Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
# 

# In[4]:


dowjones_stocks = pd.read_csv('DJI.csv')
print(dowjones_stocks)


# Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.
# 

# In[5]:


netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
print(netflix_stocks_quarterly)


# ## Step 3

# Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.
#  - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly
#  - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
#  - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
#  
# Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer.

# What year is represented in the data? Look out for the latest and earliest date.

# In[6]:


earliest_latest = pd.DataFrame([
  ['netflix_stocks',pd.to_datetime(min(netflix_stocks['Date'])),pd.to_datetime(max(netflix_stocks['Date'])),pd.to_datetime(max(netflix_stocks['Date'])).year],
  ['dowjones_stocks',pd.to_datetime(min(dowjones_stocks['Date'])),pd.to_datetime(max(dowjones_stocks['Date'])),pd.to_datetime(max(dowjones_stocks['Date'])).year],
  ['netflix_stocks_quarterly',pd.to_datetime(min(netflix_stocks_quarterly['Date'])),pd.to_datetime(max(netflix_stocks_quarterly['Date'])),pd.to_datetime(max(netflix_stocks_quarterly['Date'])).year],
],
    columns =['DataFrame designation','Earliest date','Latest date','The year is:']
)
print(earliest_latest)


# + Is the data represented by days, weeks, or months? 
# + In which ways are the files different? 
# + What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?

# In[7]:


import numpy as np
nf_st = (pd.to_datetime(netflix_stocks.iloc[1,0])-pd.to_datetime(netflix_stocks.iloc[0,0])).days
dj_st = (pd.to_datetime(dowjones_stocks.iloc[1,0])-pd.to_datetime(dowjones_stocks.iloc[0,0])).days
nfq_st = (pd.to_datetime(netflix_stocks_quarterly.iloc[1,0])-pd.to_datetime(netflix_stocks_quarterly.iloc[0,0])).days

duration = pd.DataFrame([
  ['netflix_stocks', np.where(nf_st==1, 'Yes', 'No'),np.where(nf_st/7==1, 'Yes', 'No'),np.where(nf_st/31==1, 'Yes', 'No') ],
  ['dowjones_stocks', np.where(dj_st==1, 'Yes', 'No'),np.where(dj_st/7==1, 'Yes', 'No'),np.where(dj_st/31==1, 'Yes', 'No') ],
  ['netflix_stocks_quarterly', np.where(nfq_st==1, 'Yes', 'No'),np.where(nfq_st/7==1, 'Yes', 'No'),np.where(nfq_st/31==1, 'Yes', 'No') ],
],
    columns =['Data frame','Days','Weeks','Months']
)
print('Is the data represented by days, weeks, or months? \n- The table below specifies how the records are represented')
print(duration)
print("\nIn which ways are the files different?")
print("- Well, if you're refering to the number of rows, then:")
print("netflix_stocks has ",netflix_stocks.size," rows")
print("dowjones_stocks has ",dowjones_stocks.size," rows")
print("netflix_stocks_quarterly has ",netflix_stocks_quarterly.size," rows\n")
print("\nWhat's different about the columns for netflix_stocks versus netflix_stocks_quarterly?")
print("- As you can see, netflix_stocks_quarterly has one additional column\n")
nf = pd.DataFrame.from_dict(list(netflix_stocks))
dj = pd.DataFrame.from_dict(list(dowjones_stocks))
nfq = pd.DataFrame.from_dict(list(netflix_stocks_quarterly))
comb=pd.concat([nf,dj,nfq], ignore_index=True, axis=1)
comb.columns = ['netflix_stocks','dowjones_stocks','netflix_stocks_quarterly']
print(comb)


# ## Step 4
# 
# Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. 

# In[8]:


netflix_stocks.head()


# What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! 
# 
# The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
# 
# This means this is the column with the true closing price, so these data are very important.
# 
# Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.
# 
# Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.
# Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).
# 

# In[9]:


netflix_stocks.rename(columns={
    'Adj Close': 'Price'},
    inplace=True)
dowjones_stocks.rename(columns={
    'Adj Close': 'Price'},
    inplace=True)
netflix_stocks_quarterly.rename(columns={
    'Adj Close': 'Price'},
    inplace=True)


# Run `netflix_stocks.head()` again to check your column name has changed.

# In[10]:


netflix_stocks.head()


# Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`.

# In[11]:


dowjones_stocks.head()
netflix_stocks_quarterly.head()


# ## Step 5
# 
# In this step, we will be visualizing the Netflix quarterly data! 
# 
# We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!
# 
# 
# 1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.
# 2. Use `sns.violinplot()` and pass in the following arguments:
# + The `Quarter` column as the `x` values
# + The `Price` column as your `y` values
# + The `netflix_stocks_quarterly` dataframe as your `data`
# 3. Improve the readability of the chart by adding a title of the plot. Add `"Distribution of 2017 Netflix Stock Prices by Quarter"` by using `ax.set_title()`
# 4. Change your `ylabel` to "Closing Stock Price"
# 5. Change your `xlabel` to "Business Quarters in 2017"
# 6. Be sure to show your plot!
# 

# In[20]:


ax = sns.violinplot(data=netflix_stocks_quarterly, x='Quarter', y='Price')
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
ax.set_ylabel("Closing Stock Price")
ax.set_xlabel("Business Quarters in 2017")
plt.savefig("violin_distribution_quarters.png")
plt.show()
table_violin_min = round(netflix_stocks_quarterly.groupby(['Quarter'])['Price'].min(),2)
table_violin_max = round(netflix_stocks_quarterly.groupby(['Quarter'])['Price'].max(),2)
table_comb=pd.concat([table_violin_min,table_violin_max], ignore_index=True, axis=1)
table_comb.columns = ['Min','Max']
print(table_comb)


# ## Graph Literacy
# - What are your first impressions looking at the visualized data?
# 
# - In what range(s) did most of the prices fall throughout the year?
# 
# - What were the highest and lowest prices? 

#  

#  

# ## Step 6
# 
# Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. 
# 
# 1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.
# 2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color
# 
# 3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.
# 4. Add a legend by using `plt.legend()` and passing in a list with two strings `["Actual", "Estimate"]`
# 
# 5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`
# 6. Assing "`"Earnings Per Share in Cents"` as the title of your plot.
# 

# In[13]:


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.scatter(x_positions, earnings_actual, color='Red', alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color='Blue', alpha=0.5)
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents")
plt.savefig("earnings_per_share.png")
plt.show()


# ## Graph Literacy
# 
# + What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.
# 

#  

#  

# ## Step 7

# Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).
# 
# As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. 
# 
# 1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars
# 2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data
# 3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars
# 4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data
# 5. Create a legend for your bar chart with the `labels` provided
# 6. Add a descriptive title for your chart with `plt.title()`
# 7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`
# 8. Be sure to show your plot!
# 

# In[14]:


# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = len(revenue_by_quarter) # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]



# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = len(earnings_by_quarter) # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]


plt.bar(bars1_x, revenue_by_quarter)
plt.bar(bars2_x, earnings_by_quarter)
plt.title('Earnings and revenue reported by Netflix')
plt.legend(labels)
plt.xticks(middle_x, quarter_labels)
plt.savefig("earnings_revenues_reported.png")
plt.show()


# ## Graph Literacy
# What are your first impressions looking at the visualized data?
# 
# - Does Revenue follow a trend?
# - Do Earnings follow a trend?
# - Roughly, what percentage of the revenue constitutes earnings?

# In[15]:


rev_pc = round((pd.DataFrame(np.array(revenue_by_quarter))).pct_change()*100,2)
ear_pc = round((pd.DataFrame(np.array(earnings_by_quarter))).pct_change()*100,2)
q_label = pd.DataFrame(np.array(quarter_labels))
comb_pc=pd.concat([q_label, rev_pc,ear_pc], ignore_index=True, axis=1)
comb_pc.columns=['Quarter','Revenue % difference','Earnings % difference']
print('Does Revenue follow a trend? Do Earnings follow a trend? \n- Trend amongst earnings and revenue')
print(comb_pc)
earn_ar = earnings_by_quarter
rev_ar = revenue_by_quarter
rev_earn = pd.DataFrame.from_dict([round(earn_ar/rev_ar*100,2) for earn_ar,rev_ar in zip(earn_ar,rev_ar)])
rev_earn_qs= pd.DataFrame.from_dict(quarter_labels)
rev_earn_pc=pd.concat([rev_earn_qs,rev_earn], ignore_index=True, axis=1)
rev_earn_pc.columns = ['Quarter','% earnings of revenue']
print('')
print('Roughly, what percentage of the revenue constitutes earnings?\n- Find the percentages below')
print(rev_earn_pc)


# ## Step 8
# 
# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. 
# 
# Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.
# - We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot
#     - `1`-- the number of rows for the subplots
#     - `2` -- the number of columns for the subplots
#     - `1` -- the subplot you are modifying
# 
# - Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)
# - Assign "Netflix" as a title to this subplot. Hint: `ax1.set_title()`
# - For each subplot, `set_xlabel` to `"Date"` and `set_ylabel` to `"Stock Price"`
# - Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)
# - Assign "Dow Jones" as a title to this subplot. Hint: `plt.set_title()`
# - There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`
# - Be sure to `.show()` your plots.
# 

# In[16]:


plt.figure(figsize=(10,5))
# Left plot Netflix
ax1 = plt.subplot(1, 2, 1)
ax1.set_title('Netflix')
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
plt.xticks(rotation="vertical")

# Right plot Dow Jones
ax2 = plt.subplot(1, 2, 2)
ax2.set_title('Dow Jones')
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price')
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
plt.xticks(rotation="vertical")
plt.subplots_adjust(wspace=.5)

plt.savefig("compare_nflix_dow.png",bbox_inches='tight')
plt.show()

print('''How did Netflix perform relative to Dow Jones Industrial Average in 2017? Which was more volatile? How do the prices of the stocks compare?\n

- By visually comparing the two lines, Netflix performed better than the Dow Jones Industrial Average, with less then average stock price in the last quarter. 
Netflix was more volatile and prone to sharp changes in the price level.

- If we want to really assess the changes of these two, we have to go beyond and conform them to an equal unit of measure, i.e. percentage of changes.
''')

nf_comp = round((pd.DataFrame(np.array(netflix_stocks['Price']))).pct_change()*100,2)
q_label = pd.DataFrame(np.array(dowjones_stocks['Date']))
comp_nf=pd.concat([q_label, nf_comp], ignore_index=True, axis=1)
comp_nf.columns=['Date','Price']


dj_comp = round((pd.DataFrame(np.array(dowjones_stocks['Price']))).pct_change()*100,2)
comp_dj=pd.concat([q_label, dj_comp], ignore_index=True, axis=1)
comp_dj.columns=['Date','Price']

plt.figure(figsize=(10,10))
# Combined
ax5 = plt.subplot(2, 1, 1)
ax5.set_title('Netflix and Dow Jones fluctuation')
ax5.set_ylabel('Price fluctuation in %')
plt.plot(comp_dj['Date'], comp_dj['Price'])
plt.plot(comp_nf['Date'], comp_nf['Price'])
plt.xticks(rotation="vertical")
plt.subplots_adjust(hspace=0.5)
axes = plt.gca()
axes.set_ylim([-10,30])
plt.legend(['Dow Jones', 'Netflix'])

# Left plot Netflix
ax3 = plt.subplot(2, 2, 3)
ax3.set_title('Netflix')
ax3.set_xlabel('Date')
plt.xticks(rotation="vertical")
ax3.set_ylabel('Price fluctuation in %')
plt.plot(comp_nf['Date'], comp_nf['Price'],'C1')
axes = plt.gca()
axes.set_ylim([-10,30])

# Right plot Dow Jones
ax4 = plt.subplot(2, 2, 4)
ax4.set_title('Dow Jones')
ax4.set_xlabel('Date')
ax4.set_ylabel('Price fluctuation in %')
plt.plot(comp_dj['Date'], comp_dj['Price'])
plt.xticks(rotation="vertical")
plt.subplots_adjust(wspace=.5)
axes = plt.gca()
axes.set_ylim([-10,30])

plt.savefig("combined_netflix_dow.png", bbox_inches='tight')
plt.show()


# - How did Netflix perform relative to Dow Jones Industrial Average in 2017?
# - Which was more volatile?
# - How do the prices of the stocks compare?

#  

# # Step 9
# 
# It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig("filename.png")`.
# 
# As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!
# 
# Remember that your slideshow must include:
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 
