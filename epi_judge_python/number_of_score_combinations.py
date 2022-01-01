from typing import List

from test_framework import generic_test
import copy

# 2,3,7: 9

def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # TODO - you fill in here.
    scores = copy.copy(individual_play_scores)
    scores = [score for score in scores if score <= final_score]
    if final_score == 0:
        return 1
    if not scores:
        return 0
    scores.sort()
    matrix = [[0] * (final_score+1) for i in range(len(scores))]
    imax = len(scores) - 1
    for i in range(len(scores)):
        matrix[i][0] = 1
    jmax = final_score
    for j in range(0, final_score + 1, scores[0]):
        matrix[0][j] = 1
    for i in range(1, len(scores)):
        for j in range(scores[i]):
            matrix[i][j] = matrix[i-1][j]
        for j in range(scores[i], final_score + 1):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-scores[i]]
    return matrix[imax][jmax]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
