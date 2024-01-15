# def info(word):
#     print(word, end=' ')
#     print('for u')
#
#
# def summa(a, b):
#     res = a + b
#     info(res)
#     return res
#
#
# res1 = summa(5, 7)
# summa(5.6, 4.6)
# print(res1)

def minimal(l):
    min1 = l[0]
    for i in l:
        if i < min1:
            min1 = i
    print(min1)


nums1 = [5, 4, 7, 4, -8, 45, 5]
minimal(nums1)
nums2 = [5, 4, 7, 4, 45, 5]
minimal(nums2)