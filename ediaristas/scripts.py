import subprocess

def mySql():
  subprocess.run(['mysql', '-u', 'root', '-p'])
  
def runServer():
  subprocess.run(['python', 'menage.py', 'runserver'])


