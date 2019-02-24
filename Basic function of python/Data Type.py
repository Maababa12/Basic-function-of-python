
# coding: utf-8

# a = 5
# print(a, "is of type", type(a))
# 
# a = 2.0
# print(a, "is of type", type(a))
# 
# a = 1+2j
# print(a, "is complex number?", isinstance(1+2j,complex))

# In[9]:


str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string


# In[1]:


a = 5
print(a, "is of type", type(a))

b = 2.7
print(a, "is of type", type(a))

c = a+b*2j
print(a, "is complex number?", isinstance(1+2j,complex))


# In[10]:


x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

