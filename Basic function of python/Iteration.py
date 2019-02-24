
# coding: utf-8

# In[1]:


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# In[8]:



numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:
    sum = sum+val

print("The sum is", sum)


# In[11]:


numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:
    sum = sum+val/val

print("The sum is", sum)


# In[12]:


genre = ['pop', 'rock', 'jazz']

for i in range(len(genre)):
     print("I like", genre[i])

