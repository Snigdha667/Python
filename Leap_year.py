def is_leap(year):
    leap = False
    leap1 = True
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return leap1
            else:
                return leap
        else:
            return leap1
    else:
        return leap
                
        
    # Write your logic here
    


year = int(raw_input())
print is_leap(year)