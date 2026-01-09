import sys
import os
print(f"Python executable: {sys.executable}")
print(f"CWD: {os.getcwd()}")
try:
    import data.final_tutorials
    print(f"File location: {data.final_tutorials.__file__}")
    db = data.final_tutorials.TUTORIALS_DATABASE
    print(f"Database length: {len(db)}")
    print("Sample items:")
    for item in db[:5]:
        print(item.get('title'))
    print("--- End items ---")
    for item in db[-5:]:
        print(item.get('title'))
except Exception as e:
    print(f"Error: {e}")
