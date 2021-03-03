
from scipy.special import comb
a = 0
for i in range(5):
    print(i)
    a = a + comb(25,i) * 0.2 ** i * 0.8 ** (25-i)
    print(a)
    
print(a)
