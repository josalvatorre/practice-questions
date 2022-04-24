from collections import defaultdict
from typing import Dict, List


def tournament_winner(
    competitions: List[List[str]], results: List[int]
) -> str:

    team_scores: Dict[str, int] = defaultdict(lambda: 0)

    for i in range(len(competitions)):
        card = competitions[i]
        winner = card[results[i] ^ 1]
        team_scores[winner] += 3
        pass

    return max(team_scores.items(), key=lambda item: item[1])[0]
