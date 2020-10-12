OOP 에서 

class , instance

class on Disk ( static - resource )
instance on Memory ( dynamic - resource )
생성자 (constructor) 외에는 instance 를 만들 수 없다.

생성자는 클래스명 (대문자로 시작하는) 에 parameter - zone 이라 불리는 () 구조

instance = Constructor(param)


notation : 표기법 a = '1' (str)  a = 1 (int)  a = 1.0 (float)
annotaion : 주석 


JavaScript, C-Java, @static
constant => const, static, 
variable => let, int~ , 

data -> constant + variable  => state


variable 은 change 요소를 가지고 있는 정의 -> True
constant 는 change 요소를 가지고 있지 않은 정의 -> False 

state 를 종류에 따라 (추상화) : 4가지로 분류, 
CRUD(crete data, read data, update data, delete data)

REST(Representational State Transfer)
4가지 조건
1) CS 구조 
2) stateless:  
    client context - true
    server context - false
3) URI의 사용하여 data를 JSON 형식 전송
4) 중간 서버 예) WAS(tomcat)


SQL :  Language


sba-api
sba-ui


TaePD 님의 답변

cs구조인건 잘 모르겠구요. 
상태저장을 안하고 
uri를 사용하고 
flask로 중간서버를 사용해서 

-> rest입니다

FeedBack

cs구조 -> 서버: sba-api, 클라이언트: sba-ui   (T)
상태저장을 안하고 -> 쿠키나 세션에 저장을 안했습니다   (T)
uri + JSON, string -> uri (T) + JSON ()
중간서버 사용해서 -> (T)

-> rest입니다

URL = URI/search=hyper

controller 에 REST 설정한 부분까지가 2주차 MVC 의 종료입니다.

3주차 Model 로 학습전환 합니다.

Model 에서 AI 에 대한 알고리즘 학습을 주로 합니다.

