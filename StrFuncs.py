from colorama import *
from datetime import datetime
   

init()

def evnt() -> str:
    return f"[{Fore.CYAN}~{Style.RESET_ALL}]"

def err():
    return f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Style.RESET_ALL}"

def timenow():
    now = datetime.now()
    timee = now.strftime("%H:%M:%S")
    nowtime = (f"{Fore.YELLOW}[{Fore.WHITE}{timee}{Fore.YELLOW}]{Style.RESET_ALL}")
    return nowtime