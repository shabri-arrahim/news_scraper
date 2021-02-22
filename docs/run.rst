
================  ==============================================================  ===========================================  =================  ===============  =============
Category          Description                                                     Endpoint                                     Parameters         Data             Method
================  ==============================================================  ===========================================  =================  ===============  =============
Authentication    Make authentication to LinkedIn Service (Login handler)         /auth                                        None               username         POST
                                                                                                                                                  password
                                                                                                                                                  proxies
Authentication    When making authentication to LinkedIn Service, sometimes       /auth/verification                           None               email pin        POST
                  LinkedIn needs an email verification pin to make the session.
                  This endpoint use for it.
People            Search People                                                   /people/search_people                        url or keywords    None             GET
People            Get People Profile                                              /people/profile/{people_public_id}           None               None             GET
People            Make Connection and Send Message                                /people/make_connection/{people_public_id}   None               Message          POST
                  (Message length must be < 300)
Message           Get all conversation in conversation field                      /message/conversations                       None               None             GET
People            Get message detail from a specific user                         /message/detail/{people_public_id}           None               None             GET
People            Send message to a specific conversation                         /message/{conversation_id}                   None               Message          POST
================  ==============================================================  ===========================================  =================  ===============  =============
