from math import ceil, log
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key  # self.key = key


def printInorder(root):
    val = []
    if root:
        printInorder(root.left)

        print(root.val),

        printInorder(root.right)


def printPreorder(root):
    if root:
        print(root.val),

        printPreorder(root.left)

        printPreorder(root.right)


def printPostorder(root):
    if root:
        printPostorder(root.left)

        printPostorder(root.right)

        print(root.val),


def minValueNode(node):
    current = node
    while (current.left is not None):
        current = current.left
    return current


def deleteNode(root, val):
    if root is None:
        return root

    if val < root.val:
        root.left = deleteNode(root.left, val)
    elif (val > root.val):
        root.right = deleteNode(root.right, val)
    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)

        root.val = temp.val

        root.right = deleteNode(root.right, temp.val)

    return root


def findMax(root):
    if (root == None):
        return float('-inf')
    res = root.val
    lres = findMax(root.left)
    rres = findMax(root.right)
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res


def find_min_in_BT(root):
    if root is None:
        return float('inf')
    res = root.val
    lres = find_min_in_BT(root.left)
    rres = find_min_in_BT(root.right)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res


def iterativeSearch(root, key):
    # Traverse until root reaches
    # to dead end
    while root != None:

        # pass right subtree as new tree
        if key > root.val:
            root = root.right

        # pass left subtree as new tree
        elif key < root.val:
            root = root.left
        else:
            return True  # if the key is found return 1
    return False

def draw_seq_bin_tree(nodes, cell_width=2):
    node_width = cell_width + 2
    ws = "·"
    empty_cell = ws * cell_width
    lft_br = f"{(ws * (node_width - 2))}╱{ws}"
    rgt_br = f"{ws}╲{(ws * (node_width - 2))}"
    cap = f"┌{'─' * cell_width}┐"
    base = f"└{'─' * cell_width}┘"
    space_width = 2

    n = len(nodes)
    nodes = [str(node).zfill(cell_width) for node in nodes]
    tree_height = ceil(log(n + 1, 2))
    max_lvl_nodes = 2 ** (tree_height - 1)
    max_lvl_gaps = max_lvl_nodes - 1
    last_lvl_gap_w = node_width

    max_box_width = (max_lvl_nodes * node_width) + (max_lvl_gaps * last_lvl_gap_w)
    row_width = max_box_width + (space_width * 3)
    rows_n = (tree_height * 4) + 1
    empty_row = ws * (row_width + (cell_width))

    for row_i in range(rows_n):
        if row_i == 0 or row_i == rows_n - 1:
            print(empty_row)
        else:
            lvl_i = row_i // 4
            lvl_slots_n = 2 ** lvl_i
            lvl_gaps_n = lvl_slots_n - 1
            lvl_start = lvl_slots_n - 1
            lvl_stop = (lvl_start * 2) + 1

            lvl_gap_w = (2 ** (tree_height + 2 - lvl_i)) - node_width
            lvl_box_w = (lvl_slots_n * node_width) + (lvl_gaps_n * lvl_gap_w)
            lvl_margin_w = ((row_width - lvl_box_w) // 2) + 1
            lvl_margin = ws * lvl_margin_w
            lvl_gap = ws * lvl_gap_w

            lvl_fill = ""
            if lvl_i + 1 == tree_height:
                max_slots = (2 ** tree_height) - 1
                missing_n = max_slots - n
                lvl_fill_w = (missing_n * node_width) + (missing_n * lvl_gap_w)
                lvl_fill = ws * lvl_fill_w

            lvl_nodes = [f"│{node}│" for node in nodes[lvl_start:lvl_stop]]
            lvl_legend = empty_cell

            if row_i % 4 == 0:
                # branch row
                lvl_nodes = [lft_br if br % 2 == 0 else rgt_br for br in range(len(lvl_nodes))]
            elif (row_i + 1) % 4 == 0:
                # base row
                lvl_nodes = [base for _ in lvl_nodes]
            elif (row_i + 3) % 4 == 0:
                # cap row
                lvl_nodes = [cap for _ in lvl_nodes]
            else:
                lvl_legend = str(lvl_i).zfill(cell_width)

            print(f"{lvl_legend}{lvl_margin[cell_width:]}{lvl_gap.join(lvl_nodes)}{lvl_fill}{lvl_margin}")

# def infix_to_postfix(self, infix_input: list) -> list:

#     precedence_order = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
#     associativity = {'+': "LR", '-': "LR", '*': "LR", '/': "LR", '^': "RL"}

#     clean_infix = self._clean_input(infix_input)

#     i = 0
#     postfix = []
#     operators = "+-/*^"
#     stack = deque()
#     while i < len(clean_infix):

#         char = clean_infix[i]
#         if char in operators:
#             if len(stack) == 0 or stack[0] == '(':
#                 stack.appendleft(char)
#                 i += 1
#             else:
#                 top_element = stack[0]
#                 if precedence_order[char] == precedence_order[top_element]:
#                     if associativity[char] == "LR":

#                         popped_element = stack.popleft()
#                         postfix.append(popped_element)

#                     elif associativity[char] == "RL":

#                         stack.appendleft(char)
#                         i += 1
#                 elif precedence_order[char] > precedence_order[top_element]:

#                     stack.appendleft(char)
#                     i += 1
#                 elif precedence_order[char] < precedence_order[top_element]:
#                     # pop the top element
#                     popped_element = stack.popleft()
#                     postfix.append(popped_element)
#         elif char == '(':

#             stack.appendleft(char)
#             i += 1
#         elif char == ')':
#             top_element = stack[0]
#             while top_element != '(':
#                 popped_element = stack.popleft()
#                 postfix.append(popped_element)

#                 top_element = stack[0]

#             stack.popleft()
#             i += 1
#         else:
#             postfix.append(char)
#             i += 1


#     if len(stack) > 0:
#         for i in range(len(stack)):
#             postfix.append(stack.popleft())

#     return postfix

# def evaluate(self, node=None) -> float:

#       if node.is_leaf():
#           node.value = float(node.val)
#           val = float(node.val)

#           return val

#       left_value = self.evaluate(node.left)
#       right_value = self.evaluate(node.right)

#       if node.data == "+":

#           return left_value + right_value

#       elif node.data == "-":

#           print(f"node value: {node.value}")
#           return left_value - right_value

#       elif node.data == "/":
#           return left_value / right_value

#       elif node.data == "*":
#           return left_value * right_value

#       else:
#           return left_value ** right_value

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

print("\nPreorder traversal of binary tree is")
printPreorder(root)

print("\nMaximum element is",
      findMax(root))
print("\nMin el is", find_min_in_BT(root))

print("\nAfter deletig 3")
root = deleteNode(root, 3)

print("Sorted: ")
printPreorder(root)

if iterativeSearch(root, 9):
    print("This numer (9) is in the tree")
else:
    print("This number(9) isn't in the tree")

