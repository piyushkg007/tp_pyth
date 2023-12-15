import subprocess

app_path = "C:\Program Files (x86)\FuH\Docklight V2.4\Docklight.exe"
f=1
k='1'
while(f==1):
   
    if(k=='1'):

        subprocess.Popen(app_path)
        import psutil

    app_name = "Docklight.exe"


    import psutil
    n=input()
    if(n=='c'):
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == app_name:
                process.terminate()
