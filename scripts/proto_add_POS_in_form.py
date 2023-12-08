import os
from conllup.conllup import readConlluFile, writeConlluFile

PATH_INPUT_FOLDERS = '/home/kirian/Projects/syntax/SUD_all_treebanks_utilities/data/all_together'
PATH_OUTPUT_FOLDERS = '/home/kirian/Projects/syntax/SUD_all_treebanks_utilities/data/all_together_proto'

for file in os.listdir(PATH_INPUT_FOLDERS):
    path_input_file = os.path.join(PATH_INPUT_FOLDERS, file)
    path_outpout_file = os.path.join(PATH_OUTPUT_FOLDERS, "proto_" + file)
    print("KK file", path_input_file)
    if os.path.isfile(path_input_file) and file.endswith('.conllu'): 
        sentences = readConlluFile(path_input_file)
        for sentence in sentences:
            for token in sentence['treeJson']['nodesJson'].values():
                token["FORM"] = token["FORM"] + token["UPOS"]

        writeConlluFile(path_outpout_file, sentences, overwrite=True)
            
