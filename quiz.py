import random
import csv
try:
    with open('quiz.csv', 'r', encoding='utf-8-sig') as f:
        data = csv.reader(f)
        word = {}
        for row in data:
            if row:
                clean_meanings = [w for w in row[1:] if w != '']
                word[row[0]] = clean_meanings
except FileNotFoundError:
    print("오류: 'quiz.csv' 파일을 찾을 수 없습니다. 같은 폴더에 파일을 만들어주세요.")
    exit() # 프로그램 종료


quiz_list = list(word.keys())
random.shuffle(quiz_list)
score = 0
wrongword = []

print(f"총{len(quiz_list)}문제가 로드되었습니다.")
print("")
while True:
    if len(quiz_list) == 0:
        print("모든 문제를 다 풀었습니다!")
        print(f"최종 점수는 {score}점 입니다.")
        print(f"틀린 문제 리스트입니다: {wrongword}")
        break

    quiz = quiz_list.pop()  #단어 선택 후 리스트에서 단어 제거
    
    
    print(f"단어의 뜻은?: {quiz}")
    answer = input("뜻 입력 (종료는 'N') : ").strip()
    print("")

    if answer == 'N' or answer == 'n':
        print(f"최종 점수는 {score}점 입니다.")
        break

    user_inputs = answer.replace(" ", "").split(",")

    if any(i in word[quiz] for i in user_inputs):
        print("정답입니다!")
        print("")
        score += 1
    else:
        print(f"틀렸습니다. 정답은 {', '.join(word[quiz])} 입니다.")
        wrongword.append(quiz)
        print("")
        
