from IPython.lib import passwd
import os

c = get_config()

if 'JUPYTER_PASSWORD' in os.environ:
    c.NotebookApp.password = passwd(os.environ["JUPYTER_PASSWORD"])

c.NotebookApp.open_browser = False
c.NotebookApp.notebook_dir = '/projects'
