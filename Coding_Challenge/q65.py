class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Check if the string is empty
        if not s:
            return -1

        result = 0   # Initialize result and sign
        sign = 1

        i = 0           # Initialize index to 0
        

        # Check for the sign
        if s[i] == '-':
            sign = -1
            i += 1

        # Iterate through the characters of the string
        while i < len(s):
            # Check if the character is not a digit
            if not s[i].isdigit():
                return -1

            # Update result
            result = result * 10 + int(s[i])

            # Move to the next character
            i += 1

        # Apply the sign to the result
        return sign * result 
