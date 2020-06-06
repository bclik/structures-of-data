#!/usr/bin/env python
# coding: utf-8

# ## 1. sözlük oluşturma

# In[59]:


gunler={1:"pazartesi",2:"salı",3:"çarşamba",4:"perşembe",5:"cuma",6:"cumartesi",7:"pazar"}


# In[60]:


print(gunler)
x=input("lütfen dilediğiniz ilk gün numarasını giriniz")
del gunler[int(x)]
y= input("lütfen ikinci gün numarasını giriniz")
del gunler[int(y)]

print("seçilmeyen günler:",gunler)


# ## 2. Ay ve Gün Listesi

# In[95]:


ay_gun = [("ocak",31),
          ("şubat",28),
          ("mart",31),
          ("nisan",30),
          ("mayıs",31),
          ("haziran",30),
          ("temmuz",31),
          ("agustos",31),
          ("eylül",30),
          ("ekim",31),
          ("kasım",30),
          ("aralık",31)
         ]


# ## 3. ay ve gün iki ayrı liste

# In[96]:


aylar= [ay_gun[0][0],
            ay_gun[1][0],
            ay_gun[2][0],
            ay_gun[3][0],
            ay_gun[4][0],
            ay_gun[5][0],
            ay_gun[6][0],
            ay_gun[7][0],
            ay_gun[8][0],
            ay_gun[9][0],
            ay_gun[10][0],
            ay_gun[11][0]
           
           ]

gunler2= [ay_gun[0][1],
            ay_gun[1][1],
            ay_gun[2][1],
            ay_gun[3][1],
            ay_gun[4][1],
            ay_gun[5][1],
            ay_gun[6][1],
            ay_gun[7][1],
            ay_gun[8][1],
            ay_gun[9][1],
            ay_gun[10][1],
            ay_gun[11][1]
           
           ]

toplu_liste = [aylar,gunler2]
print(toplu_liste)


# ## 4.mevsime ayrılmış listeler
# 

# In[92]:


kıs=[ay_gun[11],ay_gun[0],ay_gun[1]]
ilkbahar=[ay_gun[2],ay_gun[3],ay_gun[4]]
yaz=[ay_gun[5],ay_gun[6],ay_gun[7]]
sonbahar=[ay_gun[8],ay_gun[9],ay_gun[10]]


# ## 5. yaz ayı kaç gün sürer

# In[94]:


yaz_suresi = ay_gun[5][1] + ay_gun[6][1] + ay_gun[7][1]
print("yaz mevsiminin süresi: ",yaz_suresi)


# In[ ]:




