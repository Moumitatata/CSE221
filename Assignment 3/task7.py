n = int(input())  
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

value_to_index = {}
for i in range(n):
    value_to_index[inorder[i]] = i

postorder = []

def make_postorder(in_start, in_end, pre_start, pre_end):
    if in_start > in_end or pre_start > pre_end:
        return

    root = preorder[pre_start]
    root_pos = value_to_index[root]
    left_size = root_pos - in_start

    make_postorder(in_start, root_pos - 1, pre_start + 1, pre_start + left_size)

    make_postorder(root_pos + 1, in_end, pre_start + left_size + 1, pre_end)

    postorder.append(root)

make_postorder(0, n - 1, 0, n - 1)
print(*postorder)
