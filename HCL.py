# l1 = [1, 2, 3, 4]
# l2 = [2, 3, 4, 5]
#
# l3 = list(map(lambda x, y: x + y, l1, l2))
# print(l3)
# a = len(l1)
# b = len(l2)
# l3 = []
# if a == b:
#     for i in range(a):
#         l3.append(int(l1[i]) + int(l2[i]))
# print(l3)


# l = [1, 'a', 'cac', 2, 'dd', 'mine', 'gog']
# res_l = [i for i in l if isinstance(i, str)]
#
# def check_palindrome(param):
#     for i in range(len(param)):
#         if param[i] == param[len(param) - 1-i]:
#             return param
#         else:
#             return False
#
# for i in range(len(res_l)):
#     param = check_palindrome(res_l[i])
#     if param:
#         print(param)

# import re
# with open('response','r')as fp:
#     data = fp.readlines()
#
#
# for i in data:
#     ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', i)
#     print(ip)
#
# print(ip)

# data = {'vinod': 1, 'raju': 2, 'rashmi': 0}
# #l = list(data.values())
#
# print(sorted(data.items(), key=lambda d: (d[0],d[1])))

no_boxes = int(input('Please enter the number of boxes: '))
no_chocolates = int(input('Please enter the total number of chocolates: '))
days = int(input('Please enter the number of days: '))
last_box = int(input('Please enter the chocolate count in last box: '))
print('The number of chocolates {}'.format(no_boxes))
boxes = list(range(no_boxes))
boxes = boxes[::-1]  # reverse the boxes count for easy adding chocolates
boxes[0] = last_box  # adding the last box chocolate to first box
box_count = [last_box]
count_chocolates_per_day = []
for j in range(days-1):
    for i in range(no_boxes - 2):  # the index needs to added from the second element as the first box is constant
        print(box_count)
        box_count.append(no_chocolates - box_count[i:])
    count_chocolates_per_day[j] = sum(boxes)
    print(count_chocolates_per_day)