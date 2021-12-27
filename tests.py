# # Filter by row
# for y in range(9):
#     for x in range(9):
#         unique = set(self.all_number)
#         if len(possibilities[y][x]) != 1:
#             for i in range(9):
#                 if x != i:
#                     unique = unique - set(possibilities[y][i])
#
#         if len(list(unique & set(possibilities[y][x]))) == 1:
#             possibilities[y][x] = list(unique & set(possibilities[y][x]))
#
# # Filter by column
# for y in range(9):
#     for x in range(9):
#         unique = set(self.all_number)
#         if len(possibilities[y][x]) != 1:
#             for i in range(9):
#                 if y != i:
#                     unique = unique - set(possibilities[i][x])
#
#         if len(list(unique & set(possibilities[y][x]))) == 1:
#             possibilities[y][x] = list(unique & set(possibilities[y][x]))
#
# # Filter by square
# for y in range(9):
#     for x in range(9):
#         unique = set(self.all_number)
#         if len(possibilities[y][x]) != 1:
#             for i in range(3):
#                 for j in range(3):
#                     if x != math.floor(x / 3) * 3 + i or y != math.floor(y / 3) * 3 + j:
#                         unique = unique - set(possibilities[math.floor(y / 3) * 3 + j][math.floor(x / 3) * 3 + i])
#
#         if len(list(unique & set(possibilities[y][x]))) == 1:
#             possibilities[y][x] = list(unique & set(possibilities[y][x]))



a = [["a"], ["b", "c"]]

print(type(a))


