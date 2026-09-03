#조건문: if문, match문

age = 17
if age >= 20:
    print("성인입니다")
else:
    print("미성년자입니다")

    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    #match문
    grade = "A"

    match grade:
        case "A":
            print("우수")
        case "B":
            print("잘함")
        case "C":
            print("보통")
        case _:     #default
            print("알수없음")
            