#!/usr/bin/env python3


ver = 1.0
from colorama import *
init()
from StrFuncs import err, evnt, timenow
import asyncio 
import socket
import ast
import os
import sys
import time
import threading
import importlib
from importlib import util

def turn():
    input("Press any key to continue...")

def red(text):
    return Fore.RED + text + Style.RESET_ALL

def white(text):
    return Fore.WHITE + text + Style.RESET_ALL

def yellow(text):
    return Fore.yellow + text + Style.RESET_ALL


animdone = threading.Event()
stopanim = threading.Event()

def animation():
    try:
        for i in range(2):
            chars = [".", "..", "...", "   "]
            for i in chars:
                if stopanim.is_set():
                    break
                sys.stdout.write(f"\rInitializating Bullsploit{i}")
                sys.stdout.flush()
                time.sleep(0.5)
        sys.stdout.write("\r                            ")
        sys.stdout.flush()
    finally:
        animdone.set()

def check():
    counts = {"payloads": 0, "auxiliary": 0, "post": 0}
    paths = ["auxiliary", "payloads", "post"]
    errlog = []
    threading.Thread(target=animation, daemon=True).start()
    try:
        if not os.path.exists("Modules"):
            stopanim.set()
            print(f"\n{err()} Not found the Modules path")
            return
        for i in paths:
            path = os.path.join("Modules", i)
            if not os.path.exists(path):
                errlog.append(f"Not found the {i} path")
        for root, dirs, files in os.walk("Modules"):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    if f"{os.sep}payloads" in root:
                        counts["payloads"] += 1
                    elif f"{os.sep}auxiliary" in root:
                        counts["auxiliary"] += 1
                    elif f"{os.sep}post" in root:
                        counts["post"] += 1
                    modul = os.path.join(root, file)
                    modulename = file[:-3]
                    try:

                        with open(modul, "r", encoding="utf-8") as fail:
                           code = fail.read()
                           ast.parse(code)
                    except Exception as f:
                        errlog.append(f"Error in file {file} in {root}")

                    except Exception as j:
                        pass

        payloadc = counts["payloads"]
        auxiliaryc = counts["auxiliary"]
        postc = counts["post"]

        if errlog:
            stopanim.set()
            print()
            for r in errlog:
                print(f"{err()} {r}")

        animdone.wait()
        mainmenu(payloadc, auxiliaryc, postc)
    except Exception as l:
        pass
    

def mainmenu(payloadc, auxiliaryc, postc):
    os.system("title Bullsploit Framework")
    print(red(f"""
       ,/         \\,
      ((__,-'''-,__))
       `--)~   ~(--`
      .-'(       )`-,
      `~~`d\\   /b`~~`
          |     |
          (6___6)  {Fore.WHITE}{Back.RED}BullSploit{Style.RESET_ALL} {Fore.WHITE}{Back.RED}Framework{Style.RESET_ALL}{Fore.CYAN} dev{Fore.WHITE}#{Fore.CYAN}{ver} {Fore.RED}
           `---` {Style.RESET_ALL}"""))
    print(f"""
+- --=[ {f"{Fore.YELLOW}https://github.com/ghostemanelxrd123-creator{Style.RESET_ALL}":<43} ]-
+- --=[ {f"{payloadc} payload - {auxiliaryc} auxiliary - {postc} post":<45}]-
""")
    BSC(payloadc, auxiliaryc, postc)
    
