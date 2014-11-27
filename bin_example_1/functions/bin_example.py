from functions.bin_example import *
import re
from collections import defaultdict
import numpy as np




def extract_exon(input_bed):
    exon_features = []
    bed_features = input_bed.split('\n')
    for entry in bed_features:
        if re.search('exon', entry):
            exon_features.append(entry)
    return exon_features



def find_average(input_bed):
    transcript_exons = defaultdict(list)
    bed_features = input_bed.split('\n')

    for entry in bed_features:
        bed_fields = re.split('\t|-', entry)
        gene_name = bed_fields[-1]
        exon_length = int(bed_fields[2]) - int(bed_fields[1])
        transcript_exons[gene_name].append(exon_length)

    for key, value in transcript_exons.iteritems():
        transcript_exons[key]= np.mean(value)

    return trnanscript_exons
