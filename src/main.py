import os
import subprocess
error_command_not_found = 127

def installation():
    # requires brew and so curl
    brew = subprocess.run('brew update', shell = True, capture_output=True, text=True)
    if brew.returncode == error_command_not_found:
        print(brew.stdout)
        print('brew might not be correctly installed')
        return 1
    else:
        brew = subprocess.run('brew install arduino-cli', shell = True, capture_output=True,text=True)
        if brew.returncode == 0:
            # 0 means everything went fine
            print('arduino-cli is installed and ready to run')
            # initialization 
            arduino = subprocess.run('arduino-cli config set library.enable_unsafe_install true',shell = True, capture_output=True,text=True)
            
            return 0
    print('\n')
    #print(brew.returncode)
    print('\n')
    #print(brew.stderr)
    print('\n')
    #print(brew.stdout)



if __name__ == '__main__':
    if not installation() :
        pass
