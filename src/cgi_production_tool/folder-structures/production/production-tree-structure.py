from cgi_production_tool.directorygeneration.home_directory_validator import expanduser

expanduser = True

class validHomeDir():
    if expanduser is True:
        print("Home directory have been found")
