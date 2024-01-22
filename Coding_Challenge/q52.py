def LCA(root, n1, n2):
    temp = root
    while temp:
        temp_val = temp.data
        if temp_val > n1 and temp_val > n2:
            temp = temp.left
        elif temp_val < n1 and temp_val < n2:
            temp = temp.right
        elif temp_val == n1 or temp_val == n2:
            return temp
        elif (temp_val > n1 and temp_val < n2) or (temp_val < n1 and temp_val > n2):
            return temp
