#!/bin/bash

set -e

# Input file: mock_data.tsv
# COmmand: tr '/t' ',' < file.tsv> file.csv
#tr command = translate/convert

if [-z "$1" ]; then
	echo "this script converts a TSV into a CSV";
	echo "Append the input name and then the output file name";
fi

/usr/bin/tr '\t' ',' < $1 > $2
