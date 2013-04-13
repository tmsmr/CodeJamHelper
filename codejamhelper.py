import os, numpy

DOWNLOAD_DIR = '/home/thomas/Downloads'
OUTPUT_DIR = '/home/thomas/Desktop'
OUTPUT_FILENAME = 'codejam.out'
LOGNAME = 'CodeJamHelper'

def get_input():
	filenames = filter(lambda x: x[-3:] == '.in', os.listdir(DOWNLOAD_DIR))
	fileinfo = map(lambda fname: (fname, os.path.getmtime(os.path.join(DOWNLOAD_DIR, fname))), filenames)
	fileinfo = sorted(fileinfo, key=lambda x: x[1], reverse=True)
	if len(fileinfo) > 0:
		log('%d files with extension *.in found in %s' % (len(fileinfo), DOWNLOAD_DIR))
		for idx in enumerate(fileinfo):
			log('%s) %s' % (idx[0], idx[1][0]))
		while(True):
			try:
				choice = raw_input("[%s] select file (0):" % (LOGNAME))
				if choice == "":
					choice = 0
				else:
					choice = int(choice)
			except ValueError: pass
			else:
				filename = fileinfo[choice]
				break
		log('opening %s' % filename[0])
		with open(os.path.join(DOWNLOAD_DIR, filename[0])) as fp:
			lines = map(lambda x: str.rstrip(x, "\n"), fp.readlines())
		return lines
	else:
		log('no files in %s with extension *.in found' % DOWNLOAD_DIR)

def get_count(input):
	return int(input[0].strip())

def get_cases(input):
	return input[1:]

def get_case_tuples(input,tupleDesc):
	inputTuples = []
	for listPos in xrange(1,len(input),len(tupleDesc)):
		tmp = []
		for tuplePos in xrange(0,len(tupleDesc)):
			tmp.append(tupleDesc[tuplePos](input[listPos + tuplePos]))
		inputTuples.append(tuple(tmp))
	return inputTuples

def matrix_from_2Dlist(list, conversionMap):
	m,n = len(list),len(list[0])
	A = numpy.zeros((m,n))
	for mx in xrange(m):
		for nx in xrange(n):
			A[mx][nx] = conversionMap[list[mx][nx]]
	return A

def save_output(lines):
	for idx, line in enumerate(lines):
		lines[idx] = "Case #%s: %s\n" % (idx+1, line)
	lines[idx] = lines[idx][:-1]
	log('writing %d lines to %s/%s' % (idx+1, OUTPUT_DIR, OUTPUT_FILENAME))
	with open(os.path.join(OUTPUT_DIR, OUTPUT_FILENAME), 'w') as fp:
		fp.writelines(lines)

def log(string):
	print('[%s] %s' % (LOGNAME, string))