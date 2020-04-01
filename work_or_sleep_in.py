day = int(input ('Day (0-6)? '))
if day == 0 or day == 6:
    print('Sleep in!!! xoxoxoxo')
elif day >= 1 and day < 6:
    print('Go to work OR ELSE.')
else: 
    print('Please enter a value between 0 and 6.')