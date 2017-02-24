start_PointVal = 1
lst_LeftUp     = []
lst_LeftDown   = []
lst_RightDown  = []
lst_RightUp    = []

pre_Value      = 1
for circleCount in range(1, 501):
    # Calculate for the left up points value
    pre_Value += 2
    val = pre_Value ** 2
    lst_RightUp.append(val)
    # Calculate for the left Down points value
    lst_RightDown.append(val - 6 * circleCount)
    # Calculate for the left Down points value
    lst_LeftDown.append(val - 4 * circleCount)
    # Calculate for the left Down points value
    lst_LeftUp.append(val - 2 * circleCount)

sum_Diagonal  = sum(lst_RightUp)
sum_Diagonal += sum(lst_RightDown)
sum_Diagonal += sum(lst_LeftDown)
sum_Diagonal += sum(lst_LeftUp)
sum_Diagonal += 1
print(sum_Diagonal)