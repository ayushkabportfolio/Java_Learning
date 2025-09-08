*** Settings ***
Library    RequestsLibrary
Library    OperatingSystem

*** Variables ***
${base_url}    https://jsonplaceholder.typicode.com

*** Test Cases ***
post on session demo
    create session    my_session    ${base_url}
    # Create session is used to create a session object with the host which later can be used to hit many http requests.
    # In create session keyword, I need to provide alias,base_url,headers,cookies,auth which are common to every request that i will be making to this host.
    ${data}=    get file    data.json

    ${response}=    post on session    my_session    /posts    data=${data}
    log    ${response.json()}
    status should be    201

    # the create session keyword will be same as the get, post .. keywords, here session_name is extra & others thing will be the one which will be comma to all the requests
    # the uncommon thing should be provided in the respective '__ on session' keywords, for ex : end_point, data/json etc..
    delete all sessions