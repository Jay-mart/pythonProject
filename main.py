import numpy as np
import random
import statistics
import matplotlib.pyplot as plt

print("(N=100)-----------------------------------------------------------------------------------------------------")
# original output for x
low = -1
high = 1
x100 = [round(random.uniform(low, high), 4) for _ in range(100)]

print("This is the original x dataset")
#print(x100)

# original output for y
low = -1
high = 1
y100 = [round(random.uniform(low, high), 4) for _ in range(100)]

print("This is the original x dataset")
#print(x100)

list_yy100sqr = np.square(y100)
list_xx100sqr = np.square(x100)

#print(list_xx100sqr)
#print(len(list_xx100sqr))

# print(list_yy100sqr)
#print(len(list_yy100sqr))

list_ri100 = ([sum(x) for x in zip(list_xx100sqr, list_yy100sqr)])

# printing resultant list this will make an array. Use the original square algo to plug into this string to list_yy_400
# did not work sqr before did
#print("Addition of xx + yy")
print(str(list_ri100))

print("This is the final ri (n=100)")
# find square root of items in the list
list_output100 = np.sqrt(list_ri100)
#print(list_output100)

print("The max of Ri list is")
list_output_100= np.array([list_output100])
print(list_output_100.max())

print("The min of Ri list is")
list_output_100 = np.array([list_output100])
print(list_output_100.min())

print("The mean of Ri list is")
list_output_100 = np.array([list_output100])
print(list_output_100.mean())

ar100= np.array(list_output100)
# get the standard deviation
print("This is the standard deviation for Ri")
print(ar100.std())

# Wow, that was easy! Took hours to figure this out
print("Percentage of the ri N=100<or= to 0")
print(" 17%    17/100")
print((ar100 > 1).sum())

print("(N=200)-----------------------------------------------------------------------------------------------------")
# original output for x
low = -1
high = 1
x200 = [round(random.uniform(low, high), 4) for _ in range(200)]

print("This is the original x dataset")
#print(x200)

# original output for y
low = -1
high = 1
y200 = [round(random.uniform(low, high), 4) for _ in range(200)]

print("This is the original x dataset")
#print(x200)

list_yy200sqr = np.square(y200)
list_xx200sqr = np.square(x200)

#print(list_xx200sqr)
#print(len(list_xx200sqr))

# print(list_yy200sqr)
#print(len(list_yy200sqr))

list_ri200 = ([sum(x) for x in zip(list_xx200sqr, list_yy200sqr)])

# printing resultant list this will make an array. Use the original square algo to plug into this string to list_yy_400
# did not work sqr before did
#print("Addition of xx + yy")
print(str(list_ri200))

print("This is the final ri (n=200)")
# find square root of items in the list
list_output200 = np.sqrt(list_ri200)
#print(list_output200)

print("The max of Ri list is")
list_output_200= np.array([list_output200])
print(list_output_200.max())

print("The min of Ri list is")
list_output_200 = np.array([list_output200])
print(list_output_200.min())

print("The mean of Ri list is")
list_output_200 = np.array([list_output200])
print(list_output_200.mean())

ar200= np.array(list_output200)
# get the standard deviation
print("This is the standard deviation for Ri")
print(ar200.std())

# Wow, that was easy! Took hours to figure this out
print("Percentage of the ri N=200<or= to 0")
print(" 19.5%   39/200")
print((ar200 > 1).sum())


print("(N=300)-----------------------------------------------------------------------------------------------------")
# original output for x
low = -1
high = 1
x300 = [round(random.uniform(low, high), 4) for _ in range(300)]

print("This is the original x dataset")
#print(x300)

# original output for y
low = -1
high = 1
y300 = [round(random.uniform(low, high), 4) for _ in range(300)]

print("This is the original x dataset")
#print(x300)

list_yy300sqr = np.square(y300)
list_xx300sqr = np.square(x300)

#print(list_xx300sqr)
#print(len(list_xx300sqr))

# print(list_yy300sqr)
#print(len(list_yy300sqr))

list_ri300 = ([sum(x) for x in zip(list_xx300sqr, list_yy300sqr)])

# printing resultant list this will make an array. Use the original square algo to plug into this string to list_yy_400
# did not work sqr before did
#print("Addition of xx + yy")
print(str(list_ri300))

print("This is the final ri (n=300)")
# find square root of items in the list
list_output300 = np.sqrt(list_ri300)
#print(list_output300)

print("The max of Ri list is")
list_output_300= np.array([list_output300])
print(list_output_300.max())

print("The min of Ri list is")
list_output_300 = np.array([list_output300])
print(list_output_300.min())

print("The mean of Ri list is")
list_output_300 = np.array([list_output300])
print(list_output_300.mean())

ar300= np.array(list_output300)
# get the standard deviation
print("This is the standard deviation for Ri")
print(ar300.std())

# Wow, that was easy! Took hours to figure this out
print("Percentage of the ri N=300<or= to 0")
print(" 20.3%    61/300")
print((ar300 > 1).sum())


print("(N=400)-----------------------------------------------------------------------------------------------------")
# original output for x
low = -1
high = 1
x400 = [round(random.uniform(low, high), 4) for _ in range(400)]

print("This is the original x dataset")
#print(x400)

# original output for y
low = -1
high = 1
y400 = [round(random.uniform(low, high), 4) for _ in range(400)]

print("This is the original x dataset")
#print(x400)

list_yy400sqr = np.square(y400)
list_xx400sqr = np.square(x400)

