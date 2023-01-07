class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = heavy = neither = False
        volume = length * width * height
        if mass >= 100:
            heavy = True
        if volume >= 10**9 or length >= 10**4 or width >= 10**4 or height >= 10**4:
            bulky = True
            
        if bulky and heavy:
            return 'Both'
        elif bulky:
            return 'Bulky'
        elif heavy:
            return 'Heavy'
        else:
            return 'Neither'
        