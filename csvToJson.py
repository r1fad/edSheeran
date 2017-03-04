import csv
import json

csvfile = open('songs.csv', 'r')
jsonfile = open('songs.json', 'w')

fieldnames = ("id","lyrics","song","url","lyrics_vector","X","Y")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ], sort_keys=True, indent=2 )
jsonfile.write(out)