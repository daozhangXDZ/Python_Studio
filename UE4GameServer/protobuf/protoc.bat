@echo off
set protosrc_path = proto
set Path=protoc.exe

for /f "delims=" %%i in ('dir /b proto "%protosrc_path%/*.proto"') do %Path% ./proto/%%i  --python_out=python_out

pause