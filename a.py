import MeCab

text = '私は木下です'
tagger = MeCab.Tagger("-Ochasen")
result = tagger.parse(text)
print(result, "\n")