class BSC:
    def __init__(self, payload, auxiliary, post):
        self.post = post
        self.payload = payload
        self.aux = auxiliary
        self.options = {}
        self.selectmod = ""
        self.rank = {"Bad": Fore.RED, "Good": Fore.GREEN, "Normal": Fore.YELLOW, "Excellent": Fore.CYAN}
        self.folders = ["auxiliary", "payloads", "post"]
        self.rules = {}
        self.corrkey = []
        self.modules = []
        self.analyse()
        self.run()

    def parse(self, args=None):
        if not args: return {}
        params = {}
        for i in args:
            if ":" in i:
                key, value = i.split(":", 1)
                params[key.lower()] = value
        return params


        

    def analyse(self):
        try:
            for folder in self.folders:
                path = os.path.join("Modules", folder)
                if os.path.exists(path):
                    for file in os.listdir(path):
                        if file.endswith(".py"):
                            modulepath = os.path.join(path, file)
                            self.modules.append({
                                "name": file.replace(".py", ""),
                                "type": folder,
                                "description": self.getdesc(modulepath),
                                "date": self.getdate(modulepath),
                                "rank": self.getrank(modulepath)
                                })
                else:
                    print(f"{err()} Folder {folder} was not found")
        except Exception as k:
            print(f"{err()} {k}")

    def getmeta(self, path, meta):
        try:
            with open(path, "r", encoding="utf-8") as f:
                parsed = ast.parse(f.read())
                for modul in parsed.body:
                    if isinstance(modul, ast.FunctionDef) and modul.name == meta:
                        for line in modul.body:
                            if isinstance(line, ast.Return) and isinstance(line.value, ast.Constant):
                                return line.value.value
            return f"No {meta}"
        except Exception as c:
            return "Read error"

    def getrank(self, path):
        return self.getmeta(path, "rank")

    def getdate(self, path):
        return self.getmeta(path, "date")

    def getdesc(self, path):
        return self.getmeta(path, "description")




    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        mainmenu(self.payload, self.aux, self.post)

    def table(self, modultype=None):
        try:
            if modultype is None:
                filtered = self.modules
            else:
                mtype = modultype.lower()
                if mtype == "payload": mtype = "payloads"
                if mtype == "aux": mtype = "auxiliary"
                filtered = [m for m in self.modules if m["type"].lower() == mtype]
            if not filtered:
                print(f"{err()} Not found modules for type: {mtype}")
                return
            print()
            print(f"  {evnt()}Founded modules {len(filtered)}")
            print(" ", "="*21)
            print()
            print("    #  Name                           Date         Rank      Description")
            print("  ", "-"*80)
            for cnt, mod in enumerate(filtered):
                rankcol = self.rank.get(mod["rank"], Fore.WHITE)
                if rankcol == Fore.WHITE:
                    ranktxt = f"{Fore.WHITE}None{Style.RESET_ALL}"
                else:
                    ranktxt = f"{rankcol}{mod["rank"]}{Style.RESET_ALL}"
                name = f"{mod["type"]}/{mod["name"]}"
                if len(name) >= 30:
                    name = name[:31] + "..."
                print(f"    {cnt:<2} {name:<30} {mod["date"]:<12} {ranktxt:<18} {mod["description"]} ")
            print()
        except Exception as y:
            print(f"{err()} {y}")
        

    def run(self):
        try:
            while True:
                selectmod = f" {Fore.RED}({self.selectmod}){Style.RESET_ALL}" if self.selectmod else ""
                rawcmd = input(f"\033[4mbsc\033[0m{selectmod}>").lower().strip().split()
                
                if not rawcmd:
                    continue
                cmd = rawcmd[0]
                
                args = rawcmd[1:] if len(rawcmd) > 1 else []

                

                if cmd == "exit" or cmd == "quit": sys.exit()
                
                elif cmd == "help":
                    print(""" Usage: bsc>[options]

Common options:
    help                           --View help
    search <moduletype>            --Search module
    usagr                          --View useragreement
    github                         --Open a bullsploit link on GitHub
    clear                          --Clear console
    use <module path>              --Use some module
    set <arguments>                --Add settings
    run                            --Start module
    exit                           --Exit bullsploit

                    """)

                elif cmd == "search":
                    self.table(args[0] if args else None)

                elif cmd == "run":
                    if not self.selectmod:
                        print(f"{err()} No module selected")
                    else:
                        mtype, mname = self.selectmod.split("/")
                        path = os.path.join("Modules", mtype, mname + ".py")
                        if not os.path.exists(path):
                            print(f"{err()} Module file not found {path}")
                    try:
                        spec = importlib.util.spec_from_file_location(mname, path)
                        modul = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(modul)
                        modul.launch(self.options)
                    except RuntimeError:
                        pass
                    except Exception as b:
                        print(b)



                elif cmd == "use":
                    if not args:
                        print(f"{err()} Usage: use <type>/<module>")
                        continue
                    module = args[0]
                    found = False
                    
                    
                    for m in self.modules:
                        mpath = f"{m["type"]}/{m["name"]}".lower()
                        if module == mpath:
                            found = True
                            self.selectmod = module
                    if not found: print(f"{err()} Not found module {module}")
                    scheme = self.selectmod
                    finallyscheme = "Modules." + scheme.replace("/", ".")
                    m = importlib.import_module(finallyscheme)
                    self.rules = m.depargs()
                    
                    for key, value in self.rules.items():
                        self.corrkey.append(key)




                elif cmd == "set":
                    if not args: 
                        print(f"{err()} Usage: set <args>")
                        continue
                    if not self.selectmod: 
                        print(f"{err()} No select module!")
                        return
                    
                    newparams = self.parse(args)
                    if not newparams:
                        print(f"{err()} Usage: set host:8.8.8.8 range:1-1024")
                    for key, value in newparams.items():
                        if key in self.corrkey:
                            print(f"{evnt()} {key.capitalize()} => {value}")
                        else:
                            print(f"{err()} Invalid parameter!")
                    self.options.update(newparams)

                elif cmd == "options":
                    if self.selectmod != "":
                        print(f" {evnt()} These parameters are available for {self.selectmod}: \n")
                        print(f"  Parameter      Data type\n  {"-"*26}")
                        for key, value in self.rules.items():
                            print(f"  {key:<10}     {str(value)}")
                        print()
                    

                elif cmd == "show" and self.selectmod is not None:
                    for key, value in self.options.items():
                        print(f"{evnt()} {key.capitalize()} => {value}")


                elif cmd == "back":
                    self.selectmod = ""
                    self.options = {}

                elif cmd == "check":
                    print(self.modules)



                elif cmd == "clear":
                    self.clear()
                else:
                    print(f"{err()} Error")
                
        except KeyboardInterrupt:
            choice = input(f"\nAre you sure you want to exit? (y/n)>").lower()
            if choice == "y": sys.exit()
            else: mainmenu()
        except Exception as h:
            print(f"{err()} {h}")
            turn()

if __name__ == "__main__":
    check()
