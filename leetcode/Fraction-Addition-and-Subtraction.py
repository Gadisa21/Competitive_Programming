class Solution:
    def fractionAddition(self, expression: str) -> str:
        def parse_fraction(frac_str):
            num, denom = map(int, frac_str.split('/'))
            return num, denom
        
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)
        
        total_num = 0
        total_denom = 1
        
        i = 0
        while i < len(expression):
            sign = 1
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1
            
            j = i
            while j < len(expression) and expression[j] != '/':
                j += 1
            
            numerator = int(expression[i:j])
            i = j + 1
            j = i
            while j < len(expression) and (expression[j].isdigit()):
                j += 1
            
            denominator = int(expression[i:j])
            i = j
            
            numerator *= sign
            
            new_denom = lcm(total_denom, denominator)
            total_num = total_num * (new_denom // total_denom) + numerator * (new_denom // denominator)
            total_denom = new_denom
        
        if total_num == 0:
            return "0/1"
        
        common_divisor = gcd(total_num, total_denom)
        total_num //= common_divisor
        total_denom //= common_divisor
        
        return f"{total_num}/{total_denom}"

