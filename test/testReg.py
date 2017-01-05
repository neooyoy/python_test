import re

phone_num = "home (mobile): (555)-265-2901"

results = re.search('\((\d{3})\)', phone_num)
area_code = results.group(1)

print('the are code is: ' + area_code)