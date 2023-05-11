import streamlit as sl
import time as ts
from datetime import time

def convert(value):
    m, s, ms = value.split(":")
    t_s = (int(m)*60) + int(s) + (int(ms)/1000)
    return t_s


val = sl.time_input("set timer", value=time(0, 0, 0))
print(val)
if str(val) == "00:00:00":
    sl.write("please set time")
else:
    sec = convert(str(val))
    bar = sl.progress(0)
    perc = sec/100
    progress_status = sl.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1) + "%")
        ts.sleep(perc)
    