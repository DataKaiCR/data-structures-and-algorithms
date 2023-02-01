# Sorry for the hack, but I need to reference this project as a module.
import sys,os
project_path = os.path.abspath(os.path.join(os.getcwd(), '.')) # Overkill but safe
sys.path.insert(0, project_path)