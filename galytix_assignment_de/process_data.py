import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
import functools

#Custom error handlinf decorator as specified in Bonus points.
def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            exit(1)
        except KeyError as e:
            print(f"Error: {e}")
            exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            exit(1)
    return wrapper


# Usin OOPS concepts, Data Processing is performed.
class SimilarityCalculator:
    def __init__(self, word_embeddings_file, phrases):
        self.word_embeddings = KeyedVectors.load_word2vec_format(word_embeddings_file, binary=True, encoding='latin1')
        self.phrases = phrases

    def calculate_similarity(self, phrase1, phrase2):
        vec1 = self.get_phrase_vector(phrase1)
        vec2 = self.get_phrase_vector(phrase2)

        # Check to avoid Zero Division Error
        norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
        if norm_product == 0:
            return np.inf  

        # Calculating Cosine distance
        distance = 1 - np.dot(vec1, vec2) / norm_product
        return distance

    def get_phrase_vector(self, phrase):
        words = phrase.split()
        word_vectors = [self.word_embeddings[word] for word in words if word in self.word_embeddings]

        if not word_vectors:
            return np.zeros(self.word_embeddings.vector_size)

        #Check to avoid Zero Division Error.
        total_vector = np.sum(word_vectors, axis=0)
        norm_total_vector = np.linalg.norm(total_vector)
        if norm_total_vector == 0:
            return total_vector

        return total_vector / norm_total_vector

    def batch_execution(self):
        num_phrases = len(self.phrases)
        similarity_matrix = np.zeros((num_phrases, num_phrases))

        for i in range(num_phrases):
            for j in range(i + 1, num_phrases):
                similarity_matrix[i, j] = self.calculate_similarity(self.phrases[i], self.phrases[j])
                similarity_matrix[j, i] = similarity_matrix[i, j]

        return similarity_matrix

    def on_the_fly_execution(self, user_input):
        closest_match = None
        min_distance = float('inf')

        for phrase in self.phrases:
            distance = self.calculate_similarity(user_input, phrase)
            if distance < min_distance:
                min_distance = distance
                closest_match = phrase

        return closest_match, min_distance

    
def load_phrases(file_path, column_name='Phrases', encoding='utf-8'):
    try:
        phrases_df = pd.read_csv(file_path, encoding=encoding)
        if column_name not in phrases_df.columns:
            raise KeyError(f"Column '{column_name}' not found in the CSV file.")
        return phrases_df[column_name].tolist()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File '{file_path}' not found.") from e

if __name__ == "__main__":
    # Loading phrases from CSV
    file_path = 'phrases.csv'
    phrases_column_name = 'Phrases'
    phrases = load_phrases(file_path, column_name=phrases_column_name, encoding='latin1')

    similarity_calculator = SimilarityCalculator('vectors.bin', phrases)


    # Batch execution
    results_batch = similarity_calculator.batch_execution()
    # On-the-fly execution example
    user_input = "Main channels in India"
    #Giving output as-
    #Closest match: Which are the main distribution channels in India?, Distance: 0.39894187450408936
    closest_match, distance = similarity_calculator.on_the_fly_execution(user_input)
    print(f"Closest match: {closest_match}, Distance: {distance}")
