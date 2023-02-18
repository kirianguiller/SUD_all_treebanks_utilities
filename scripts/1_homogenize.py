from glob import glob
import os
from pathlib import Path
import shutil
from conllup.conllup import readConlluFile

PATH_TREEBANKS_SOURCE = Path(__file__).parent.parent / "treebanks"
PATH_TREEBANKS_TARGET = Path(__file__).parent.parent / "data" / "gold"
PATH_TREEBANKS_ALL_TOGETHER_TARGET = Path(__file__).parent.parent / "data" / "all_together"

for path in [PATH_TREEBANKS_TARGET, PATH_TREEBANKS_ALL_TOGETHER_TARGET]:
    if not os.path.isdir(path):
        os.makedirs(path)

path_mapping = {
    "SUD_Beja-NSC": "",
    "SUD_Chinese-PatentChar": "",
    "SUD_French-GSD": "",
    "SUD_French-ParisStories": "",
    "SUD_Naija-NSC": "",
    "SUD_Tunisian_Arabic-NAxLAT": "",
    "SUD_Zaar-Autogramm": "CORPUS",
}

for treebank_name, folder_conll in path_mapping.items():
    path_treebank_conlls_folder = PATH_TREEBANKS_SOURCE / treebank_name / folder_conll
    # print(path_treebank_conlls_folder)
    path_gold_folder_output = PATH_TREEBANKS_TARGET / treebank_name
    if os.path.isdir(path_gold_folder_output):
        shutil.rmtree(path_gold_folder_output)
    os.makedirs(path_gold_folder_output)
    path_treebank_conlls = glob(str(path_treebank_conlls_folder) + "/*.conllu")
    for path_conll_src in path_treebank_conlls:
        conll_name = Path(path_conll_src).name
        path_conll_dest = path_gold_folder_output / conll_name
        path_conll_all_together_dest = PATH_TREEBANKS_ALL_TOGETHER_TARGET / conll_name
        shutil.copyfile(path_conll_src, path_conll_dest)
        shutil.copyfile(path_conll_src, path_conll_all_together_dest)

        # sentences_json = readConlluFile(path_conll_src)
        # for sentence_json in sentences_json:
        #     for token in sentence_json["treeJson"]["nodesJson"].values():
        #         print(token["FORM"])
