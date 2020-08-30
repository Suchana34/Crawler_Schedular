from datetime import datetime

with open(datetime.now().strftime("%d-%m-%Y"), "w") as file:
    file.write('we automated the task using python and python anywhere')
