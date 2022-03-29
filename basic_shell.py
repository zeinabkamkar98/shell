import os,signal
import fancycompleter
import style
import readline
import re
from datetime import datetime
import pathlib


###################################################################

COMMANDS = []
#add command suggestion
COMMANDS.append("&")
COMMANDS.append("alias")
COMMANDS.append("apropos")
COMMANDS.append("apt-get")
COMMANDS.append("aptitude")
COMMANDS.append("aspell")
COMMANDS.append("awk")
COMMANDS.append("basename")
COMMANDS.append("base32")
COMMANDS.append("base64")
COMMANDS.append("bash")
COMMANDS.append("bc")
COMMANDS.append("bg")
COMMANDS.append("bind")
COMMANDS.append("break")
COMMANDS.append("builtin")
COMMANDS.append("bzip2")
COMMANDS.append("cal")
COMMANDS.append("case")
COMMANDS.append("cat")
COMMANDS.append("cd")
COMMANDS.append("cfdisk")
COMMANDS.append("chattr")
COMMANDS.append("chgrp")
COMMANDS.append("chmod")
COMMANDS.append("chown")
COMMANDS.append("chpasswd")
COMMANDS.append("chroot")

RE_SPACE = re.compile('.*\s+$', re.M)

class Completer(object):

    def _listdir(self, root):
        "List directory 'root' appending the path separator to subdirs."
        res = []
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.isdir(path):
                name += os.sep
            res.append(name)
        return res

    def _complete_path(self, path=None):
        "Perform completion of filesystem path."
        if not path:
            return self._listdir('.')
        dirname, rest = os.path.split(path)
        tmp = dirname if dirname else '.'
        res = [os.path.join(dirname, p)
                for p in self._listdir(tmp) if p.startswith(rest)]
        # more than one match, or single match which does not exist (typo)
        if len(res) > 1 or not os.path.exists(path):
            return res
        # resolved to a single directory, so return list of files below it
        if os.path.isdir(path):
            return [os.path.join(path, p) for p in self._listdir(path)]
        # exact file match terminates this completion
        return [path + ' ']

    def complete_extra(self, args):
        "Completions for the 'extra' command."
        if not args:
            return self._complete_path('.')
        # treat the last arg as a path and complete it
        return self._complete_path(args[-1])

    def complete(self, text, state):
        "Generic readline completion entry point."
        buffer = readline.get_line_buffer()
        line = readline.get_line_buffer().split()
        # show all commands
        if not line:
            return [c + ' ' for c in COMMANDS][state]
        # account for last argument ending in a space
        if RE_SPACE.match(buffer):
            line.append('')
        # resolve command to the implementation function
        cmd = line[0].strip()
        if cmd in COMMANDS:
            impl = getattr(self, 'complete_%s' % cmd)
            args = line[1:]
            if args:
                return (impl(args) + [None])[state]
            return [cmd + ' '][state]
        results = [c + ' ' for c in COMMANDS if c.startswith(cmd)] + [None]
        return results[state]

