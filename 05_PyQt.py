# 참고 자료: https://wikidocs.net/book/1664

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("test.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pushButton.clicked.connect(self.processInput)

    # 버튼이 눌리면 작동할 함수
    def processInput(self):
        inputText = self.lineEdit.text()
        keywords = ["트랜지스터", "메모리", "전력 소비", "효율"]
        foundKeywords = []  # 발견된 키워드를 저장할 리스트

        for keyword in keywords:
            if keyword in inputText:
                foundKeywords.append(keyword)

        if foundKeywords:  # 발견된 키워드가 있으면
            processedText = ", ".join(foundKeywords)  # 발견된 키워드를 쉼표로 구분하여 하나의 문자열로 합칩니다.
        else:
            processedText = "No keywords found"  # 발견된 키워드가 없으면

        self.lineEdit_2.setText(processedText)  # 결과를 lineEdit_2에 설정

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

