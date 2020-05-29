#!/usr/bin/env python
# coding: utf-8

# $$\Large \color{blue}{\textbf{Exploring a Database with SQLite}}$$
# 
# $$\small \color{green}{\textbf{Written and Coded by}}$$
# $$\large \color{green}{\textbf{Phuong Van Nguyen}}$$
# $$\small \color{red}{\textbf{ phuong.nguyen@summer.barcelonagse.eu}}$$

# # Loading Libraries

# In[1]:


from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


# In[2]:


get_ipython().run_line_magic('reload_ext', 'sql')

import sqlite3

import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pandas_profiling import ProfileReport


# # Assessing to a Database
# ![SQLiteDatabase.png](attachment:SQLiteDatabase.png)

# In[3]:


get_ipython().run_line_magic('sql', 'sqlite:///C:/Users/Phuong_1/Documents/SQL/SQLite/SQLite_Programming/chinook.db')


# # Exploring the Database

# ## Showing the list of Tables in Database

# In[4]:


get_ipython().run_line_magic('sql', "SELECT name FROM sqlite_master WHERE type='table'")


# ## The invoices Tables

# ### Columns of Table

# In[5]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT * \n    FROM invoices\n    WHERE 1=0')


# ### The first k Observations

# In[6]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT *\n    FROM invoices\n    LIMIT 5')


# ### Locations

# In[7]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT DISTINCT BillingCountry\n    FROM invoices')


# In[8]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT COUNT (DISTINCT BillingCountry)\n    FROM invoices')


# ### The Number of invoices

# In[9]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT COUNT(InvoiceId)\n    FROM invoices')


# ### Group the invoice by country

# In[10]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT  BillingCountry,InvoiceId, round(sum(Total),2)\n    FROM invoices\n    GROUP BY BillingCountry')


# In[11]:


df_invoice = get_ipython().run_line_magic('sql', 'SELECT  BillingCountry,InvoiceId, round(sum(Total),2) FROM invoices GROUP BY BillingCountry')
df_invoice=df_invoice.DataFrame()
display(df_invoice)
fig = px.bar(df_invoice, x='round(sum(Total),2)', y='BillingCountry',orientation='h')
fig.show()


# ## The customers Tables

# ### Columns of the customers Tables

# In[12]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT *\n    FROM customers\n    WHERE 1=0')


# ### The first Observations

# In[13]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT *\n    FROM customers\n    LIMIT 5')


# ### Locations

# In[14]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT DISTINCT Country\n    FROM customers')


# ### The number of customers

# In[15]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT COUNT(CustomerId)\n    FROM customers')


# ## The employees Tables

# ### Columns of the employees Tables

# In[16]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT * FROM employees\n    WHERE 1=0')


# ### The first Observations of the employees Tables

# In[17]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT * FROM employees\n    LIMIT 5')


# ### Job levels

# In[18]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT DISTINCT Title\n    FROM employees')


# ### Listing the number of  locations

# In[19]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT DISTINCT City, State, Country\n    FROM employees')


# ### The number of observations

# In[20]:


get_ipython().run_cell_magic('sql', 'sqlite://', '    SELECT count(EmployeeId)\n    FROM employees')


# In[ ]:




