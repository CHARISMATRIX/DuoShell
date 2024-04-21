PluginCommands = ["test"]

def output(txt,options):
    txt = str(txt)
    print(txt)
    filename = None
    for option in options:
        if option.startswith("-Output:") or option.startswith("O:"):
            filename = ":".join(option.split(":")[1:])
            print("SAVING: "+filename)
            break
    if filename:
        with open(filename, "w") as f:
            f.write(txt)

def OnCall(cmd,splitted,args,options,argString):
    if cmd == "test":
        print("Test plugin called!")
