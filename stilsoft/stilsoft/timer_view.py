import time

seconds = 360
while True:
    d = str('{:02}:{:02}:{:02}'.format(seconds // 3600 % 24,
                                       seconds // 60 % 60,
                                       seconds % 60))
    print(d[0:20], end="")
    time.sleep(1)
    print("\r\033[K", end='') # перенос курсора в начало текущей строки
    seconds += 1