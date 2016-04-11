#!/usr/bin/env python

"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.
"""

import sys
import csv
from collections import defaultdict

output_file = 'test.data'
present_str = "present"

def construct_line( label, line ):
	new_line = []
	if float( label ) == 0.0:
		label = "0"
	new_line.append( label )

	for i, item in enumerate( line ):
		if item == '' or float( item ) == 0.0:
			continue
		new_item = "%s:%s" % ( i + 1, item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

# ---


def csv2libsvm(input_file, label_index, skip_headers):

        i = open( input_file, 'rb' )
        o = open( output_file, 'wb' )

        reader = csv.reader( i )

        if skip_headers:
                headers = reader.next()

        for line in reader:
                if label_index == -1:
                        label = '1'
                else:
                        label_str = line.pop( label_index )
                        #print label_str
                        if(label_str == present_str):
                                label = '1'
                        else:
                                label = '0'
                new_line = construct_line( label, line )
                o.write( new_line )
        return output_file
