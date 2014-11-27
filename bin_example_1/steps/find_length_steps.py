from behave import *
from functions.bin_example import extract_exon, find_average

@given(u'a bedfile containing the following lines')
def step_impl(context):
	input_bed =  context.text
	context.input = input_bed
	prove = u"""1	100	200	exon-1-geneA
1	120	150	cds-1-geneA
1	300	400	exon-2-geneA
1	320	460	cds-2-geneA
20	1000	4000	exon-1-geneB"""
	assert context.input == prove

@when(u'I choose BED line that contains \'exon\' in the \'name\' field')
def step_impl(context):
	exons = extract_exon(context.input)
	context.output = exons

@then(u'I will get the following lines')
def step_impl(context):
	context.output = "\n".join(context.output)
	assert context.output == str(context.text)

@then(u'Their average exon length are')
def step_impl(context):
	mock_lengths =  {}
	for rows in context.table :
		mock_lengths[rows['gene']] = int(rows['average_exon_len'])
	print mock_lengths
	print find_average(context.output)
	assert mock_lengths == find_average(context.output)
