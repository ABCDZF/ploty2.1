#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import plotly.express as plt

data = sns.load_dataset('titanic')
plt.scatter(data, x='age', y= 'fare')


# Q2

# In[8]:


tip_data = plt.data.tips()
plt.box(tip_data,x='day',y='total_bill')


# Q3

# In[13]:


data = plt.data.tips()
histogram = plt.histogram(data,x ='sex', y ='total_bill',color ='day',pattern_shape="smoker")
histogram.show()


# Q4

# In[15]:


# Load the iris dataset from Plotly
iris_data = plt.data.iris()

# Create a scatter matrix plot
scatter_matrix = plt.scatter_matrix(
    iris_data,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species"
)

# Show the scatter matrix plot
scatter_matrix.show()


# Q5. What is Distplot? Using Plotly express, plot a distplot.
# 
# Ans> Distplot is a seaborn library function that is used to visualize a univariate distribution of observations. It combines a histogram with a kernel density estimate, allowing to visualize the distribution of a variable along with its density curve

# In[18]:


data = plt.data.tips()
histogram = plt.histogram(data, x="total_bill")

# Show the histogram
histogram.show()


# In[ ]:




