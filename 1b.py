def F(d):
    # Sort by keys (ascending order)
    print("Sorted by keys (ascending):")
    for key in sorted(d.keys()):
        x, y = d[key]
        print(f"-{key}-, -{x}-, -{y}-")
    
    # Sort by x values (descending order)
    print("\nSorted by x values (descending):")
    for key, (x, y) in sorted(d.items(), key=lambda item: item[1][0], reverse=True):
        print(f"-{key}-, -{x}-, -{y}-")
    
    # Sort by y values (ascending order)
    print("\nSorted by y values (ascending):")
    for key, (x, y) in sorted(d.items(), key=lambda item: item[1][1]):
        print(f"-{key}-, -{x}-, -{y}-")

F({1 : (1, 2), 2 : (-1, 4), 5 : (-4, 3), 4 : (2, 3)})
print()