def solution(genres, plays):
    answer = []
    total_map = {}  # 각 장르별 총 재생 횟수를 담은 {}
    genre_map = {}  # 각 장르의 고유번호에 따른 재생 횟수를 담은 {}
    
    # 각 장르와 노래 정보를 딕셔너리에 저장
    for i in range(len(genres)):
        genre = genres[i]
#       해당 장르가 이미 해시 안에 키로 존재한다면 삽입
        if genre in genre_map:
            genre_map[genre].append((i, plays[i]))
            total_map[genre] += plays[i]
#       해당 장르가 해시 안에 키로 존재하지 않는다면 할당
        else:
            genre_map[genre] = [(i, plays[i])]
            total_map[genre] = plays[i]

    # 장르를 재생 횟수 순으로 정렬
    sorted_genres = sorted(total_map.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in sorted_genres:
        # 각 장르 내에서 노래를 재생 횟수 순으로 정렬
        genre_map[genre] = sorted(genre_map[genre], key=lambda x: (-x[1], x[0]))
        
        # 각 장르에서 최대 2곡 선택
        for i in range(min(len(genre_map[genre]), 2)):
            answer.append(genre_map[genre][i][0])

    return answer