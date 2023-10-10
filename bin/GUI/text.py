import sys
from pathlib import Path
env_path = Path(__file__).parent

sys.path.append(rf"{env_path}")
import assets.logs as logs

logs.creat_log()