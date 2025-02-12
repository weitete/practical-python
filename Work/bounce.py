# bounce.py
#
# Exercise 1.5
height=100
numberof_bounce=1
while numberof_bounce<=10:
    height = (height * 3) / 5
    print(numberof_bounce,round(height,4))
    numberof_bounce += 1


print('Total bounces',numberof_bounce)
print('Final height',round(height,4))