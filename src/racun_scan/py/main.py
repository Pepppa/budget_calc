import argparse
import sys
import html_racun_parser

parser = argparse.ArgumentParser(description='Extract data from fiskalni racun')
parser.add_argument('--file')
parser.add_argument('--link')

args = parser.parse_args()

filefrom = args.file
urlfrom = args.link

if filefrom is not None :
    htmlstr = html_racun_parser.retrieve_html_from_file(filefrom)
elif urlfrom is not None :
    htmlstr = html_racun_parser.retrieve_html_from_url(urlfrom)
else :
    print ("Specify either file or url")
    sys.exit()

result = html_racun_parser.extract_all_positions_as_table(htmlstr)

print (result)
