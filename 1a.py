def F(n):
    for i in range(n):
        # Generate the left and right padding
        padding = '-' * (n - i - 1)
        
        # Generate the middle pattern
        middle = ''
        for j in range(i + 1):
            middle += chr(65 + j)  # Append letters starting from 'A'
        for j in range(i, 0, -1):
            middle += chr(65 + j - 1)  # Append letters in reverse order
        
        # Combine padding and middle part
        result = padding + middle + padding
        print(result)


F(3)
print()