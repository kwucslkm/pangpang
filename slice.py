# jumin= "990120-1234567"
# print("생년월일 : " + jumin[:6])
# print("주민번호 뒷자리 : "+ jumin[-7:])

# print('저는 "나도코딩" 입니다.')
# ------------------------------------------------
# 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!" 로 구성
# 예) 생성된 비밀번호 : nav51!
url = "http://naver.com"

pw1 = url.replace("http://","")
pw2 = pw1[:pw1.index(".")]
password = pw2[:3] + str(len(pw2)) + str(pw2.count("e"))+"!"
print(password)
