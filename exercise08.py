def is_leap(year):      # 判斷是否為閏年，閏年return True、平年return False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                if year % 3200 == 0:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(2022))
print(is_leap(2000))
print(is_leap(1900))
print(is_leap(1988))
