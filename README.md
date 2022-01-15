# Instagram Follower Tracker
You can check who does, and who does not follow you back on Instagram, as well as who you don't follow back, using this CLI tool. The code runs locally on your machine, ensuring no privacy leaks or data breaches.

### First Time Usage:
1. Download the codebase into your machine, and open check.py in a code editor.
2. Go to line 2, and add the absolute path to the site-package directory, inside the codebase.
3. Go to line 14, and add the username and password of the account using which you wish to inspect other accounts (access account). It is advisable to use a throwaway account for this, since the password is being stored as a non-encrypted file.
4. You can also add a cache path for faster results, although that is completely optional. If you do not wish to do so, please replace the relevant parameter ('cachepath') with an empty string ('').
5. It is also advisable to turn off 2FA for the throwaway access account, in order for the program to function smoothly.
6. At current settings the program, fails or displays inaccurate results for result accounts with 10000+ followers or followings. The codebase can be modified accordingly by increasing the second paramenter in line 39 and 45, which will allow the checking of accounts with followers or followings upto the modified value. It is, however, not advisiable to do so, since it frequently generates bot usage suspicion from Instagram resulting in temporary account suspension. It may also cause data overload in the program, causing it to crash, albeit that is rare.

### Regular Usage:
Run check.py, and enter the username of the account for which you wish to check results, when prompted (result account). Please note that when the result account is private, it is neccesary that the access account is following the result account, at the time of running the program.

### Dependencies:
1. [igramscraper](https://pypi.org/project/igramscraper/)
2. Python 3.9

### Acknowledgement:
[Shubham Kumar Singh](https://github.com/shubhamm-06) for assisting in package management and testing.
