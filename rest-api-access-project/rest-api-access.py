import requests as r

# # Making GET Request to jsonplaceholder REST API

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = r.get(api_url)
response_obj = response.json()
response_obj
type(response_obj)

# ### Ways to print the parameters returned by the API
# ### Method-1
# #### Method 1: Parameters
for parameters, values in response_obj.items():
    print(parameters)

# #### Method 1: Values
for parameters, values in response_obj.items():
    print(values)

# ### Method-2
# #### Method2: Parameters
list(response_obj.keys())

# #### Method2: Values
list(response_obj.values())
list(response_obj.items())

# # Making POST Request to jsonplaceholder REST API
post_content = {'userId': 1, 'title': 'milk', 'completed': False}

post_content2 = {'userId': 2, 'title': 'cheese', 'completed': False}

api_url2 = 'https://jsonplaceholder.typicode.com/todos'
post_response = r.post(api_url2, json=post_content)  # json=post_content serializes post_content dict into a json string
post_response.json()
post_response2 = r.post(api_url2, json=post_content2)
post_response2.json()

r.get("https://jsonplaceholder.typicode.com/todos/201").json()
# I think the created post resource is getting deleted and hence not retrievable

r.get("https://jsonplaceholder.typicode.com/todos/").json()[0]

import pandas as pd

Series1 = pd.Series()
Series2 = pd.Series()
Series3 = pd.Series()
Series4 = pd.Series()

table = pd.DataFrame()

# # Making PUT Request to jsonplaceholder REST API

put_content = {'userId': 1, 'title': 'cow-milk', 'completed': True}
resp = r.put("https://jsonplaceholder.typicode.com/todos/10", json=put_content)
resp.json()
resp.status_code

k = r.get("https://jsonplaceholder.typicode.com/todos/")  # these are immutable
type(k.json())


l1 = []
l2 = []
l3 = []
l4 = []

for i in range(len(k.json())):
    l1.append(k.json()[i]['userId'])
    l2.append(k.json()[i]['id'])
    l3.append(k.json()[i]['title'])
    l4.append(k.json()[i]['completed'])

# In[202]:


col1 = pd.DataFrame(l1, columns=['userId'])
col2 = pd.DataFrame(l2, columns=['id'])
col3 = pd.DataFrame(l3, columns=['title'])
col4 = pd.DataFrame(l4, columns=['completed'])

table = pd.concat([col1, col2, col3, col4], axis=1)

# In[208]:


table

# In[ ]:
