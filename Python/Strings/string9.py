def isValid(s):
    # Split the input string by periods to get individual parts
    arr = s.split(".")
    
    # Check if there are exactly 4 parts in the IP address
    if len(arr) != 4:
        return 0  # Not a valid IPv4 address
    
    # Iterate through each part
    for x in arr:
        # Check if a part has leading '0's but is not '0'
        if len(x) > 1 and x[0] == '0':
            return 0  # Not a valid IPv4 address
        
        try:
            # Try to convert the part to an integer
            x = int(x)
            
            # Check if the integer is within the valid range [0, 255]
            if 0 <= x <= 255:
                continue  # Move to the next part
            else:
                return 0  # Not a valid IPv4 address
            
        except ValueError:
            return 0  # Not a valid IPv4 address (part is not an integer)
    
    # If all parts are valid, return 1 to indicate a valid IPv4 address
    return 1
