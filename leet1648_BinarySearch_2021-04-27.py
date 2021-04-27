class Solution(object):
    def check(self, inventory, x, orders):
        '''
        Suppose the last(cheapest)  ball costs x values. we check if we can fill up "orders" balls.
        '''
        count = 0
        for i in range(len(inventory)):
            if inventory[i]>=x:
                count += inventory[i]-x+1
                if count>=orders:
                    return True
        return False
    
    
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        inventory.sort(reverse = True)
        
        left = 0
        right = 10**9
        while(left+1<right):
            middle = (left+right)/2
            if self.check(inventory, middle, orders):
                left = middle
            else:
                right = middle
        if self.check(inventory, right, orders):
            x = right
        else:
            x = left
            
        # all balls with value above x can be sold out
        # print x
        values = 0
        for v in inventory:
            if v>x:
                values += (v-x)*(x+1+v)/2
                orders -= (v-x)
                # print values, orders
        # all other balls are sold at the value of x
        values += orders*x
        return values%(10**9+7)
