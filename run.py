from util import merge_csv
from glob import glob

files = glob('./result/opensmile/**/result_condition*.csv')

for input_file in files:
    merge_csv.merge_csv(input_file)
