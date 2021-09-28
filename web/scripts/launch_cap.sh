#!/bin/bash

# do not forget to add this to `visudo`:
# `www-data ALL=NOPASSWD: /var/www/html/scripts/launch_cap.sh`

run_user="ced"

cwd="/home/ced/git/icf/CAP/"
main="Main.py"
src="src/"
python="/home/ced/Apps/miniconda3/envs/cap/bin/python"

cmd_export='export PYTHONPATH='${PYTHONPATH}':/'${cwd}${src}
cmd_cd='cd '${cwd}
cmd_eval='eval '${python}'" "'${src}${main}

su -c "${cmd_export} && ${cmd_cd} && ${cmd_eval}" ${ced}