#print(list_xx400sqr)
#print(len(list_xx400sqr))

# print(list_yy400sqr)
#print(len(list_yy400sqr))

list_ri400 = ([sum(x) for x in zip(list_xx400sqr, list_yy400sqr)])

# printing resultant list this will make an array. Use the original square algo to plug into this string to list_yy_400
# did not work sqr before did
#print("Addition of xx + yy")
print(str(list_ri400))

print("This is the final ri (n=400)")
# find square root of items in the list
list_output400 = np.sqrt(list_ri400)
#print(list_output400)

print("The max of Ri list is")
list_output_400= np.array([list_output400])
print(list_output_400.max())

print("The min of Ri list is")
list_output_400 = np.array([list_output400])
print(list_output_400.min())

print("The mean of Ri list is")
list_output_400 = np.array([list_output400])
print(list_output_400.mean())

ar400= np.array(list_output400)
# get the standard deviation
print("This is the standard deviation for Ri")
print(ar400.std())

# Wow, that was easy! Took hours to figure this out
print("Percentage of the ri N=400<or= to 0")
print(" 19%   76/400")
print((ar400 > 1).sum())


print("(N=500)-----------------------------------------------------------------------------------------------------")
# original output for x
low = -1
high = 1
x500 = [round(random.uniform(low, high), 4) for _ in range(500)]

print("This is the original x dataset")
#print(x500)

# original output for y
low = -1
high = 1
y500 = [round(random.uniform(low, high), 4) for _ in range(500)]

print("This is the original x dataset")
#print(x500)

list_yy500sqr = np.square(y500)
list_xx500sqr = np.square(x500)

#print(list_xx500sqr)
#print(len(list_xx500sqr))

# print(list_yy500sqr)
#print(len(list_yy500sqr))

list_ri500 = ([sum(x) for x in zip(list_xx500sqr, list_yy500sqr)])

# printing resultant list this will make an array. Use the original square algo to plug into this string to list_yy_500
# did not work sqr before did
#print("Addition of xx + yy")
print(str(list_ri500))

print("This is the final ri (n=500)")
# find square root of items in the list
list_output500 = np.sqrt(list_ri500)
#print(list_output500)

print("The max of Ri list is")
list_output_500= np.array([list_output500])
print(list_output_500.max())

print("The min of Ri list is")
list_output_500 = np.array([list_output500])
print(list_output_500.min())

print("The mean of Ri list is")
list_output_500 = np.array([list_output500])
print(list_output_500.mean())

ar500= np.array(list_output500)
# get the standard deviation
print("This is the standard deviation for Ri")
print(ar500.std())

# Wow, that was easy! Took hours to figure this out
print("Percentage of the ri N=500<or= to 0")
print(" 23.6%    118/500")
print((ar500 > 1).sum())

print("(N=600)-----------------------------------------------------------------------------------------------------")
# original output for x
low = -1
high = 1
x600 = [round(random.uniform(low, high), 4) for _ in range(600)]

print("This is the original x dataset")
#print(x600)

# original output for y
low = -1
high = 1
y600 = [round(random.uniform(low, high), 4) for _ in range(600)]

print("This is the original x dataset")
#print(x600)

list_yy600sqr = np.square(y600)
list_xx600sqr = np.square(x600)

#print(list_xx600sqr)
#print(len(list_xx600sqr))

# print(list_yy600sqr)
#print(len(list_yy600sqr))

list_ri600 = ([sum(x) for x in zip(list_xx600sqr, list_yy600sqr)])

# printing resultant list this will make an array. Use the original square algo to plug into this string to list_yy_600
# did not work sqr before did
#print("Addition of xx + yy")
print(str(list_ri600))

print("This is the final ri (n=600)")
# find square root of items in the list
list_output600 = np.sqrt(list_ri600)
#print(list_output600)

print("The max of Ri list is")
list_output_600= np.array([list_output600])
print(list_output_600.max())

print("The min of Ri list is")
list_output_600 = np.array([list_output600])
print(list_output_600.min())

print("The mean of Ri list is")
list_output_600 = np.array([list_output600])
print(list_output_600.mean())

ar600= np.array(list_output600)
# get the standard deviation
print("This is the standard deviation for Ri")
print(ar600.std())

# Wow, that was easy! Took hours to figure this out
print("Percentage of the ri N=600<or= to 0")
print(" 21.8%    131/600")
print((ar600 > 1).sum())


# Data analysis

# x axis values
x1 = [100, 200, 400, 500, 600, ]
# corresponding y axis values (P)
y1 = [17, 19.5, 20.3, 19, 23.6, ]
# y2 = p*4
y2 = [68, 78, 81.2, 76, 94.4, ]
# y3 = y1/2
y3 = [8.5, 9.75, 10.15, 9.5, 11.8, ]
# y4= ri > 1



# plotting the points
plt.plot(x1, y1, )
plt.plot(x1, y2, )
plt.plot(x1, y3, )


# setting x and y-axis range
plt.ylim(1, 100)
plt.xlim(100, 600)

# naming the x-axis

plt.xlabel('N')

# naming the y-axis
plt.ylabel('P(Ri)')
plt.plot(y1, 'g--', y2, 'r--',y3, 'b--',)
plt.legend(['Ri as a percentage P', ' 4*P','P/2',], loc='upper left')
plt.title('P(Ri)/N')
plt.plot(x1,y1)



# function to show the plot
plt.show()


