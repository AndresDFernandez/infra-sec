*** Settings ***
Library  RoboNmap
Library  Collections

*** Variables ***
${TARGET}  172.16.0.1

*** Test Cases ***
Run Basic Port Scan
    nmap script scan  ${TARGET}  version_intense=3  file_export=nmap.txt
    nmap print results