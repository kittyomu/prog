from PrepareChain import PrepareChain

text = u"適当な長い文章。長い文章。"
chain = PrepareChain(text)
triplet_freqs = chain.make_triplet_freqs()
chain.save(triplet_freqs, True)
