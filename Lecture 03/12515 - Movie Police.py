import sys
import io

#Problem 4

txt = """3 1
000011
1101111111
1111100000
1000111"""

stdin = io.StringIO(txt)

#Actual use (Comment the below line for testing)
stdin = sys.stdin


def compare_sequences(clip, movie_sequence):
    h_distance = 0
    for i in range(len(clip)):
        if clip[i] != movie_sequence[i]:
            h_distance += 1
    return h_distance

def find_max_similarity(movies, clips):
    similar_movies = [] #Index of movie most similar for each clip
    for clip in clips:
        hamming_distances = []  #Hamming distances for each clip with each movie
        for movie in movies:
            if len(movie) < len(clip):
                # It is not specified what happens in this case. Through my testing in the udebg website, it seems it doesn't
                # look in these cases, so I'll just add a case that will never be the minimum distance
                hamming_distances.append(100000000000)
            else:
                min_hamming_distance = 100000000000000
                difference = len(movie) - len(clip) #Will be helpful to see the sequences inside a movie
                for case in range(difference + 1):
                    tmp = compare_sequences(clip, movie[case:(case + len(clip))])
                    if tmp < min_hamming_distance:
                        min_hamming_distance = tmp

                # Adds to the list the maximum distance a clip has with a movie.
                # That way, the max distance with each movie will be in order.
                # [max distance with movie 1, max distance with movie 2, ...]
                hamming_distances.append(min_hamming_distance)

        # For each clip, the movie with max distance is added to this list.
        # For how index() works, in case of more than one movie with the same 
        # distance, will append the one with the lower index. 
        similar_movies.append(hamming_distances.index(min(hamming_distances)))
    
    for movie in similar_movies:
        print(movie + 1)

def P4():
    for i, line in enumerate(stdin.readlines()):
        if line[-1] == '\n':
            line = line[0:-1]
        if not i:
            M, Q = map(int, line.split())
            movies = []
            clips = []
        else:
            if i <= M:
                movies.append(line)

            elif i == M + Q:
                 clips.append(line)
                 find_max_similarity(movies, clips)

            #When M < i < M + Q
            else:
                clips.append(line)


P4()