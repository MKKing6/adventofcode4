input = open("input.txt").readlines()

# part 1
# for card in input:
#   score = 0
#   winningNums = []
#   yourNums = []
#   nums = card.split(":")[1].split("|")
#   for i in range(len(nums)):
#     num = nums[i].strip()
#     if i % 2 == 0:
#       winningNums = num.split()
#     else:
#       yourNums = num.split()
#   for i in winningNums:
#     for j in yourNums:
#       if int(j) == int(i):
#         score += 1
#   if score > 0:
#     sum += 2 ** (score - 1)
# print(sum)

score = []
queue = []
sum = 0

#part 2
def checkCards():
  global sum
  for index, card in enumerate(input):
    copy = 0
    winningNums = []
    yourNums = []
    nums = card.split(":")[1].split("|")
    for i in range(len(nums)):
      num = nums[i].strip()
      if i % 2 == 0:
        winningNums = num.split()
      else:
        yourNums = num.split()
    for i in winningNums:
      for j in yourNums:
        if int(j) == int(i):
          copy += 1
    score.append(copy)
    for i in range(index + 1, index + 1 + copy):
      if i < len(input):
        queue.append(i)
    sum += 1

checkCards()
while len(queue) > 0:
  i = queue.pop()
  for j in range(i + 1, i + 1 + score[i]):
    if j < len(input):
      queue.append(j)
  sum += 1
print(sum)
