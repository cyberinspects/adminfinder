# Fastest adminfinder
Administrator login and dashboard page finder in python.
## Feautures
1. Completely commad-line tool, easy to integrate in your bash or python scripts
2. Multithreaded - You can choose the number of threads to run.
3. Custom wordlist support.
4. Comes with a nice defualt wordlist
5. Support to find PHP,HTML,ASP,HTML,JS,CFM,CGI and BRF pages.
## How to install
```
git clone https://github.com/cyberinspects/adminfinder
cd adminfinder
pip3 install -r requirements.txt
python3 adminfinder.py
```
## How to use
usage: adminfinder.py [-h] -u U [-t T] [-w W]

Administrator login and dashboard page finder in python3.

options:
  -h, --help  show this help message and exit
  -u U        Define a target using domain name without any protocls.
  -t T        Number of threads to work parallelly
  -w W        Wordlist to use for page findings
## Author
The script is developed by Kaleem Ibn Anwar (@kaleemibnanwar), He is a professional python programmer and Cyber Security expert. He is also the owner of cyberinspects vendor. You may follow or contact him on @kaleemibnanwar social media.

