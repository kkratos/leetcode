# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    re = []
    while l is not None:
        if l.value != k:
            re.append(l.value)
        l = l.next
    return re
