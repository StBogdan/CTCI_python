from typing import List, Tuple
from collections import defaultdict


def sparse_similarity(docs_raw: List[Tuple[int, List[int]]]) -> None:
    doc_dict = dict(docs_raw)
    rev_index = defaultdict(set)

    for doc_id, doc_words in doc_dict.items():
        for word in doc_words:
            rev_index[word].add(doc_id)

    intersect_of_pairs = defaultdict(int)

    for doc_id, doc_words in doc_dict.items():
        for word in doc_words:
            for other_doc in rev_index[word]:
                # We assume an ordering of the doc ids,
                # as to prevent duplicate counting
                if other_doc <= doc_id:
                    continue

                intersect_of_pairs[(doc_id, other_doc)] += 1

    print(f"ID1, ID2:\tSIMILARITY")
    for (doc1, doc2), in_common in intersect_of_pairs.items():
        union_size = len(doc_dict[doc1]) + len(doc_dict[doc2]) - in_common
        docs_simil = in_common / union_size

        print(f"{doc1:3}, {doc2:3}:\t{docs_simil}")


if __name__ == "__main__":
    ex = [
        (13, [14, 15, 100, 9, 3]),
        (16, [32, 1, 9, 3, 5]),
        (19, [15, 29, 2, 6, 8, 7]),
        (24, [7, 10])
    ]

    sparse_similarity(ex)
