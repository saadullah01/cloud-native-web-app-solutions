'''
    Auto Script to add, commit and push code to GitHub
    Arguments:
    ----------
    commands.txt
'''

import pexpect, os, sys, time

# Variables
username = os.environ["username"]
password = os.environ["access_token"]
repo_name = os.environ["repository_name"]
author = os.environ["author"]

print("Pushing to GitHub Repo '"+repo_name+"'...")
# Clone user's repo
pexpect.run(
    "git clone https://github.com/"+username+"/"+repo_name+".git",
    cwd="/Educative/")

cmd_dir = "/Educative/" + repo_name + "/"

pexpect.run("git switch -c enable-firebase-hosting", cwd=cmd_dir)
pexpect.run("cp -r files/template.html "+cmd_dir+"services/web/src/")
pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m 'Firebase SDK added'", cwd=cmd_dir)
ch = pexpect.spawn("git push --set-upstream origin enable-firebase-hosting", cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(5)
print("Done")