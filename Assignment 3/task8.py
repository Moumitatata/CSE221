def get_preorder(inorder, postorder):
    # Map each value in inorder to its index for quick lookup
    value_index = {}
    for i in range(len(inorder)):
        value_index[inorder[i]] = i

    # Start from the last element of postorder (the root)
    post_pos = [len(postorder) - 1]  # Use list to make it mutable in recursion

    def build(in_start, in_end):
        if in_start > in_end:
            return []

        # Root is the current last item in postorder
        root = postorder[post_pos[0]]
        post_pos[0] -= 1

        # Find root position in inorder
        mid = value_index[root]

        # Build right subtree first (important because we go backward in postorder)
        right = build(mid + 1, in_end)
        left = build(in_start, mid - 1)

        # Return preorder: root → left → right
        return [root] + left + right

    return build(0, len(inorder) - 1)

# Input
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# Build preorder and print
preorder = get_preorder(inorder, postorder)
print(*preorder)
