class Solution:
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        while dividend >= divisor:
            temp_divisor, count = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            dividend -= temp_divisor
            quotient += count
            
        if negative:
            quotient = -quotient
            
        return max(-2147483648, min(2147483647, quotient))