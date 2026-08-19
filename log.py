import subprocess
import json

out = subprocess.check_output([r"C:\Program Files\Git\cmd\git.exe", "log", "--format=%H|%P|%an|%ae|%ad|%s", "--reverse"])
lines = out.decode('utf-8').strip().split('\n')

commits = []
for line in lines:
    parts = line.split('|', 5)
    if len(parts) == 6:
        commits.append({
            'hash': parts[0],
            'parents': parts[1].split(),
            'name': parts[2],
            'email': parts[3],
            'date': parts[4],
            'msg': parts[5]
        })

with open("commits.json", "w", encoding='utf-8') as f:
    json.dump(commits, f, ensure_ascii=False, indent=2)
