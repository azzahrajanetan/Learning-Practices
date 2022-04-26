import glob
import os
import shutil
import json
try: # if this fails, it will run line 9 
    os.mkdir("./processed") #create a processed directory 
except OSError:
    print("'processed' directory already exists")
# Get a list of receipts #./processed/new/receipt-0.json
receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0
print(receipts)
#
for path in receipts: #loop
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
        name = path.split('/')[-1]
        destination = f"./processed/{name}"
        shutil.move(path, destination) # this is where you move each receipt to the processed directory
        print(f"moved '{path}' to '{destination}'")
    print("Receipt subtotal: $%.2f" % subtotal)