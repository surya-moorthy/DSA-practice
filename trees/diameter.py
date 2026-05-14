def diameter(root , res): # res is the maxi , since it can be vary based on the recursion
    if root is None:
        return 0
    
    left = diameter(root.left, res)
    right = diameter(root.right, res)

    res[0] = max(res[0] , left + right)

    return max(left, right) + 1 
