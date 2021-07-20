def get_assignments(userdata):
    import imaplib                              
    import email
    from email.header import decode_header
    import webbrowser
    import os
    import sys
    conn = imaplib.IMAP4_SSL("imap.gmail.com")

    try:
        (retcode, capabilities) = conn.login(userdata["email"], userdata["password"])
    except:
        print(sys.exc_info()[1])
        sys.exit(1)
    conn.list()
    conn.select(readonly=1) # Select inbox or default namespace
    (retcode, messages) = conn.search(None, '(UNSEEN)')
    links = []
    subjects = []
    if retcode == 'OK':
        for num in messages[0].decode().split(' '):
            typ, data = conn.fetch(num,'(RFC822)')
            for response in data:
                if isinstance(response, tuple):
                    
                    msg = email.message_from_bytes(response[1])

                    if "New assignment" in msg["Subject"] or "Due tommorow" in msg["Subject"]:
                        subjects.append(msg["Subject"])
                        acquired = str(response[1]).index('details')
                        i = ""
                        
                        while i != "<":
                            acquired -= 1
                            i = str(response[1])[acquired]

                        acquired2 = str(response[1]).index('details')

                        i = ""

                        while i != ">":
                            acquired2 += 1
                            i = str(response[1])[acquired2]

                        link = str(response[1])[acquired+1:acquired2]
                        links.append(link)
                    
    conn.close()
    return links,subjects
