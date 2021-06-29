*** Settings ***
Library    ${EXECDIR}/Libraries/GB32960.py
Library    ${EXECDIR}/Libraries/TcpClient.py
Variables  ${EXECDIR}/TestData/test_data.yaml



*** Test Cases ***
GB32960 Vehicle Login Test Case
    TCP Client connect to Server   ${HOST}   ${PORT}
    GB32960 Codec Init   ${VIN}
    ${login_fields}   Encode GB32960 Vehicle Login   ${ICCID}
    Set Test Variable   ${login_fields}
    TCP Client Send data to Server   ${login_fields}
    
