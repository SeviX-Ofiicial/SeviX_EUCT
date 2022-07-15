DownloadURL = ''

from mega import Mega
import linkformGit
mega = Mega()
m = mega.login()

m.download_url(DownloadURL)