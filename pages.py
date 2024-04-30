import shutil
total, used, free = shutil.disk_usage("/")

class commands_descriptions: # Klasse für die Help Page

    NetswanSuperBot = "🌠Version 0.1 INDEV 🌠\n"    
    Prefix = "%\n"
    Start = "Starte dem Session-Client"
 
    OpenSess = "Öffne eine neue Session"

    DiskSpace = "Zeigt informationen über den Festplattenspeicher an."
    netinfo = "Zeigt informationen über die Netzwerkkonfiguration an."
    dockerinfo = "Zeigt informationen über den Docker und Docker-Compose config an."
    dcinfo = "Zeigt informationen über den Discord Server an."
    devinfo = "Zeigt informationen über den Entwickler an."

class Dsk_space: # Klasse für die Disk Space Page

    NetswanSuperBot = "💾Disk Space Tool💾\n"    
    Festplattenspeicher = total
    Belegt = used
    Offen = free

class Net_info:
    NetswanSuperBot = "🌐Network Informtion🌐\n"
    Status = "Work In Progress"


class Docker_info:
    NetswanSuperBot = "🐳Docker Information🐳\n"
    Status = "Work In Progress"

class Discord_info:
    NetswanSuperBot = "🤖Bot Information🤖\n"
    Status = "Work In Progress"


class Dev_info:
    NetswanSuperBot = "👥Developer Information👥\n"
    Author = "00Gaddy/Junes.Z"
    ProvidedBy = "Netswan"