###################################################################
def theme():

    while True:

        select=input("1)screen_backgroung\n2)screen_text\nexit\n")

        if len(select)==0:
            pass
        
        elif select.split()[0]=="exit":
            break

        elif int(select.split()[0])==1:
            bg_color=input("which color:\nblack\nred\ngreen\nyellow\nblue\nmagenta\ncyan\nwhite\ndefault\n")

            if len(bg_color)==0:
                pass

            elif bg_color.split()[0]=="black":
                os.system('setterm --background black')

            elif bg_color.split()[0]=="red":
                os.system('setterm --background red')

            elif bg_color.split()[0]=="green":
                os.system('setterm --background green')

            elif bg_color.split()[0]=="yellow":
                os.system('setterm --background yellow')

            elif bg_color.split()[0]=="blue":
                os.system('setterm --background blue')

            elif bg_color.split()[0]=="magenta":
                os.system('setterm --background magenta')

            elif bg_color.split()[0]=="cyan":
                os.system('setterm --background cyan')

            elif bg_color.split()[0]=="white":
                os.system('setterm --background white')

            elif bg_color.split()[0]=="default":
                os.system('setterm --background default')

            else:
                pass


        elif int(select.split()[0])==2:
            

            bg_color=input("which color:\nblack\nred\ngreen\nyellow\nblue\nmagenta\ncyan\nwhite\ndefault\n")

            if len(bg_color)==0:
                pass

            elif bg_color.split()[0]=="black":
                os.system('setterm --foreground black')


            elif bg_color.split()[0]=="red":
                os.system('setterm --foreground red')

            elif bg_color.split()[0]=="green":
                os.system('setterm --foreground green')

            elif bg_color.split()[0]=="yellow":
                os.system('setterm --foreground yellow')

            elif bg_color.split()[0]=="blue":
                os.system('setterm --foreground blue')

            elif bg_color.split()[0]=="magenta":
                os.system('setterm --foreground magenta')

            elif bg_color.split()[0]=="cyan":
                os.system('setterm --foreground cyan')

            elif bg_color.split()[0]=="white":
                os.system('setterm --foreground white')

            elif bg_color.split()[0]=="default":
                os.system('setterm --foreground default')

            else:
                pass

        

###################################################################
def get_input():

    comp = Completer()
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(comp.complete)
    readline.parse_and_bind('set editing-mode vi')

    print(style.bold(style.green("time:{",style.white(datetime.now().strftime("%H:%M:%S")),"}"),style.green("Directory:{",style.white(pathlib.Path().absolute()),"}")))
    input_script=input(style.yellow(">> "))
    out=[]
    dq=0
    j=0
    k=0
    if len(input_script)==0:
        return out

    for i in range(len(input_script)):

        if (input_script[i]==" "):
            if input_script[i-1]!="\\":
                if dq!=1:
                    out.append(input_script[j:i])
                    j=i+1

        if (input_script[i]=='"'):
            if dq==0:
                dq=1
            else:
                dq=0
        k=i

    out.append(input_script[j:i+1])

    return out

###############################################################

# bashrc
# file= open("conf.txt", "r")
# data=file.readlines()

# for d in data:
#     pass

# file.close()

###############################################################
bg_list_pid=[]
bg_list_command=[]
print(style.green("Hi :)"))

while True:

    in_list=get_input()
        
    if len(in_list)==0:
        pass 
    
    elif in_list[0]=="theme" :
        theme()

    elif in_list[0]=="exit" :
        print(style.green("Bye :("))
        break

    elif in_list[0]=="pwd":
        print(os.getcwd())

    elif in_list[0]=="cd":
        os.chdir(in_list[1])

    elif in_list[0]=="bglist":
        for counter in range(len(bg_list_command)):
            print(counter,bg_list_pid[counter],bg_list_command[counter])
        
    elif in_list[0]=="bgkill":
        os.kill(bg_list_pid[int(in_list[1])],signal.SIGTERM)
        del bg_list_pid[int(in_list[1])]
        del bg_list_command[int(in_list[1])]

    elif in_list[0]=="bgstop":
        os.kill(bg_list_pid[int(in_list[1])],signal.SIGSTOP)

    elif in_list[0]=="bgstart":
        os.kill(bg_list_pid[int(in_list[1])],signal.SIGCONT)
    

    else:

        pid=os.fork()

        if in_list[0]=="bg":            
            bg_list_pid.append(pid)
            bg_list_command.append(in_list[1:])

        if pid==0:

            if in_list[0]=="bg":                
                os.execvp(in_list[1],in_list[1:])

            else:
                os.execvp(in_list[0],in_list)
        
        elif pid in bg_list_pid:            
            os.waitpid(pid,os.WNOHANG)

        else:            
            os.waitpid(pid,0)

        
        
        