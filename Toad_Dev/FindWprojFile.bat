@ECHO OFF

@ECHO TargetPath: %1
@ECHO CurrentDir: %cd%
@ECHO BATDir: %~dp0

SET CLIPATH=%cd%\wwisecli.exe
@ECHO CLIPATH: %CLIPATH%
@ECHO TEXTPATH: %TEXTPATH%


@REM 배치파일이 있는 디렉토리로 경로 이동
CHDIR /d %~dp0

@REM 검사를 수행 할 확장자를 설정
SET TARGET_FILEX=wproj

@REM 배치파일이 있는 위치로부터 몇 번째 상위레벨까지 탐색할지 설정
SET /A LOOPCOUNT=4

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
    CHDIR ..
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
@ECHO ------------------------------------------
@ECHO Create Audio Bus Diagram Using wproj File!
@ECHO ------------------------------------------

@REM 이곳에 명령줄을 입력한다.

:P
@pause
