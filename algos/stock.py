
class StockSpanner:
    def __init__(self):
        self.mono = []
        
    def next(self, price: int) -> int:

        stack = self.mono
        
        cur_price = price
        cur_span = 1
        
        while stack and stack[-1][0] <= cur_price:
            
            prev_price, prev_span = stack.pop()
            cur_span += prev_span
        
        stack.append( (cur_price, cur_span) )
        return cur_span




