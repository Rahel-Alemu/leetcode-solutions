class Solution(object):
    def maxIceCream(self, costs, coins):
        max_cost = 0
        for cost in costs:
            if cost > max_cost:
                max_cost = cost
        
        counts = [0] * (max_cost + 1)
        
        for cost in costs:
            counts[cost] += 1
            
        bought_bars = 0
        
        for current_cost in range(1, max_cost + 1):
            if counts[current_cost] > 0:
                num_available = counts[current_cost]
                
                if coins < current_cost:
                    break
                    
                num_can_afford = coins // current_cost
                
                num_to_buy = min(num_available, num_can_afford)
                
                bought_bars += num_to_buy
                coins -= num_to_buy * current_cost
                
        return bought_bars