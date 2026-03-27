def ft_helper(day):
    if (day > 0):
          ft_helper(day - 1)
          print(f"Day {day}")

def ft_count_harvest_recursive():
       day = int(input("Days until harvest: "))
       ft_helper(day)
       print("Harvest time!")