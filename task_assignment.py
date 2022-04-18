from typing import List


def task_assignment(k: int, tasks: List[int]) -> List[int]:

    sorted_task_indices = sorted(
        range(len(tasks)),
        key=tasks.__getitem__,
    )

    task_1_index = iter(sorted_task_indices)
    task_2_index = iter(reversed(sorted_task_indices))

    return [
        [
            next(task_1_index),
            next(task_2_index),
        ]
        for _ in range(k)
    ]
