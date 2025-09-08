How to pass json data from file
===================================
- import operating system library.
- create a .json file with the json inside it.
- use 'get file' keyword to featch the data from file
- pass the fetched data to 'data'/json parameter of the requests keywords.

Note:
- both the data & json parameters are used to pass data.
- both accept dict and can serlize the data
- 'data' paramter is used to pass raw json data, usually from file.(.json file is preffered, so that the data in it is JSON data), but it even accept the dict & can serliaze it.
- 'json' parameter is used to pass the python dic, which will be serialized to json & sent as a request.

*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary


*** Variables ***
${base_url}    https://jsonplaceholder.typicode.com

*** Test Cases ***
post with json data from file
     ${json_data}=    Load Json From File   path/data.json
    # path should be relative to project, as for Resourse in settings
    log    ${json_data}
    ${response}=    POST     ${base_url}/posts    json=${json_data}
    log    ${response}