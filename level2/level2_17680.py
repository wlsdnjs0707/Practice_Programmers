def solution(cacheSize, cities):
    answer = 0

    # LRU (Least Recently Used) 알고리즘
    # 호출시 head로 순서 변경
    # 새로운 값이 추가되어 cache size 벗어나면 tail 삭제

    cache = []

    for i in cities:
        if i.lower() in cache:
            # cache hit
            answer += 1
            # 원래 자리에서
            cache.remove(i.lower())
            # 헤드로 이동
            cache.insert(0, i.lower())
        else:
            # cache miss
            answer += 5
            # 캐시가 다 차지 않았으면 (+cache size가 0이 아닐때)
            if len(cache) < cacheSize and cacheSize != 0:
                # 캐시에 추가
                cache.insert(0, i.lower())
            # 캐시가 다 찼으면
            else:
                # 가장 오래된 tail 값 삭제
                if len(cache) > 0:
                    cache.pop(cacheSize - 1)
                # 새로운 값 추가 (+cache size가 0이 아닐때)
                if cacheSize != 0:
                    cache.insert(0, i.lower())

    return answer