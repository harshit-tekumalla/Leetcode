# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        while head:
            list.append(head)
            head = head.next
        i = 0
        j = len(list) - 1
        flag = True
        while(i<j):
            if (list[i].val!=list[j].val):
                flag = False
                break
            i+=1
            j-=1
        return flag
            
        
        
