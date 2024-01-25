def noSibling(root):
    queue, result = deque(), []  # 'queue' for breadth-first traversal, 'result' for storing nodes without siblings
    queue.append(root)

    while queue:
        current_node = queue.popleft()
        child_count, position = 0, -1  # 'child_count' to track the number of children, 'position' to store the position of the child (0 for left, 1 for right)

        if current_node.left:
            queue.append(current_node.left)
            child_count, position = child_count + 1, 0

        if current_node.right:
            queue.append(current_node.right)
            child_count, position = child_count + 1, 1

        if child_count == 1:
            # If the node has only one child, add the data of that child to the result list
            result.append(current_node.left.data if not position else current_node.right.data)

    # Return the sorted unique values of nodes without siblings, or [-1] if none found
    return [-1] if not result else sorted(list(set(result)))
