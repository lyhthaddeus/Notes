def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    temp = ListNode()
    curr = temp

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        carry = total // 10
        total = total % 10
        
        curr.next = ListNode(total)
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2: 
            l2 = l2.next
    
    return temp.next
