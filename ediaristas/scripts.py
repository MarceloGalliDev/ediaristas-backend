import subprocess

def mysql():
  subprocess.run(['mysql', '-u', 'root', '-p'])

if __name__ == '__main__':
  mysql()
