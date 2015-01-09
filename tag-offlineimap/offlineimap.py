import os
import subprocess
import sys
import re

def nametrans_remote(folder):
  return re.sub("^\[Gmail\]/Drafts$", "drafts",
  re.sub("^\[Gmail\]/Important$", "important",
  re.sub("^\[Gmail\]/Sent Mail$", "sent",
  re.sub("^\[Gmail\]/Starred$", "flagged",
  re.sub("^INBOX$", "inbox", folder)))))

def nametrans_local(folder):
  return re.sub('^drafts$',    '[Gmail].Drafts',
  re.sub('^important$', '[Gmail].Important',
  re.sub('^sent$',      '[Gmail].Sent Mail',
  re.sub('^flagged$',   '[Gmail].Starred',
  re.sub('^inbox$',     'INBOX',  folder)))))

def folder_filter(folder):
  return folder not in ['[Gmail]/All Mail', '[Gmail]/Spam', '[Gmail]/Trash']

def mailpasswd(gpg_file):
  path = "%s/.passwords/%s" % (os.getenv("HOME"), gpg_file)
  args = ["gpg", "--quiet", "--batch", "--no-tty", "--decrypt", path]
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
