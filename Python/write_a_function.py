def is_leap(year):
    if(year%4==0):
        if(not(year%100==0)):
            return True
        elif year%400==0:
            return True
        else: 
            return False
    else:
        return False

year = int(input())
print(is_leap(year))