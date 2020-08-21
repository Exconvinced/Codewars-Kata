def tribonacci(signature, n):
    if n <= 3: return signature[:n] 
    for _ in range(n - 3): signature.append(sum(signature[-3:]))
    return signature



signature, n = [3, 2, 1], 10
print(tribonacci(signature, n))