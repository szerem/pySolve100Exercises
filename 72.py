import webbrowser

# query = input("Enter your Google query: ")
query = "pomidor"
url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % query
webbrowser.open_new(url)

