import os
import subprocess
import sys
import re

def nametrans_remote(folder):
  return re.sub("^\[Gmail\]/Drafts$", "drafts",
  re.sub("^\[Gmail\]/Trash$", "trash",
  re.sub("^\[Gmail\]/Spam$", "spam",
  re.sub("^\[Gmail\]/Sent Mail$", "sent",
  re.sub("^\[Gmail\]/Starred$", "flagged",
  re.sub("^INBOX$", "inbox", folder))))))

def nametrans_local(folder):
  return re.sub('^drafts$', '[Gmail].Drafts',
  re.sub('^trash$', '[Gmail].Trash',
  re.sub('^spam$', '[Gmail].Spam',
  re.sub('^sent$', '[Gmail].Sent Mail',
  re.sub('^flagged$', '[Gmail].Starred',
  re.sub('^inbox$', 'INBOX', folder))))))

def folder_filter(folder):
  return folder not in ['[Gmail]/All Mail', '[Gmail]/Important', '[Gmail]/Spam', '[Gmail]/Trash']

def mailpasswd(path):
  args = ["/usr/local/bin/pass", "show", path]
  try:
    return subprocess.check_output(args).strip()
  except subprocess.CalledProcessError:
    return ""
