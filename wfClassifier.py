import os
import wave
import shutil
from tkinter import filedialog

# 웨이브 파일(stereo, mono) 분류기 
def waveClassifier():
    srcDir = filedialog.askdirectory(title='원본 폴더 선택...')
    stereoTargetDir = filedialog.askdirectory(title='스테레오 폴더 선택...')
    monoTargetDir = filedialog.askdirectory(title='모노 폴더 선택...')
    files = []

    # src 파일 경로 리스트 만들기
    for r, d, f in os.walk(srcDir):
        #r=root, d=directories, f=files
        files += [os.path.join(r,file) for file in f if '.wav' in file]
    
    # stereo, mono 각각의  폴더로 분류 작업
    for wavefile in files:
        wf = wave.Wave_read(wavefile)
        subPath = getSubPath(srcDir, wavefile)
        if wf.getnchannels()==2:
            if not os.path.isdir(os.path.dirname(stereoTargetDir+subPath)):
                os.makedirs(os.path.dirname(stereoTargetDir+subPath))
            shutil.copy(wavefile, stereoTargetDir+subPath)
        elif wf.getnchannels()==1:
            if not os.path.isdir(os.path.dirname(monoTargetDir+subPath)):
                os.makedirs(os.path.dirname(monoTargetDir+subPath))
            shutil.copy(wavefile, monoTargetDir+subPath)
        wf.close()

# 소스 경로와 목적 경로에서 겹치치 않는 하위 경로만 가져오기
def getSubPath(src, target):
    paths = [src, target]
    return paths[1][len(os.path.commonpath(paths)):]

# 메인
if __name__=="__main__":
    waveClassifier()
