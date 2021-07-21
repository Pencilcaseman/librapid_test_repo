import re
import os

def recursive_search(dir, terms):
    files = os.listdir(dir)

    for file in files:
        f = os.path.join(dir, file)
        if os.path.isdir(f):
            try:
                recursive_search(f, terms)
            except PermissionError:
                pass
        else:
            for term in terms:
                if re.match(term, file):
                    print(f)

def find_files(directory, search):
    search_terms = []
    if isinstance(search, str):
        search_terms = [re.compile(search)]
    elif isinstance(search, list):
        search_terms = [re.compile(term) for term in search]
    else:
        raise TypeError("Expected str or list")
    
    recursive_search(directory, search_terms)

terms = [r"^cblas\.h", r"^f77blas\.h", r"^openblas_config\.h", r".*\.lib$", r".*\.a$", r".*\.so$", r".*\.dll$"]
find_files(os.getcwd(), terms)
