import datetime

now = datetime.datetime.now()
timeStar = now.strftime("%w")
if (int(timeStar) == 1):
     timeStar="Mon"
     
    
print(timeStar)