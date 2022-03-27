import itertools
from typing import Iterable, Optional


def get_lowest_common_manager(top_manager, report_1, report_2):
    def path(tree, node) -> Optional[Iterable]:
        if tree is node:
            return (tree,)  # tuple of one
        elif len(tree.directReports) == 0:
            return None
        else:
            subpath_to_node = next(
                (
                    p
                    for report in tree.directReports
                    if (p := path(report, node)) is not None
                ),
                None,
            )
            return (
                None
                if subpath_to_node is None
                else itertools.chain((tree,), subpath_to_node)
            )

    shorter_path, longer_path = sorted(
        (tuple(path(top_manager, report)) for report in (report_1, report_2)),
        key=len,
    )

    shorter_path_last = len(shorter_path) - 1

    if shorter_path[shorter_path_last] == longer_path[shorter_path_last]:
        fork_index = shorter_path_last
    else:
        fork_index = next(
            (
                i - 1
                for i in range(1, len(shorter_path))
                if longer_path[i] != shorter_path[i]
            ),
            0,
        )
    return shorter_path[fork_index]


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
