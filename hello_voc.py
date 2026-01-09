def analyze_customer_feedback(feedback_text: str) -> dict:
    """
    고객 피드백 텍스트를 분석하여 감정(sentiment)과 점수(score)를 반환합니다.
    
    Args:
        feedback_text (str): 분석할 고객 피드백 텍스트
    
    Returns:
        dict: 다음 키를 포함하는 딕셔너리
            - sentiment (str): '긍정', '중립', 또는 '부정'
            - score (float): 0~1 사이의 점수
    
    규칙:
        - '좋다', '만족', '추천' 포함 → 긍정
        - '싫다', '불만', '최악' 포함 → 부정
        - 그 외 → 중립
    """
    pass


# 테스트 코드
if __name__ == "__main__":
    # 테스트 케이스 1: 긍정
    test1 = "이 제품 정말 좋아요! 추천합니다."
    result1 = analyze_customer_feedback(test1)
    print(f"테스트 1: {test1}")
    print(f"결과: {result1}")
    print(f"예상: sentiment='긍정'")
    print()
    
    # 테스트 케이스 2: 부정
    test2 = "최악의 배송 경험입니다."
    result2 = analyze_customer_feedback(test2)
    print(f"테스트 2: {test2}")
    print(f"결과: {result2}")
    print(f"예상: sentiment='부정'")
    print()
    
    # 테스트 케이스 3: 중립
    test3 = "그냥 그래요."
    result3 = analyze_customer_feedback(test3)
    print(f"테스트 3: {test3}")
    print(f"결과: {result3}")
    print(f"예상: sentiment='중립'")
    print()
