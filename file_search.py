import re
import os
import shutil

def recursive_search(dir, terms, lst):
	files = os.listdir(dir)

	for file in files:
		f = os.path.join(dir, file)
		if os.path.isdir(f):
			try:
				recursive_search(f, terms, lst)
			except PermissionError:
				pass
		else:
			for term in terms:
				if re.match(term, file):
					# print(f)
					lst.append(f)

def find_files(directory, search, lst=[]):
	search_terms = []
	if isinstance(search, str):
		search_terms = [re.compile(search)]
	elif isinstance(search, list):
		search_terms = [re.compile(term) for term in search]
	else:
		raise TypeError("Expected str or list")
    
	recursive_search(directory, search_terms, lst)
	return lst

terms = [
r"^cblas\.h",
r"^f77blas\.h",
r"^lapack\.h",
r"^lapacke\.h",
r"^lapacke_config\.h",
r"^lapacke_mangling\.h",
r"^lapacke_utils\.h",
r"^openblas_config\.h",
r".*\.lib$",
r".*\.a$",
r".*\.so$",
r".*\.dll$"
]

files = find_files(os.getcwd(), terms)
for f in files:
	print("Copying file:", f)
	
	path, name = os.path.split(f)
	new_dir = os.path.join(os.getcwd(), "located_files", name)
	os.makedirs(os.path.dirname(new_dir), exist_ok=True)
	shutil.copy(f, new_dir)
