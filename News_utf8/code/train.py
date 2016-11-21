from gensim.models import word2vec 
import logging 
def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus('../all_text.txt')
    model = word2vec.Word2Vec(sentences, size=250)
    model.save_word2vec_format('med.model.bin',binary=True)

if __name__ == "__main__":
    main()
