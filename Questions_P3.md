
## Part 3 – Questions
>1. Describe how the assembly changes with different k-mer values using the assembly statistics you have collected. How does the contig length distribution change?

As k-mer size increases, the size of the contigs seem to increase as well (the distribution shifts to the right). We observe larger N50 values for larger contig values which confirms the larger average kmer size.

>2. How does an increased coverage cutoff affect the assembly? What is happening to the de Bruijin graph when you change the value of this parameter? How does velvet calculate its value for ‘auto’?

coverage cutoff will exclude data with coverage under `cov-cutoff`, this means that paths of the de Bruijin Graph where there is little coverage will get cut out. According to the manual `"If determined automatically, this cutoff is simply set to half the expected coverage."`

<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2952100/>

>3. How does increasing minimum contig length affect your contig length distribution and N50?

velvet simply throws out all contigs below the minimum set, meaning that your distribution of lengths get's shifted to the right and N50 gets **bigger** ... obviously?



