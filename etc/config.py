# this file will be interpreted as python3

urlprefix = '/'

# Minor allele frequency (MAF) filters:
# Note:
#    "Association" means an association between a variant and a phenotype.
#    Every association has a p-value.  It may also have other attributes.
#    MAF-filters will apply to allele frequency (AF) and allele count (AC) (if PheWeb knows num_samples for the phenotype)
# First, PheWeb drops any association with a MAF < assoc_min_maf.
# Next, PheWeb drops any variant where every association has MAF < variant_inclusion_maf.
# In a dataset where all associations to a given variant all have the same MAF, the two filters do the same thing.
#     - in that case, use `assoc_min_maf` to save disk space and parse time.
# If variant_inclusion_maf <= assoc_min_maf, it won't have any effect.
# Using assoc_min_maf will save disk space, even if you're already using variant_inclusion_maf.
assoc_min_maf = 0.005
# variant_inclusion_maf = 0.01
variant_inclusion_maf = 0.005

within_pheno_mask_around_peak = 100000
between_pheno_mask_around_peak = 100000
manhattan_num_unbinned = 2000
manhattan_peak_max_count = 2000
manhattan_peak_pval_threshold = 1000000
manhattan_peak_sprawl_dist = 200000
top_hits_pval_cutoff = 100000

# num_procs = 1 # for debugging convenience.

# directory for caching large (~1GB) common files like dbsnp
#cache = '/home/ubuntu/pheweb/cache'
cache = '~/pheweb/cache'

# genome assembly, only '19' or '38' are supported
build = '38'