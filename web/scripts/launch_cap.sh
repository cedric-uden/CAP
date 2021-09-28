cwd="/home/ced/git/icf/CAP/"
main="Main.py"
src="src/"
python="/home/ced/Apps/miniconda3/envs/cap/bin/python"


export PYTHONPATH=$PYTHONPATH:/$cwd$src
cd $cwd
eval $python" "$src$main
