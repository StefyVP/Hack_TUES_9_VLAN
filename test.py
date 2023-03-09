import re

line = "should we use regex more often? let me know at  jdsk@bob.com.lol or popop@coco.com"
match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)

print(match)

line_egn = "0450036377"
match_egn = re.findall(r'')
