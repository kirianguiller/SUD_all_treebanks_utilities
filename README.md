# SUD treebanks utilities
Utility repo and scripts for all SUD treebanks. This can be used for using all the SUD treebanks at once for some downstream tasks (training and evaluating multilingual parser; testing conllu handling libraries; etc...)

## Clone
Clone the repo with the recusrive-modules parameter
```bash
git clone --recurse-submodules https://github.com/kirianguiller/SUD_all_treebanks_utilities
```
If you already cloned the project and forgot --recurse-submodules, you can combine the git submodule init and git submodule update steps by running git submodule update --init. To also initialize, fetch and checkout any nested submodules, you can use the foolproof git submodule update --init --recursive.