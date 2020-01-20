*** Settings ***
Library  RoboNmap
Library  Collections

*** Variables ***
${TARGET}  

*** Test Cases ***
Run Basic Port Scan
    nmap script scan  ${TARGET}  version_intense=3  file_export=nmap.txt
    nmap print results

Run Vulnerabilities scan
    nmap script scan  ${TARGET}  version_intense=3  file_export=nmap.txt  script_name=vuln  portlist=80
    nmap print results