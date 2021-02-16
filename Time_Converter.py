def timeConverter(seconds):
    
    try:
        seconds=int(seconds)

        if seconds>359999:
            return 'Invalid Input' 
        elif seconds<0:
            return 'Invalid Input'
        else:            
            hour = seconds // 3600
            hourmod = seconds % 3600
            minute = hourmod // 60
            minutemod = hourmod % 60
            second = minutemod

            return f'{hour:02d}:{minute:02d}:{second:02d}'
        
    except:
        return 'Invalid Input'

print(timeConverter(input('Masukkan detik: ')))