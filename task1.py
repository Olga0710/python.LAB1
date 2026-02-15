from pathlib import Path

CODE_LIST = {'.cpp', '.hpp', '.c', '.h', '.py', '.pyw', '.cs', '.js', '.java'}
WHITE_LIST = CODE_LIST | {'.html', '.json', '.txt', '.ipynb'}

folders = [r"C:\Users\User\Projects\C++.SEM1",
          r"C:\Users\User\Projects\C++.SEM3",
          r"C:\Users\User\Projects\OPP.SEM1"]

def kind(extension):   
    if extension in WHITE_LIST:
        return 'W'
    elif extension in CODE_LIST:
        return 'C'
    else: 
        return 'O'

d={}

for folder in folders:
    folder_path = Path(folder)
    for el in folder_path.glob("**/*"):
        if el.is_file():
            ext = el.suffix.lower()
            d[ext]=d.setdefault(ext,0)+1

sorted_list = sorted(d.items(), key=lambda x:x[1], reverse=True)
print (f"{'Ext':>23} {'Cnt':>6} {'Cat':>3}")
for ext, cnt in sorted_list:
    cat = kind(ext)
    print(f"{ext:>23} {cnt:6} {cat:>3}")
