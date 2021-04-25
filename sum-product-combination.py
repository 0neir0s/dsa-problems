"""
Given N, we have to find the sum of products of all combinations taken 1 to N at a time. 
Example:
    Input :  N = 3
    Output : f(1) = 6, f(2) = 11, f(3) = 6
"""

def multiply(A, B): 
    """Multiply two polynomials term by term"""
    m, n = len(A), len(B)
    prod = [0] * (m + n - 1); 
    for i in range(m):
        for j in range(n):
            prod[i + j] += A[i] * B[j]
    return prod

def constructPolynomial(N):
    ''' get the polynomial (1+x)(1+2x)...(1+Nx) 
        F(n) = 2F(n/2) + O(n^2) => F = O(n^2) '''
    ps = [[1,i] for i in range(1,N+1)]
    while (len(ps)!=1):
        l = len(ps)
        end = [ps[-1]] if l%2 else []
        ps = [multiply(ps[i],ps[i+1]) for i in range(0,l-1,2)] + end 
    return ps

print(constructPolynomial(4))
