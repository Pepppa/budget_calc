import argparse
import sys
import html_racun_parser
import table_constructor
import csv_from_manirs_parser

parser = argparse.ArgumentParser(description='Extract data from fiskalni racun')
parser.add_argument('--htmlfile')
parser.add_argument('--csvfile')
parser.add_argument('--link')

args = parser.parse_args()

htmlfilefrom = args.htmlfile
urlfrom = args.link
csvfilefrom = args.csvfile

if htmlfilefrom is not None :
    htmlstr = html_racun_parser.retrieve_html_from_file(htmlfilefrom)
    extracted_data = html_racun_parser.extract_all_positions_as_dict(htmlstr)
elif csvfilefrom is not None :
    extracted_data = csv_from_manirs_parser.extract_all_positions_as_dict(csvfilefrom)
elif urlfrom is not None :
    htmlstr = html_racun_parser.retrieve_html_from_url(urlfrom)
    extracted_data = html_racun_parser.extract_all_positions_as_dict(htmlstr)
else :
    print ("Specify either file or url")
    sys.exit()

result = table_constructor.construct_importable_table(extracted_data)

print (result)
