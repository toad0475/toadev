@ECHO OFF


@ECHO TargetPath: %1
@ECHO CurrentDir: %cd%
@ECHO BATDir: %~dp0

@REM Tab delimited 텍스트 파일 사용자 입력
FOR /F "tokens=*" %%a IN ('%~dp0OpenFileBox.exe "Tab delimited text (*.txt)|*.txt" "%cd%" "Choose Tab delimited text file(s)"') DO SET TEXTPATH=%%a

SET CLIPATH=%cd%\wwisecli.exe
@ECHO CLIPATH: %CLIPATH%
@ECHO TEXTPATH: %TEXTPATH%


@REM 배치파일이 있는 디렉토리로 경로 이동
CD /d %~dp0

@REM 검사를 수행 할 확장자를 설정
SET TARGET_FILEX=wproj

@REM 배치파일이 있는 위치로부터 몇 번째 상위레벨까지 탐색할지 설정
SET /A LOOPCOUNT=3

:LOOP
FOR /R %%f IN (*.%TARGET_FILEX%) DO (
    IF EXIST %%f (
        SET WWISEPROJPATH=%%f
        GOTO SHOWPATH 
    )
)

IF %LOOPCOUNT% == 0 (
    GOTO DOESNTEXIST
) ELSE (
    SET /A LOOPCOUNT-= 1
    CD ..
    GOTO LOOP
)

:SHOWPATH
@ECHO WWISEPROJPATH: %WWISEPROJPATH%
GOTO EXECUTEIMPORT

:DOESNTEXIST
@REM Wwise 프로젝트 파일이 없습니다.
@ECHO Wwise project file doesn't exist.
GOTO :P


:EXECUTEIMPORT
@REM Tab으로 구분된 텍스트 파일을 Wwise로 임포트
@ECHO -----------------------------------
@ECHO Import Text File Using WwiseCli.exe
@ECHO -----------------------------------
"%CLIPATH%" %WWISEPROJPATH% -TabDelimitedImport %TEXTPATH% -TabDelimitedOperation UseExisting -ContinueOnError -Save 

:P
::@pause
