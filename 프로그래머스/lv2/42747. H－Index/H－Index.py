def solution(citations):
    sort_citations = sorted(citations)

    for i in range(len(citations)):
        if sort_citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0
