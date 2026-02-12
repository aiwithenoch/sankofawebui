import os
import sys

# Add the backend directory to the sys.path so we can import open_webui
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from open_webui.main import app
