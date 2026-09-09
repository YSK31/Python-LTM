import numpy as np

class ExamScoreAnalyzer:
    def create_score_array(self, scores: list) -> np.ndarray:
        return np.array(scores, dtype=int)

    def validate_score_range(self, arr: np.ndarray) -> bool:
        return arr.size > 0 and np.all((arr >= 0) & (arr <= 100))

    def score_percentiles(self, arr: np.ndarray) -> tuple:
        return (
            round(float(np.percentile(arr, 25)), 2),
            round(float(np.percentile(arr, 50)), 2),
            round(float(np.percentile(arr, 75)), 2),
        )

    def apply_grace_marks(self, arr: np.ndarray, grace: int) -> np.ndarray:
        return np.minimum(arr + grace, 100).astype(int)

    def top_score_indices(self, arr: np.ndarray, n: int) -> np.ndarray:
        indices = np.arange(arr.size)
        order = np.lexsort((indices, -arr))
        return order[:n]

    def count_passing_scores(self, arr: np.ndarray, pass_mark: int) -> int:
        return int(np.sum(arr >= pass_mark))


if __name__ == "__main__":
    analyzer = ExamScoreAnalyzer()

    scores = analyzer.create_score_array([42, 78, 91, 65, 91, 55])
    print("Score array:", scores)
    print("Valid:", analyzer.validate_score_range(scores))
    print("Percentiles:", analyzer.score_percentiles(scores))
    print("After grace marks:", analyzer.apply_grace_marks(scores, 7))
    print("Top 4 indices:", analyzer.top_score_indices(scores, 4))
    print("Passing count:", analyzer.count_passing_scores(scores, 60))

    print("Empty valid:", analyzer.validate_score_range(np.array([], dtype=int)))
    print("All indices when n is large:", analyzer.top_score_indices(np.array([70, 70, 60]), 10))
