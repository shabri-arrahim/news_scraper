API End-Point
-------------

This API requires authenticating to LinkedIn in order to run any processes you want.

An endpoint for performing authentication is provided (endpoint with authentication category).

All you have to do is, first check whether your account requires a verification pin email to log in with the endpoint provided (the route will be: "/ auth / check_verification"),
if the response you get is "True", When you access the route "/ auth" (to login) you have to send a verification pin email via the provided endpoints (the route will be: "/ auth / verification").

================  ==============================================================  ===========================================  =================  ===============  ===============  =============
Category          Description                                                     Endpoint                                     Parameters         Data             Headers          Method
================  ==============================================================  ===========================================  =================  ===============  ===============  =============
Authentication    To check if the account need a verification PIN or not          /auth/check_verification                     None               username         None             POST
                                                                                                                                                  password         
Authentication    Make authentication to LinkedIn Service (Login handler)         /auth                                        None               username         None             POST
                                                                                                                                                  password
Authentication    When making authentication to LinkedIn Service, sometimes       /auth/verification                           None               email pin        None             POST
                  LinkedIn needs an email verification pin to make the session.
                  This endpoint use for it.
People            Search People                                                   /people/search_people                        url or keywords    None             Proxy            GET
                                                                                                                                                                   Cookie
People            Get People Profile                                              /people/profile/{people_public_id}           None               None             Proxy            GET
                                                                                                                                                                   Cookie
People            Make Connection and Send Message                                /people/make_connection/{people_public_id}   None               Message          Proxy            POST
                  (Message length must be < 300)                                                                                                                   Cookie
Message           Get all conversation in conversation field                      /message/conversations                       None               None             Proxy            GET
                                                                                                                                                                   Cookie
Message           Get message detail from a specific user                         /message/detail/{people_public_id}           None               None             Proxy            GET
                                                                                                                                                                   Cookie
Message           Send message to a specific conversation                         /message/{conversation_id}                   None               Message          Proxy            POST
                                                                                                                                                                   Cookie
================  ==============================================================  ===========================================  =================  ===============  ===============  =============
