from pathlib import Path

env_path = Path(__file__).parent
if not Path(f"{env_path}/config/config.ini").exists():
    print("no")
else:
    print("yes")
