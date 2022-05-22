from argparse import ArgumentParser
import string
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from config import conf

def arg_parser():
    parser = ArgumentParser()
    parser.add_argument("-o", "--output",default='\data\generated', metavar='subpath',
                        type=str)
    parser.add_argument("-m", "--mode", default='no_class', metavar='mode',
                        type=str)
    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()
    mode = args.mode
    output_subpath = args.output
    root_path = conf.ROOT_DIR
    output_path = os.path.join(root_path, output_subpath)
    print(output_path)


if __name__ == '__main__':
    main()
