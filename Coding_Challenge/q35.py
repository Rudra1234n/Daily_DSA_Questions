class Solution:
    # Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self, histogram):
        stack = []
        max_area = 0
        index = 0

        while index < len(histogram):
            # If the stack is empty or the current height is greater than the height at the top of the stack,
            # push the current index onto the stack.
            if not stack or histogram[index] >= histogram[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Calculate the area of the rectangle using the height at the top of the stack.
                top = stack.pop()
                height = histogram[top]
                width = index if not stack else index - stack[-1] - 1
                max_area = max(max_area, height * width)

      
        while stack:
            top = stack.pop()
            height = histogram[top]
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area
