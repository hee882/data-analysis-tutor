import subprocess
import os
import json
import re

def run_git(args, env=None):
    git_exe = r"C:\Program Files\Git\cmd\git.exe"
    cmd = [git_exe] + args
    res = subprocess.check_output(cmd, env=env)
    return res.decode('utf-8').strip()

with open("commits.json", "r", encoding="utf-8") as f:
    commits = json.load(f)

mapping = {}

for c in commits:
    old_hash = c['hash']
    old_parents = c['parents']
    
    # Strip Emojis
    new_msg = c['msg']
    new_msg = re.sub(r'[^\w\s:&\-()가-힣.,/\[\]_]+', '', new_msg)
    new_msg = re.sub(r'^\s+', '', new_msg)
    
    tree = run_git(["log", "-1", "--format=%T", old_hash])
    
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = c['name']
    env["GIT_AUTHOR_EMAIL"] = c['email']
    env["GIT_AUTHOR_DATE"] = c['date']
    env["GIT_COMMITTER_NAME"] = c['name']
    env["GIT_COMMITTER_EMAIL"] = c['email']
    env["GIT_COMMITTER_DATE"] = c['date']
    
    cmd_args = ["commit-tree", tree, "-m", new_msg]
    for p in old_parents:
        cmd_args.extend(["-p", mapping[p]])
        
    new_hash = run_git(cmd_args, env=env)
    mapping[old_hash] = new_hash
    print(f"Mapped {old_hash[:7]} -> {new_hash[:7]}: {new_msg.encode('ascii', 'ignore').decode()}")

last_old_hash = commits[-1]['hash']
last_new_hash = mapping[last_old_hash]
run_git(["reset", "--hard", last_new_hash])
print("Branch successfully updated!")
