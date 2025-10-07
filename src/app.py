import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from data.students import STUDENTS
from src.version import VERSION

def banner():
    names = ", ".join(STUDENTS)
    return f"Hola {names}! (versión {VERSION})"

if __name__ == "__main__":
    print(banner())
