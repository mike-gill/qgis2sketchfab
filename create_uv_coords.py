#-------------------------------------------------------------------------------
# Name:        create_uv_coords
# Purpose:     Adds uv coordinates for a .obj file exported from
#              qgis2threejs
#
# Author:      Mike Gill, Avon Valley Archaeological Society
#
# Created:     27/08/2016
#
# MIT License
#
# Copyright (c) 2017 Mike Gill, Avon Valley Archaeological Society
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#-------------------------------------------------------------------------------

import sys
import os

def calc_stats(fin):
    min_x = 9999999.0
    max_x = -9999999.0
    min_z = 9999999.0
    max_z = -9999999.0

    for line in fin:
        tokens = line.split(' ')
        if tokens[0] == 'v':
            min_x = min(min_x, float(tokens[1]))
            max_x = max(max_x, float(tokens[1]))
            min_z = min(min_z, float(tokens[3]))
            max_z = max(max_z, float(tokens[3]))

    return (min_x, max_x, min_z, max_z)

def calc_x_ordinate(min, range, value):
    return 1.0 - ((value - min) / range)

def calc_z_ordinate(min, range, value):
    return (value - min) / range

def write_uv(fin, fout, stats):

    x_range = stats[1] - stats[0]
    z_range = stats[3] - stats[2]

    for line in fin:
        tokens = line.split(' ')

        if tokens[0] == 'v':
            fout.write(line)
            fout.write("vt {0} {1}\n".format(
                calc_x_ordinate(stats[0], x_range, float(tokens[1])),
                calc_z_ordinate(stats[2], z_range, float(tokens[3]))
                ))
        elif tokens[0] == 'f':
            fout.write("f {0}/{0} {1}/{1} {2}/{2}\n" .format(
                tokens[1], tokens[2], int(tokens[3])))

        else:
            fout.write(line)



def main(fn_in, fn_out):
    with open(fn_in) as fin:
        with open(fn_out, 'w') as fout:
            stats = calc_stats(fin)
            print(stats)
            fin.seek(0)
            write_uv(fin, fout, stats)


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage:  create_uv_coords.py <in filename> <out filename>")
        print("Command line example:  python create_uv_coords.py model.obj model_with_uv.obj")
        print("Note:  if file names or their paths have spaces, wrap them in double quotes.")
        sys.exit()

    fn_in = sys.argv[1]
    fn_out = sys.argv[2]
    main(fn_in, fn_out)

