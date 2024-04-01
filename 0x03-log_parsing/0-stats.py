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

regex_str = (r'^([^\s]+)\s*-\s*\[(\d{4}-\d{2}-\d{2} '
             r'\d{2}:\d{2}:\d{2}\.\d{6})\] ("GET /projects/260 HTTP/1.1") '
             r'(\d{3} \d{1,4})$')
file = r'\d{1,4}$'
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

for line in sys.stdin:
    try:
        if (count == 10):
            count = 0
            printing()
        fs = re.search(file, line)
        file_size += int(fs.group())
        if re.match(regex_str, line):
            st_code = line.split()[-2]
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
