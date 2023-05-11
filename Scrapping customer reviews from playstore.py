#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')


# In[14]:


import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# In[5]:


import pandas as pd
import numpy as np
from google_play_scraper import app, reviews_all
import plotly.express as px


# In[6]:


hk_project = reviews_all('com.mysugr.android.companion', sleep_milliseconds = 0, lang = 'en', country = 'US')


# In[7]:


hk_project


# In[8]:


df = pd.json_normalize(hk_project)


# In[9]:


df


# In[10]:


df.info()


# In[15]:


from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

stop_words = stopwords.words('english')

def clean_text(x):
  x = str(x)
  x = x.lower()
  x = re.sub(r'#[A-Za-z0-9]*', ' ', x)
  x = re.sub(r'https*://.*', ' ', x)
  x = re.sub(r'@[A-Za-z0-9]+', ' ', x)
  tokens = word_tokenize(x)
  x = ' '.join([w for w in tokens if not w.lower() in stop_words])
  x = re.sub(r'[%s]' % re.escape('!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~“…”’'), ' ', x)
  x = re.sub(r'\d+', ' ', x)
  x = re.sub(r'\n+', ' ', x)
  x = re.sub(r'\s{2,}', ' ', x)
  return x

df['clean_text'] = df.content.apply(clean_text)


# In[16]:


df["Sentiment"] = df["score"].apply(lambda score: "positive" if score >= 3 else "negative")
df['Sentiment'] = df['Sentiment'].map({'positive':1, 'negative':0})


# In[17]:


df


# In[18]:


df0 = df[['clean_text','Sentiment']]
df0


# In[19]:


color = sns.color_palette()
get_ipython().run_line_magic('matplotlib', 'inline')
py.init_notebook_mode(connected=True)
# Product Scores
fig = px.histogram(df, x="score")
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Product Score')
fig.show()


# In[20]:


stopwords = set('STOPWORDS')
stopwords.update(["br", "href"])
textt = " ".join(review for review in df0.clean_text)
wordcloud = WordCloud(stopwords=stopwords).generate(textt)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud11.png')
plt.show()


# In[21]:


df0['Sentiment'] = df0['Sentiment'].replace({0 : 'negative'})
df0['Sentiment'] = df0['Sentiment'].replace({1 : 'positive'})
fig = px.histogram(df0, x="Sentiment")
fig.update_traces(marker_color="indianred",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Product Sentiment')
fig.show()


# In[ ]:




