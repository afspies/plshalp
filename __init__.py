import time
from contextlib import contextmanager
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

@contextmanager
def timed_context(description: str):
    start_time = time.time()
    start_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{Colors.OKBLUE}{'=' * 50}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{description} started at {start_datetime}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'=' * 50}{Colors.ENDC}")
    
    try:
        yield
    finally:
        end_time = time.time()
        end_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elapsed_time = end_time - start_time
        
        print(f"{Colors.OKBLUE}{'=' * 50}{Colors.ENDC}")
        print(f"{Colors.OKGREEN}{description} completed at {end_datetime}{Colors.ENDC}")
        print(f"{Colors.WARNING}Elapsed time: {elapsed_time:.2f} seconds{Colors.ENDC}")
        print(f"{Colors.OKBLUE}{'=' * 50}{Colors.ENDC}")
