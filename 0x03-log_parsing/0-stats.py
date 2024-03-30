#!/usr/bin/python3
"""
this the the code to impliment a log parsing
scenario using regex and signals to achieve desired
outcomes
"""
import sys
import re
import signal
import time

regex_str = (r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} '
             r'\d{2}:\d{2}:\d{2}\.\d{6})\] ("GET /projects/260 HTTP/1.1") '
             r'(\d{3} \d{1,4})$')
file = r'\d{1,4}$'
status = r'(200|301|400|401|403|404|405|500)'
count = 0
file_size = 0
buffer = {}


def printing():
    print(f"File size: {file_size}")
    srt_buffer = dict(sorted(buffer.items()))
    for k, v in srt_buffer.items():
        print(f"{k}: {v}")


def interrupt_handler(signum, frame):
    printing()


signal.signal(signal.SIGINT, interrupt_handler)
signal.signal(signal.SIGPIPE, interrupt_handler)


for line in sys.stdin:
    try:
        if (count == 10):
            count = 0
            printing()
        if re.match(regex_str, line):
            fs = re.search(file, line)
            file_size += int(fs.group())
            st = re.search(status, line)
            st_code = int(st.group())
            value = buffer.get(st_code, 0)
            value += 1
            buffer[st_code] = value
        count += 1
    except Exception as e:
        continue

printing()

'''
if re.match(regex_str, tester):
    print("yes")
else:
    print("no")
gg = re.search(file, tester)
if gg:
    print("yes")
    print(gg.group())
else:
    print("no")
rr = re.search(status, tester)
if rr:
    print("yes")
    print(rr.group())
else:
    print("no")
'''
