from git import Repo
from pathlib import Path
import stat
from os import system

try:
    import httplib  # python < 3.0
except:
    import http.client as httplib


def have_internet() -> bool:
    conn = httplib.HTTPSConnection("8.8.8.8", timeout=15)
    try:
        conn.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        conn.close()


# stash existing

def git_pull():
    gb_repo = Repo('GameButton')
    if gb_repo.is_dirty():
        gb_repo.remotes.origin.pull()
        # make executable
        f = Path("/path/to/file.txt")
        f.chmod(f.stat().st_mode | stat.S_IEXEC)


def game_start():
    system('cmd /c "MYSTARTER"')


if __name__ == '__main__':
    have_internet()
    if have_internet():
        git_pull()
        game_start()
    else:
        system('cmd /c "ifconfig"')

