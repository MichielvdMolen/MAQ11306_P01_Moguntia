try:
    from ipywidgets import *
except:
    from IPython.html.widgets import *
import subprocess,glob,os, datetime

class CMoguntia:
    def __init__(self):
        self.infiles = glob.glob('*.in')
        self.infiles.sort()
        self.name = 'DUMMY'
        self.molmass = '28.5'
        interact_manual(self.Moguntia,inputfile = self.infiles)
        
    def Moguntia(self,inputfile = 'test.in'):
        xfile = open(inputfile,'r')
        outp = subprocess.check_output(['MODEL/MOGUNTIA'],stdin=xfile)
        print(outp.decode("utf-8")) 
        xfile.close()
        xfile = open(inputfile,'r')
        # now process the output:
        lines = xfile.readlines()
        for line in lines:
            if line.startswith('TITLE'): self.title = line.split()[1]
            if line.startswith('START_DATE'): self.start_date = line.split()[1]
            if line.startswith('END_DATE'): self.end_date = line.split()[1]
            if line.startswith('MOLMASS'): self.molmass = line.split()[1]
            if line.startswith('NAME'): self.name = line.split()[1]
        xfile.close()
        xfile = open(os.path.join('OUTPUT',self.title+'files_written'))
        
        local = datetime.datetime.fromtimestamp(os.path.getctime(inputfile)) + datetime.timedelta(hours=2)
        local = datetime.datetime.strftime(local, '%Y-%m-%d %H:%M:%S')
        print('MOGUNTIA has now run according to the input file %s, changed at %s. Congratulations!'%(inputfile,local))
        print('You can now inspect the simulated concentrations by activating the Python code in the cell below.')
        lines = xfile.readlines()
        lines.sort()
        self.outputfiles = lines       
        


