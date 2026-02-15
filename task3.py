import sys
import datetime
from pathlib import Path
from datetime import datetime as dt
import csv

CODE_LIST = {'.cpp', '.hpp', '.c', '.h', '.py', '.pyw', '.cs', '.js', '.java'}
WHITE_LIST = CODE_LIST | {'.html', '.json', '.txt', '.ipynb'}

folders = [r"C:\Users\User\Projects\C++.SEM1",
          r"C:\Users\User\Projects\C++.SEM3",
          r"C:\Users\User\Projects\OPP.SEM1"]

def _created_at_Linux(path):    
    p = Path(path)
    stat = p.stat()
    timestamp = min(stat.st_ctime, stat.st_mtime)
    dt_obj = dt.fromtimestamp(timestamp)
    return dt_obj.year, dt_obj.month

def _created_at_Windows(path):
    p = Path(path)
    stat = p.stat()
    timestamp = stat.st_ctime 
    dt_obj = dt.fromtimestamp(timestamp)
    return dt_obj.year, dt_obj.month

if sys.platform.startswith('win'):
    created_at = _created_at_Windows
else:
    created_at = _created_at_Linux  

def lines_counter(path):
   count = 0
   with open(path, encoding ="utf-8", errors="ignore") as f:
       for line in f:
           if line and not line.isspace():
               count+=1
   return count

d = {}
for folder in folders:
    folder_path = Path(folder)
    for el in folder_path.glob("**/*"):
        if el.is_file():
            ext = el.suffix.lower()
            if ext in WHITE_LIST:   
                year, month = created_at(el)
                key = (year, month, ext)

                if key not in d:
                    d[key] = [0, 0, 0]

                d[key][0] += 1                
                d[key][1] += el.stat().st_size  
                
                if ext in CODE_LIST:           
                    d[key][2] += lines_counter(el)
items = sorted(d.items())
with open("lab1_1.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter =";")
    writer.writerow(["year", "mon", "ext", "cnt", "size", "lines", "avg_size", "avg_line"])
    for (year, month, ext), (cnt, size, lines) in items:

        if cnt > 0:
            avg_size = size // cnt
        else:
            avg_size = 0

        if ext in CODE_LIST:
            lines_out = lines
            if cnt > 0:
                avg_line = lines // cnt
            else:
                avg_line = 0
        else:
            lines_out = ""
            avg_line = ""
        writer.writerow([year, month, ext, cnt, size, lines_out, avg_size, avg_line])
