Feature: Find the average length of exons of genes in bed format
				 In order to find the average exon length of genes
				 I want to read bedfile
				 And Identify which lines are exons from the name of the feature
				 And substract the start and end of bed feature

Scenario: Identify bed features which are exons and Calculate average exon
				 length from selected bed feature
				 Given a bedfile containing the following lines
				 """
				 1	100	200	exon-1-geneA
				 1	120	150	cds-1-geneA
				 1	300	400	exon-2-geneA
				 1	320	460	cds-2-geneA
				 20	1000	4000	exon-1-geneB
				 """
				 When I choose BED line that contains 'exon' in the 'name' field
				 Then I will get the following lines
				 """
				 1	100	200	exon-1-geneA
				 1	300	400	exon-2-geneA
				 20	1000	4000	exon-1-geneB
				 """
				 And Their average exon length are
				 | gene		 | average_exon_len |
				 | geneA	 |	100				|
				 | geneB	 |	3000			|
