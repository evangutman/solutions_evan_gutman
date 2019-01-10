import sys


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


items = []


def twoGifts(left, balance):
    """Two Gift Sum Algorithm

    Finds the sum of two gifts that are equivalent to, or closest to, the balance given.

    Attributes: 
        right: Index furthest right when traversing the list of items
        maxItems: Array of two items with a sum closest to the balance
        maxSum: Sum of two items closest to the balance
        currentSum: Temporary sum of two items while iterating over the full list of items

    :param left: Index furthest left when traversing the list of items 
    :param balance: Gift card balance

    :return maxSum, maxItems
    """

    right = len(items) - 1
    maxItems = [items[left], items[left + 1]]    
    maxSum = items[left].price + items[left + 1].price   
    if maxSum > balance:
        return maxSum, maxItems

    while left < right:
        currentSum = items[left].price + items[right].price
        
        if currentSum < balance:
            if currentSum > maxSum:
                maxItems[0] = items[left]
                maxItems[1] = items[right]
                maxSum = currentSum
            left += 1
        elif currentSum > balance:
           right -= 1
        else:
            maxItems[0] = items[left]
            maxItems[1] = items[right]
            maxSum = currentSum
            break
            
    return maxSum, maxItems

    
def threeGifts(balance):
    """Three Gift Sum Algorithm
    
    Finds the sum of three gifts that are equivalent to, or closest to, the balance given.

    Attributes:
        maxItems: Array of two items with a sum closest to the balance
        maxSum: Sum of two items closest to the balance
        subTotal: Balance remaining if bought one item
        maxSubTotal: Sum of two items closest to the subTotal
        subItems: Array of two items with a sum closest to the subTotal

    :param balance: Gift card balance

    :return maxSum, maxItems
    """
    maxItems = [items[0], items[1], items[2]]
    maxSum = items[0].price + items[1].price + items[2].price
    if maxSum > balance:
        return maxSum, maxItems

    for idx, item in enumerate(items):
        subTotal = balance - item.price
        
        if idx == len(items) - 2:
            break

        maxSubTotal, subItems = twoGifts(idx + 1, subTotal)

        if maxSubTotal < subTotal:
            if maxSubTotal + item.price > maxSum:
                maxItems[0] = item
                maxItems[1] = subItems[0]
                maxItems[2] = subItems[1]
                maxSum = maxSubTotal + item.price
        elif maxSubTotal == subTotal:
            maxItems[0] = item
            maxItems[1] = subItems[0]
            maxItems[2] = subItems[1]
            maxSum = maxSubTotal + item.price
            break

    return maxSum, maxItems


def loadItems():
    with open(sys.argv[1]) as file:
        for line in file:
            data = [d.strip() for d in line.split(',')]
            items.append(Item(data[0], int(data[1])))


def driver():
    """Driver Function

    Process the command line argument for the number of gifts and call the respective function

    Attributes:
        finalSum: Sum of items closest to the balance
        finalItems: Array of items with a sum closest to the balance
    """
    
    if len(sys.argv) != 4:
        print('Number of arguments is incorrect!')
        return

    loadItems()

    numGifts = int(sys.argv[2])
    balance = int(sys.argv[3])

    if numGifts == 2:
        finalSum, finalItems = twoGifts(0, balance)
    elif numGifts == 3:
        finalSum, finalItems = threeGifts(balance)
    else:
        print('Please enter either 2 or 3 for the number of gifts')
        return
  
    print('Not Possible') if finalSum > balance else print(', '.join([item.name + ' ' + str(item.price) for item in finalItems]))


driver()
