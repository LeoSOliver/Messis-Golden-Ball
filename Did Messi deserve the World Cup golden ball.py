#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.express as px


# In[3]:


fifa_df = pd.read_csv("Fifa_WC_2022_Match_data.csv", encoding='latin1')
stats_df = pd.read_csv("player_stats.csv", encoding='latin1')


# In[4]:


fifa_df.info()
stats_df.info()


# In[5]:


fifa_df['total_match_goals'] = fifa_df['1_goals'] + fifa_df['2_goals']


# In[6]:


#Messi


# In[7]:


argentina_match = fifa_df[(fifa_df['1'] == 'ARGENTINA') | (fifa_df['2'] == 'ARGENTINA')] 


# In[8]:


final = fifa_df[(fifa_df['1'] == 'ARGENTINA') & (fifa_df['2'] == 'FRANCE')]
final


# In[9]:


messi_stats = stats_df[(stats_df['player'] == 'Lionel Messi')].copy()
messi_stats


# In[10]:


arg_players = stats_df[(stats_df['team'] == 'Argentina')].copy()
arg_players


# In[11]:


Total_arg = arg_players['goals'].sum()
Total_arg


# In[12]:


messi_goals = messi_stats['goals'].sum()
messi_goals


# In[13]:


Arg_goals = Total_arg - messi_goals


# In[14]:


stats_df['high npxg'] = np.where(stats_df['npxg'] >= 2, True, False)


# In[15]:


npxg_df = stats_df[stats_df['high npxg'] == True]


# In[16]:


figure1 = px.bar(npxg_df, 
                x=npxg_df["player"],
                y=npxg_df["npxg"],
                title="Non-penalty xG")
figure1.show()


# In[16]:


#Mbappe


# In[17]:


france_match = fifa_df[(fifa_df['1'] == 'FRANCE') | (fifa_df['2'] == 'FRANCE')] 


# In[18]:


mbappe_stats = stats_df[(stats_df['player'] == 'Kylian MbappÃ©')].copy()
mbappe_stats


# In[19]:


fra_players = stats_df[(stats_df['team'] == 'France')].copy()
fra_players


# In[20]:


mbappe_goals = mbappe_stats['goals'].sum()
mbappe_goals


# In[21]:


Total_fra = fra_players['goals'].sum()
Total_fra


# In[22]:


Fra_goals = Total_fra - mbappe_goals


# In[23]:


labels = ['Argentina', 'France']
player = [messi_goals, mbappe_goals]
team = [Arg_goals, Fra_goals]
plt.bar(labels, player, label = 'Player')
plt.bar(labels, team, bottom = player, label = 'Country')
plt.ylabel('Goals')
plt.title('Messi and Mbappe goals compared to their teams goals')
plt.legend(['Player','Country'])


# In[24]:


messiXG = messi_stats['xg'].sum()
mbappeXG = mbappe_stats['xg'].sum()


# In[25]:


messiNPXG = messi_stats['npxg'].sum()
mbappeNPXG = mbappe_stats['npxg'].sum()


# In[26]:


messi_extra = messiXG - messiNPXG
mbappe_extra = mbappeXG - mbappeNPXG


# In[27]:


labels = ['Messi', 'Mbappe']
npxg = [messiNPXG, mbappeNPXG]
extra = [messi_extra, mbappe_extra]
plt.bar(labels, npxg, label = 'NPXG')
plt.bar(labels, extra, bottom = npxg, label = 'XG')
plt.ylabel('XG')
plt.title('Messi and Mbappe NPXG compared to XG')
plt.legend(['NPXG','XG'])


# In[28]:


all_goals = stats_df['goals'].sum()
all_goals


# In[34]:


messiXA = messi_stats['xg_assist'].sum()
mbappeXA = mbappe_stats['xg_assist'].sum()
messiXA


# In[35]:


messiNPXA = messi_stats['npxg_xg_assist'].sum()
mbappeNPXA = mbappe_stats['npxg_xg_assist'].sum()
messiNPXA


# In[31]:


messi_extra_assist = messiXA - messiNPXA
mbappe_extra_assist = mbappeXA - mbappeNPXA


# In[36]:


labels = ['Messi', 'Mbappe']
npxa = [messiNPXA, mbappeNPXA]
extra_assist = [messi_extra_assist, mbappe_extra_assist]
plt.bar(labels, npxa, label = 'NPXA')
plt.bar(labels, extra_assist, bottom = npxa, label = 'XA')
plt.ylabel('XA')
plt.title('Messi and Mbappe NPXA compared to XA')
plt.legend(['NPXA','XA'])


# In[39]:


labels = ['xg','npxg','xg_assist','npxg_xg_assist','xg_per90','xg_assist_per90','xg_xg_assist_per90','npxg_per90','npxg_xg_assist_per90']
messi = [messi_stats['xg'],messi_stats['npxg'],messi_stats['xg_assist'],messi_stats['npxg_xg_assist'],messi_stats['xg_per90'],messi_stats['xg_assist_per90'],messi_stats['xg_xg_assist_per90'],messi_stats['npxg_per90'],messi_stats['npxg_xg_assist_per90']]
mbappe = [mbappe_stats['xg'],mbappe_stats['npxg'],mbappe_stats['xg_assist'],mbappe_stats['npxg_xg_assist'],mbappe_stats['xg_per90'],mbappe_stats['xg_assist_per90'],mbappe_stats['xg_xg_assist_per90'],mbappe_stats['npxg_per90'],mbappe_stats['npxg_xg_assist_per90']]
plt.plot(labels, messi)
plt.plot(labels,mbappe)
plt.title('Messi and Mbappe compared using Expected values')
plt.ylabel('Expected value')
plt.legend(['Messi','Mbappe'])
plt.show()


# In[ ]:


# Messi produced almost half of his team's goals for this competition. However, Mbappe also produced half of his team's goals.
# Argentina were the only team to have more than 1 player register greater than 2 NPXG, so Messi was helped on the road to the final.
# Mbappe produced a better NPXG than Messi during the torunament.
# Messi produced a much better NPXA through the torunament.
# Mbappe scored a hattrick in the final that probably should have gotten him MoM except 2 of the goals were penalties
# Using these statistics I would say they had almost equal performances throughtout the competition and were both instrumental in
# getting their teams to the final. Therefore, winning the torunament was enough to get Messi the golden ball

