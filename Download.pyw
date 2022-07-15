DownloadURL = ''

from mega import Mega
import linkformGit
import os
mega = Mega()
m = mega.login()
m.download_url(DownloadURL)

os.system('EUCTFiles.exe')
os.system('CopyFilesEUCT.exe')
