import os
import wave
import shutil
from pathlib import Path
import logging as log

from PySide2.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
QLabel, QLineEdit, QPushButton, QComboBox, QCheckBox, QMessageBox, 
QApplication, QGridLayout, QFormLayout,QGroupBox,QDialogButtonBox,QFileDialog,QPlainTextEdit)

from PySide2.QtGui import QIcon

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        
        # 기본 설정
        self.initSettings()

        # 툴 설명 박스 생성
        self.createDescription()

        # 사용자 입력 그룹 생성
        self.createUserInputBox()

        # 로그 메세지 박스 생성
        self.createMessageBox()

        # 하단 수행 버튼 생성
        self.createExcuteBtn()

        # 메인 레이아웃 생성 및 위젯 연결
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.descriptionBox)
        mainLayout.addWidget(self.userInputBox)
        mainLayout.addWidget(self.messageBox)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)
    

    def initSettings(self):
        self.setWindowTitle("Wavefile Classifier")
        self.setWindowIcon(QIcon('E:\\ToadProject\\toadev\\Toad_Dev\WavefileClassifier\\Classifier.png')) # app 아이콘 지정
        self.setMinimumSize(700, 500)

    def createDescription(self):
        self.descriptionBox = QGroupBox("Wave 파일 분류기")
        descriptionBoxLayout = QVBoxLayout()

        desc = QLabel()
        desc.setText('아래 항목에 경로를 입력하시고 Apply 버튼을 클릭하시면 Wave 파일을 자동으로 분류합니다.')
        descriptionBoxLayout.addWidget(desc)
        self.descriptionBox.setLayout(descriptionBoxLayout)
        

    def createUserInputBox(self):
        self.userInputBox = QGroupBox("User Input")
        inputBoxlayout = QFormLayout()

        subLayout1 = QHBoxLayout()
        originBrowseBtn = QPushButton("Browse...")
        self.originDir = QLineEdit("Original 폴더 경로를 입력하세요.")
        originBrowseBtn.clicked.connect(lambda: self.openFileNameDialog('Original 폴더 경로를 입력하세요.',self.originDir))
        subLayout1.addWidget(self.originDir)
        subLayout1.addWidget(originBrowseBtn)

        subLayout2 = QHBoxLayout()
        selectButton2 = QPushButton("Browse...")
        self.monoDir = QLineEdit("Mono 폴더 경로를 입력하세요.")
        selectButton2.clicked.connect(lambda: self.openFileNameDialog('Mono 폴더 경로를 입력하세요.',self.monoDir))
        subLayout2.addWidget(self.monoDir)
        subLayout2.addWidget(selectButton2)

        subLayout3 = QHBoxLayout()
        selectButton3 = QPushButton("Browse...")
        self.stereoDir = QLineEdit("Stereo 폴더 경로를 입력하세요.")
        selectButton3.clicked.connect(lambda: self.openFileNameDialog('Stereo 폴더 경로를 입력하세요.',self.stereoDir))
        subLayout3.addWidget(self.stereoDir)
        subLayout3.addWidget(selectButton3)

        inputBoxlayout.addRow(QLabel('Original Root Folder: '), subLayout1)
        inputBoxlayout.addRow(QLabel('Mono Folder: '), subLayout2)
        inputBoxlayout.addRow(QLabel('Stereo Folder: '), subLayout3)
        self.userInputBox.setLayout(inputBoxlayout)

    def createMessageBox(self):
        self.messageBox = QGroupBox("Log Message")
        messageBoxlayout = QHBoxLayout()
        self.textBox = QPlainTextEdit()
        self.textBox.setReadOnly(True)
        messageBoxlayout.addWidget(self.textBox)
        self.messageBox.setLayout(messageBoxlayout)
    
    def createExcuteBtn(self):
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton("Apply", QDialogButtonBox.AcceptRole)
        self.buttonBox.accepted.connect(self.waveClassifier) # Apply 버튼 클릭 시 이벤트 연결
    
    def openFileNameDialog(self, dialogTitle,dirPath):
        selectedDir = QFileDialog.getExistingDirectory(self, dialogTitle) 
        if selectedDir:
            return self.setFolderdDir(selectedDir,dirPath)

    def setFolderdDir(self,dir,dirPath):
        dirPath.setText(dir)

    def checkValidPath(self, *args):
        for p in args:
            if not os.path.exists(p):
                self.textBox.insertPlainText("[{}] 디렉토리가 유효하지 않습니다. \n".format(p))
                print("[{}] 디렉토리가 유효하지 않습니다.".format(p))
                return False
        return True
            
    # 웨이브 파일(stereo, mono) 분류기 
    def waveClassifier(self):
        
        in_originDir = self.originDir.text()
        in_monoDir = self.monoDir.text()
        in_stereoTDir = self.stereoDir.text()

        monoCount,stereoCount,totCount = 0,0,0

        if self.checkValidPath(in_originDir,in_monoDir,in_stereoTDir):
            files = list()
            OrifolderName = self.getSubPath(Path(in_originDir).parents[0],in_originDir)

            # src 파일 경로 리스트 만들기
            for r, d, f in os.walk(in_originDir):
                #r=root, d=directories, f=files
                files += [os.path.join(r,file) for file in f if file.endswith('.wav')]
            
            # stereo, mono 각각의  폴더로 분류 작업
            self.textBox.insertPlainText('wav 파일 분류작업을 시작합니다.\n')
            print('wav 파일 분류작업을 시작합니다.')
            for wavefile in files:
                subPath = self.getSubPath(in_originDir, wavefile)
                with wave.open(wavefile,'r') as wf:
                    totCount += 1
                    try:
                        if wf.getnchannels() == 2:
                            if not os.path.isdir(os.path.dirname(in_stereoTDir + OrifolderName + subPath)):
                                os.makedirs(os.path.dirname(in_stereoTDir + OrifolderName + subPath))
                            shutil.copy(wavefile, in_stereoTDir + OrifolderName + subPath)
                            self.textBox.insertPlainText('INFO: {} 파일이 {} 로 복사되었습니다.\n'.format(wavefile,in_stereoTDir + OrifolderName + subPath))
                            print('INFO: {} 파일이 {} 로 복사되었습니다.'.format(wavefile,in_stereoTDir + OrifolderName + subPath))
                            stereoCount += 1
                        elif wf.getnchannels() == 1:
                            if not os.path.isdir(os.path.dirname(in_monoDir + OrifolderName + subPath)):
                                os.makedirs(os.path.dirname(in_monoDir + OrifolderName + subPath))
                            shutil.copy(wavefile, in_monoDir + OrifolderName + subPath)
                            self.textBox.insertPlainText('INFO: {} 파일이 {} 로 복사되었습니다.\n'.format(wavefile,in_monoDir + OrifolderName + subPath))
                            print('INFO: {} 파일이 {} 로 복사되었습니다.'.format(wavefile,in_monoDir + OrifolderName + subPath))
                            monoCount += 1
                    except:
                        self.textBox.insertPlainText('WARNING: {} 파일이 경로에 이미 존재하여 복사하지 못했습니다.\n'.format(wavefile))
                        print('WARNING: {} 파일이 경로에 이미 존재하여 복사하지 못했습니다.'.format(wavefile))

            self.textBox.insertPlainText("총 {}개의 Wave 파일 중, Mono 파일 {}개, Stereo 파일 {}개가 분류되었습니다.\n".format(totCount, monoCount, stereoCount))
            print("총 {}개의 Wave 파일 중, Mono 파일 {}개, Stereo 파일 {}개가 분류되었습니다.".format(totCount, monoCount, stereoCount))
            self.textBox.insertPlainText("분류 작업을 완료 했습니다!\n")
            print("분류 작업을 완료 했습니다!")

    # 소스 경로와 목적 경로에서 겹치치 않는 하위 경로만 가져오기
    def getSubPath(self, src, target):
        paths = [src, target]
        return paths[1][len(os.path.commonpath(paths)):]

# 메인
if __name__=='__main__':
    # 기본 앱 생성
    app = QApplication([])
    
    wcApp = Form()
    wcApp.show()
    app.exec_()


