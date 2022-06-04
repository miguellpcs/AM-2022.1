from argparse import ArgumentParser
import string
import os
import sys
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def arg_parser():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", default='\data\original', metavar='subpath',
                        type=str)
    parser.add_argument("-o", "--output", default='\data\generated', metavar='subpath',
                        type=str)
    parser.add_argument("-m", "--mode", default='no_class', metavar='mode',
                        type=str)
    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    mode = args.mode

    input_subpath = args.input
    output_subpath = args.output

    ''' root_path = str(conf.ROOT_DIR)
    output_path = os.path.join(
        root_path, output_subpath, 'avila-combined-noclass.csv') '''
    #TODO: learn how to work with windows paths and use m
    output_path = os.path.join(
        "c:/", 'Users/poldm/OneDrive/Documentos/GitHub/AM-2022.1/data/generated', 'avila-combined.csv')
    tr_path = os.path.join(
        'c:/', 'Users/poldm/OneDrive/Documentos/GitHub/AM-2022.1/data/original/avila-tr.txt')
    ts_path = os.path.join(
        'c:/', 'Users/poldm/OneDrive/Documentos/GitHub/AM-2022.1/data/original/avila-ts.txt')

    avila_tr = pd.read_csv(tr_path, sep=",")
    avila_ts = pd.read_csv(ts_path, sep=",")

    if mode == 'no_class':
        avila_tr = avila_tr.drop(10, axis=1)
        avila_ts = avila_ts.drop(10, axis=1)
        output_path = os.path.join(
        "c:/", 'Users/poldm/OneDrive/Documentos/GitHub/AM-2022.1/data/generated', 'avila-combined-noclass.csv')

    merged = pd.concat([avila_tr, avila_ts], axis=0)

    merged.to_csv(output_path, index=False)


if __name__ == '__main__':
    main()
