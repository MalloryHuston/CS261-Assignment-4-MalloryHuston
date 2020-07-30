# Course: CS 261 - Data Structures
# Student Name: Mallory Huston
# Assignment: 4, Part 1
# Description: Implementation of a Binary Search Tree data structure.


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty
    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty
    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        if cur.left:
            self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        if cur.right:
            self._str_helper(cur.right, values)

    def add(self, value: object) -> None:
        """
        Inserts value property of new node into BST
        """
        # handle case where BST is empty
        if self.root is None:
            self.root = TreeNode(value)
            return

        # create convenient variables to utilize while iterating through BST
        child = self.root
        parent = None

        # iterate through BST in search of appropriate node placement
        while child is not None:
            parent = child
            if value < child.value:
                child = child.left
            else:
                child = child.right

        # add new_node as child of parent
        if value < parent.value:
            parent.left = TreeNode(value)
        else:
            parent.right = TreeNode(value)

    def contains(self, value: object) -> bool:
        """
        Indicates whether value is present in BST
        """
        # iterate through tree in search of value
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        # value was not found, so return False
        return False

    def get_first(self) -> object:
        """
        Returns value stored at root node of BST
        """
        # handle case where BST is empty
        if self.root is None:
            return None

        # return value property of root node
        return self.root.value

    def remove(self, value: object) -> bool:
        """
        Removes first node with value property matching value argument
        """
        # iterate through tree in search of value
        left_bool = False
        node_found = False
        parent = None
        to_remove = self.root
        while to_remove is not None and not node_found:
            if value == to_remove.value:
                node_found = True
            elif value < to_remove.value:
                parent = to_remove
                to_remove = to_remove.left
                left_bool = True
            else:
                parent = to_remove
                to_remove = to_remove.right
                left_bool = False

        # handle case where value was not found in BST
        if not node_found:
            return False

        # handle case where node to remove is root
        if to_remove == self.root:
            self.remove_first()
            return True

        # handle case where to_remove is a leaf
        if self.is_leaf(to_remove) and left_bool:
            parent.left = None
            return True
        if self.is_leaf(to_remove) and not left_bool:
            parent.right = None
            return True

        # handle case where to_remove only has left subtree
        if to_remove.right is None and left_bool:
            parent.left = to_remove.left
            return True
        if to_remove.right is None and not left_bool:
            parent.right = to_remove.left
            return True

        # handle case where to_remove has a right subtree
        # find left-most child from right subtree
        left_bool_2 = False
        replace_node = to_remove.right
        replace_parent = to_remove
        while replace_node.left is not None:
            replace_parent = replace_node
            replace_node = replace_node.left
            left_bool_2 = True

        # fill open slot from removing new_to_remove
        if left_bool_2:
            replace_parent.left = replace_node.right
        if not left_bool_2:
            replace_parent.right = replace_node.right

        # insert left-most child from right subtree in open spot
        if left_bool:
            parent.left = replace_node
            replace_node.left = to_remove.left
            replace_node.right = to_remove.right
            return True
        if not left_bool:
            parent.right = replace_node
            replace_node.left = to_remove.left
            replace_node.right = to_remove.right
            return True

    def remove_first(self) -> bool:
        """
        Removes root node from BST
        """
        # handle case where BST is empty
        if self.root is None:
            return False

        # handle case where root is a leaf
        if self.is_leaf(self.root):
            self.root = None
            return True

        # handle case where root has NO right subtree
        if self.root.right is None:
            self.root = self.root.left
            return True

        # handle case where root has a right subtree
        # iterate through right subtree in search of left-most child
        replace_node = self.root.right
        replace_parent = self.root
        left_bool = False
        while replace_node.left is not None:
            replace_parent = replace_node
            replace_node = replace_node.left
            left_bool = True

        # remove leftmost child (replace_node) from tree
        if left_bool:
            replace_parent.left = replace_node.right
        else:
            replace_parent.right = replace_node.right

        # insert leftmost child into root position
        replace_node.left = self.root.left
        replace_node.right = self.root.right
        self.root = replace_node
        return True

    def pre_order_traversal(self) -> Queue:
        """
        Performs pre-order traversal of BST
        """
        # initialize Queue to add TreeNode objects to
        q = Queue()

        # handle case where BST is empty
        if self.root is None:
            return q

        # utilize recursive helper function in processing non-empty BST and return resulting Queue
        self.pre_order_helper(self.root, q)
        return q

    def pre_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function to pre_order_traversal()
        """
        # process current node
        q.enqueue(node)

        # if node.left exists, navigate traversal to node.left
        if node.left is not None:
            self.pre_order_helper(node.left, q)

        # if node.right exists, navigate traversal to node.right
        if node.right is not None:
            self.pre_order_helper(node.right, q)

    def in_order_traversal(self) -> Queue:
        """
        Performs in-order traversal of BST
        """
        # initialize Queue to add TreeNode objects to
        q = Queue()

        # handle case where BST is empty
        if self.root is None:
            return q

        # utilize recursive helper function in processing non-empty BST and return resulting Queue
        self.in_order_helper(self.root, q)
        return q

    def in_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function to in_order_traversal()
        """
        # if node.left exists, navigate traversal to node.left then process current node
        if node.left is not None:
            self.in_order_helper(node.left, q)

        # process current node
        q.enqueue(node)

        # if node.right exists, navigate traversal to node.right
        if node.right is not None:
            self.in_order_helper(node.right, q)

    def post_order_traversal(self) -> Queue:
        """
        Performs post-order traversal of BST
        """
        # initialize Queue to add TreeNode objects to
        q = Queue()

        # handle case where BST is empty
        if self.root is None:
            return q

        # utilize recursive helper function in processing non-empty BST and return resulting Queue
        self.post_order_helper(self.root, q)
        return q

    def post_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function to post_order_traversal()
        """
        # if node.left exists, navigate traversal to node.left then process current node
        if node.left is not None:
            self.post_order_helper(node.left, q)

        # if node.right exists, navigate traversal to node.right
        if node.right is not None:
            self.post_order_helper(node.right, q)

        # process current node
        q.enqueue(node)

    def by_level_traversal(self) -> Queue:
        """
        Performs by-level traversal of BST
        """
        # initialize Queue objects to help with processing BST
        working_q = Queue()
        final_q = Queue()

        # handle case where BST is empty
        if self.root is None:
            return final_q

        # start process by placing BST.root in working_q
        working_q.enqueue(self.root)

        # iterate through BST laterally, adding TreeNode's to working_q for processing
        while not working_q.is_empty():
            working_node = working_q.dequeue()
            if working_node is not None:
                final_q.enqueue(working_node)
                working_q.enqueue(working_node.left)
                working_q.enqueue(working_node.right)

        return final_q

    def is_full(self) -> bool:
        """
        Indicates whether BST is full
        """
        # handle case where BST is empty
        if self.root is None:
            return True

        # handle case where BST has single root node
        if self.root.left is None and self.root.right is None:
            return True

        # call recursive helper function
        return self.is_full_helper(self.root)

    def is_full_helper(self, node: object) -> bool:
        """
        Recursive helper function for is_full()
        """
        # handle base case where node is a leaf
        if self.is_leaf(node):
            return True

        # handle base case where node has single child
        if node.left is None and node.right is not None:
            return False
        if node.left is not None and node.right is None:
            return False

        # handle recursive case where node has two children
        return True and self.is_full_helper(node.left) and self.is_full_helper(node.right)

    def is_complete(self) -> bool:
        """
        Determines whether BST is complete
        """
        # handle case where BST is empty
        if self.root is None:
            return True

        # handle case where BST is perfect
        if self.is_perfect():
            return True

        # start process by placing BST.root in q for processing
        q = Queue()
        q.enqueue(self.root)

        # iterate through BST laterally, adding TreeNode's to q for processing
        need_leaves = False
        while not q.is_empty():
            node = q.dequeue()

            # handle cases where we do not need all leaves
            if not need_leaves:
                # handle case where node.left is None but working_node.right is populated
                if node.left is None and node.right is not None:
                    return False

                # handle case where node is a leaf
                elif self.is_leaf(node):
                    need_leaves = True

                # handle case where node.left is populated but working_node.right is None
                elif node.left is not None and node.right is None:
                    need_leaves = True
                    q.enqueue(node.left)

                # handle case where node has two children
                if not need_leaves and node.left is not None and node.right is not None:
                    q.enqueue(node.left)
                    q.enqueue(node.right)

            # handle cases where we need all leaves
            elif need_leaves:
                if not self.is_leaf(node):
                    return False

        # if program makes it this far, BST is complete
        return True

    def is_perfect(self) -> bool:
        """
        Determines whether BST is perfect
        """
        # handle case where BST is empty
        if self.root is None:
            return True

        # iterate through BST while testing for perfect property
        height = self.height()
        return self.is_perfect_helper(self.root, 0, height)

    def is_perfect_helper(self, node: object, iter: int, iter_limit: int) -> bool:
        """
        Recursive helper function for is_perfect()
        """
        # handle base case where iteration limit reached without returning false
        if iter == iter_limit:
            return True

        # handle base case where node with < 2 children found
        if node.left is None or node.right is None:
            return False

        # handle recursive case where node has 2 children
        return self.is_perfect_helper(node.left, iter + 1, iter_limit) and self.is_perfect_helper(node.right, iter + 1,
                                                                                                  iter_limit)

    def size(self) -> int:
        """
        Returns the number of TreeNodes in BST
        """
        # handles case where BST is empty
        if self.root is None:
            return 0

        # call recursive helper function to count distinct nodes
        return self.size_helper(self.root)

    def size_helper(self, node: object) -> int:
        """
        Recursive helper function for size()
        """
        # process current node
        count = 1

        # recursively call size_helper() on left subtree of current node
        if node.left is not None:
            count += self.size_helper(node.left)

        # recursively call size_helper() on right subtree of current node
        if node.right is not None:
            count += self.size_helper(node.right)

        return count

    def height(self) -> int:
        """
        Returns height of BST
        """
        # handle case where BST is empty
        if self.root is None:
            return -1

        # call recursive helper function to count max number of traversals to leaf in BST
        return self.height_helper(self.root)

    def height_helper(self, node: object) -> int:
        """
        Recursive helper function for height()
        """
        # handle base case where current node is a leaf
        if self.is_leaf(node):
            return 0

        # handle recursive case where current node has a single child
        if node.left is not None and node.right is None:
            return 1 + self.height_helper(node.left)
        if node.left is None and node.right is not None:
            return 1 + self.height_helper(node.right)

        # handle case where node has two children
        if self.height_helper(node.left) > self.height_helper(node.right):
            return 1 + self.height_helper(node.left)
        else:
            return 1 + self.height_helper(node.right)

    def count_leaves(self) -> int:
        """
        Counts number of nodes in BST that have no children
        """
        # handle case where BST is empty
        if self.root is None:
            return 0

        # call recursive helper function to count total leaves
        return self.count_leaves_helper(self.root)

    def count_leaves_helper(self, node: object) -> int:
        """
        Recursive helper function for count_leaves()
        """
        # handle base case where current node is a leaf
        if self.is_leaf(node):
            return 1

        # handle recursive case where current node has single child
        if node.left is not None and node.right is None:
            return self.count_leaves_helper(node.left)
        if node.left is None and node.right is not None:
            return self.count_leaves_helper(node.right)

        # handle recursive case where current node has two children
        return self.count_leaves_helper(node.left) + self.count_leaves_helper(node.right)

    def count_unique(self) -> int:
        """
        Counts number of nodes with unique values
        """
        # handle case where BST is empty
        if self.root is None:
            return 0

        # call recursive helper function to count unique values
        q = Queue()
        return self.count_unique_helper(self.root, q)

    def count_unique_helper(self, node: object, q: object) -> int:
        """
        Recursive helper function for count_unique()
        """
        # iterate through q to determine whether node.value exists within q
        temp_q = Queue()
        new_value = True
        while not q.is_empty() and new_value:
            current_node = q.dequeue()
            temp_q.enqueue(current_node)
            if node.value == current_node.value:
                new_value = False

        # enqueue nodes from temp_q back into q
        while not temp_q.is_empty():
            current_node = temp_q.dequeue()
            q.enqueue(current_node)

        # assign integer indication of whether current node had new value to convenient variable
        current_add = 0
        if new_value:
            q.enqueue(node)
            current_add = 1

        # handle base case where current node is leaf
        if self.is_leaf(node):
            return current_add

        # handle recursive case where current node has a single child
        if node.left is not None and node.right is None:
            return current_add + self.count_unique_helper(node.left, q)
        if node.left is None and node.right is not None:
            return current_add + self.count_unique_helper(node.right, q)

        # handle case where current node has two children
        return current_add + self.count_unique_helper(node.left, q) + self.count_unique_helper(node.right, q)

    def is_root(self, node: object) -> bool:
        """
        Indicates whether TreeNode passed as argument is root
        """
        if node == self.root:
            return True
        else:
            return False

    def is_leaf(self, node: object) -> bool:
        """
        Indicates whether TreeNode passed as argument is a leaf
        """
        if node.left is None and node.right is None:
            return True
        else:
            return False


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')
