""" 
A knapsack is a bin-packing problem, in which the goal is to maximize the total 
value of items in (typically) a single bin. 

Food Value & Calories

"""
weights=[[120,343,560,340,230,654,980,180,780,456]]
capacities=[250]
values=weights[0]

class Food (object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ':<' + str(self.value) + ','+ str(self.calories)
    
    def buildMenu(self, names,values, calories):
        """ names, values, calaories lists of same length.
            name a list of strings
            values and calories list of numberse.
            returns a list of foods"""
        menu = []
        for i in range(len(values)):
            menu.append(Food(names[i], values[i], calories[i]))
        return menu
    
    def greedy(self, items,maxCost, keyFunction):
        itemsCopy = sorted (items,key=keyFunction, reverse=True)
        result=[]
        totalValue, totalCost = 0.0,0.0
        for i in range(len(itemsCopy)):
            if(totalCost+itemsCopy[i].getCost()) <= maxCost:
                result.append(itemsCopy[i])
                totalCost += itemsCopy[i].getCost()
                totalValue += itemsCopy[i].getValue()
        return (result, totalValue)

