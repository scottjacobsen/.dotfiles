import os
import subprocess
import sys

def mailpasswd(gpg_file):
  path = "%s/.passwords/%s" % (os.getenv("HOME"), gpg_file)
  args = ["gpg2", "--quiet", "--batch", "--no-tty", "--decrypt", path]
  try:
    return subprocess.check_output(args).strip()
  except subprocess.CalledProcessError:
    return ""

def prime_gpg_agent():
  ret = False
  i = 1
  while not ret:
    ret = (mailpasswd("prime.gpg") == "prime")
    if i > 2:
      from offlineimap.ui import getglobalui
      sys.stderr.write("Error reading in passwords. Terminating.\n")
      getglobalui().terminate()
    i += 1
  return ret

prime_gpg_agent()
