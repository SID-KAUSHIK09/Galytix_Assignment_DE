import gensim
from gensim.models import KeyedVectors

location = "GoogleNews-vectors-negative300.bin"
wv = KeyedVectors.load_word2vec_format(location, binary=True, limit=1000000)
wv.save_word2vec_format('vectors.bin', binary=True)
##Pretrained vectors of WordtoVec downloaded from, https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM
##First 1000000 vectors loaded in vectors.bin. 