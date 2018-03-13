# matching-intervals
This piece of script is used in the paper "Fine-scale characterization of genomic structural variation in the human genome reveals adaptive and biomedically relevant hotspots" (under reviewed)
It requires two input files to run, the first one contains the hotspot intervals to be matched, and the second one contains the candidate non-hotspot intervals that can possibly match the hotspots in the first file.
These input files need to be in bed format, with the first three columns describing coordinates of intervals and the rest columns describing the features of intervals. 
This piece of script would search from the second file for intervals with their composition similar (<10% differences) the intervals in the first file. The criteria for matching can be change depending on different purpose. Currently, these include GC content, SNP, exon_bp, gene_bp, SegDup_bp, SINE_bp, LINE_bp, DNA_bp.
The succesfully matched pairs would be written into a designated output file, with the intervals from the first file denoted as "hotspot" and the intervals from the second file denoted as "hotspot-match". 
