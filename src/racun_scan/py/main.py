import argparse
import html_racun_parser

parser = argparse.ArgumentParser(description='Extract data from fiskalni racun')
parser.add_argument('--racun')

args = parser.parse_args()

filefrom = args.racun

result = html_racun_parser.extract_all_positions_as_table(filefrom)
print (result)
