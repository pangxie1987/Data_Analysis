import argparse
parse=argparse.ArgumentParser()
parse.add_argument('integer',type=int,help='display an integer')
args=parse.parse_args()

print(args.integer)