*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${base_url}    https://jsonplaceholder.typicode.com

*** Test Cases ***
get request demo
    ${query_params}=    create dictionary    page=2    id=10
    ${response}=     GET   ${base_url}    ${query_params}

    # validation
    should be equal as numbers    ${response.status_code}    201

    should be equal as strings    ${response.json()}[data][first_name]    SAMARTH

    should be equal as strings    ${response.headers}[Content-Type]    application-json

    should be equal as strings    ${response.cookies}

post request demo
    ${json_data}=    create dictionary    a=b    c=d    e=f
    ${response}=    POST    ${base_url}/posts    json=${json_data}

    # validation
    should be equal as strings    ${response.status_code}    201


    ${id}=    set variable    ${response.json()}[id]
    set global variable     ${id}
    should not be empty    ${id}

put request demo
    ${json_data}=    create dictionary    a=b    c=t    e=f
    ${response}=    PUT    ${base_url}/posts/${id}    json=${json_data}

    should be equal as numbers    ${response.status_code}    201

    should be equal as strings    ${response.json()}[c]    t


delete request demo
    ${response}=    DELETE    ${base_url}/path/id
    should be equal as numbers    ${response.status_code}    204


post
    ${json_data}=    load json from file    path/.josn
    I can make some cahnges in the json_data, then

    ${response}=    POST    url    json=${json_data}
    status should be    200     ${response}


