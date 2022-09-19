# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1 = list1
        temp2 = list2
        if(not list1):
            return list2
        if(not list2):
            return list1
        if(list1.val < list2.val):
            head = ListNode(list1.val)
            temp1 = temp1.next 
        else:
            head = ListNode(list2.val)
            temp2 = temp2.next
        currnode = head
        while(temp1 and temp2):
            if(temp1.val < temp2.val):
                node = ListNode(temp1.val)
                temp1 = temp1.next
                currnode.next = node
                currnode = currnode.next
            else:
                node = ListNode(temp2.val)
                temp2 = temp2.next
                currnode.next = node
                currnode = currnode.next
        while(temp1):
            node = ListNode(temp1.val)
            temp1 = temp1.next
            currnode.next = node
            currnode = currnode.next
        while(temp2):
            node = ListNode(temp2.val)
            temp2 = temp2.next
            currnode.next = node
            currnode = currnode.next
        return head