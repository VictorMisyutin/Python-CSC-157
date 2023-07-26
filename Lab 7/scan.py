#**************************************************************************
# * Name: Victor Misyutin                                           CSC 157
# * Date: 18-7-2023                                                 LAB 7   
# *************************************************************************
# * Problem Statement and Specifications: Given a file with items and their prices
# *                     output the following:
# * Output: The name of each item and its price as well as the sum of all the items
# *         and the total number of items.
# *
# *************************************************************************

# output descriptive messages
print('This program will read each line in the file invoice.txt and print a\n'
       + 'a table indicating the item and it\'s cost.  When the file is exhausted,\n'
       + 'it will print the cumulative sum of all of the costs and the total \n'
       + 'number of items.\n')

# display header line for items list
print('{0: <10}'.format('Item'), '{0: >17}'.format('Cost'), sep = '' )

# add your remaining code below
prices = []
file = open("invoice.txt","r")
for line in file:
    items = line.split("#")
    prices.append(items[1])
    print('{0: <10}'.format(items[0]), '{0: >17}'.format("$"+items[1]), sep = '',end='')
print()
print()
sum = 0.0
for price in prices:
    sum += float(price)
print('{0: <10}'.format("Total"), '{0: >17}'.format("$"+str(sum)), sep = '' ,)
print('{0: <10}'.format("Number Of Tools"), '{0: >12}'.format(len(prices)), sep = '')
