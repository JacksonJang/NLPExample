from konlpy.tag import Hannanum, Kkma, Komoran, Okt
from collections import Counter
morphs_processors= [('Hannanum', Hannanum()), ('Kkma', Kkma()), ('Komoran', Komoran()), ('Okt', Okt())]

string = """
사우디아라비아를 방문 중인 문재인 대통령은 19일(현지시간) 수도 리야드에서 나예프 알 하즈라프 걸프협력회의(GCC) 사무총장을 접견하고 협력 강화 방안 및 FTA 협상 재개 등에 대해 의견을 교환했다고 박경미 청와대 대변인이 서면 브리핑을 통해 전했다.

접견에서 문 대통령은 “한국이 전체 원유수입량의 61%를 GCC 회원국으로부터 공급받고 있으며, GCC의 주요 인프라 건설에는 한국의 우수한 건설기업들이 참여하고 있다”면서 “한국과 GCC 각국은 상호 보완적인 경제구조를 갖고 호혜적 동반자 관계를 통해 경제 발전과 공동 번영을 이뤄왔다”고 평가했다.

이에 나예프 GCC 사무총장은 “대통령이 찾아주신 사우디는 지금 아주 아름다운 날씨인데, 이는 양국 간 협력을 잘 보여주는 배경이라고 생각한다”면서 “양측은 2014년에 체결된 ‘한-GCC 전략·협력 양해각서’(MOU)와  2020년의 공동행동계획을 기반으로 경제, 문화, 과학, 보건 등 다양한 분야에서 협력을 강화해 나갈 것”이라고 말했다.
"""

for name, morphs_processor in morphs_processors:
    count = Counter(morphs_processor.nouns(string))
    print(name)
    array = count.most_common(100)
    print(array)
    if name == "Komoran":
        for item in array:
            print(item[0])
