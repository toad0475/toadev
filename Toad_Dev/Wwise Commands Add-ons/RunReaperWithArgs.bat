@echo off
set list=%*

(for %%a in (%list%) do (
    echo %%~a
)) > filelist.txt

type Config.txt >> filelist.txt

"C:\\Program Files\\REAPER (x64)\\reaper.exe" -batchconvert filelist.txt
