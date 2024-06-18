from ftplib import FTP
import shutil
import os

PathToSource = r"F:/Obsidian" #Source directory
try:
    ftp = FTP()
    ftp.connect("YOUR IP", YOUR PORT)
    ftp.login("YOUR LOGIN", "YOUR PASSWORD")

    try:
        ftp.rmd("Obsidian") #A folder in your smartphone where you need to dump the directory you want to use
        ftp.mkd("Obsidian") 
    except:
        pass
        
    ftp.cwd("Obsidian")
    def uploadThis(path):
        
        files = os.listdir(path)
        os.chdir(path)
        for f in files:
            if os.path.isfile(os.path.join(path,f)):
                fh = open(f, 'rb')
                ftp.storbinary('STOR %s' % f, fh)
                fh.close()
            elif os.path.isdir(os.path.join(path,f)):
                try:
                    ftp.rmd(f)
                except:
                    pass
                try:
                    ftp.mkd(f)
                except:
                    pass
                ftp.cwd(f)
                uploadThis(os.path.join(path,f))
        
        ftp.cwd('..')

        os.chdir('..')

    uploadThis(PathToSource)
    ftp.quit()
except:
    pass
