class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next



#Explanation : 

class Solution:
    def addTwoNumbers(self, l1, l2):

        # Create a dummy node to start the answer linked list
        dummy = ListNode()

        # 'curr' is used to build the new linked list
        curr = dummy

        # Stores the carry from the previous addition
        carry = 0

        # Continue while l1 has nodes, l2 has nodes, or carry is non-zero
        while l1 or l2 or carry:

            # Get the value of the current node of l1, otherwise use 0
            x = l1.val if l1 else 0

            # Get the value of the current node of l2, otherwise use 0
            y = l2.val if l2 else 0

            # Add both digits and the carry
            total = x + y + carry

            # Get the carry for the next iteration
            carry = total // 10

            # Store the last digit of total in a new node
            curr.next = ListNode(total % 10)

            # Move curr to the newly created node
            curr = curr.next

            # Move l1 to its next node if it exists
            if l1:
                l1 = l1.next

            # Move l2 to its next node if it exists
            if l2:
                l2 = l2.next

        # Return the answer list (skip the dummy node)
        return dummy.next
