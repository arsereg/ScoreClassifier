
import random

from models.Score import Score


class ScoreFactory:

    def __createScore(self, value):
        return Score(value)


    def __createRandomScore(self):
        return self.__createScore(random.randint(0, 60))


    def createScores(self, n: int):
        scores = []
        for i in range(n):
            scores.append(self.__createRandomScore())
        return scores

