#!/usr/bin/env bash

#   NAME: StdVSTools.sh
#   DATE: 04/03/2024
# .SYNOPSIS
#    Generate file and folder structures for contestant search utilities
#
# .DESCRIPTION
#    Generate file and folder structures for contestant search utilities

lorum="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et\
 dolore magna aliqua. Tortor aliquam nulla facilisi cras fermentum. Sodales ut eu sem integer. Fusce id velit\
 ut tortor pretium viverra suspendisse. Elementum nisi quis eleifend quam adipiscing vitae proin sagittis\
 nisl. Cursus metus aliquam eleifend mi in. Sed turpis tincidunt id aliquet risus feugiat. Tellus in hac\
 habitasse platea dictumst. Eu mi bibendum neque egestas congue quisque egestas. Facilisi etiam dignissim\
 diam quis enim lobortis."

path_depth=6

echo Saving folder structure in $HOME.

mkdir $HOME/competition
mkdir $HOME/competition/milestone1
mkdir $HOME/competition/milestonex

curr_dir=$HOME/competition/milestone1

for ((i = 1 ; i <= $path_depth ; i++)); do
    curr_dir=$curr_dir/f$i
    mkdir $curr_dir
    for fn in john paul george ringo; do
        echo -en "$i-$fn\n\n$lorum" > $curr_dir/$fn.txt
    done
done

curr_dir=$HOME/competition/milestonex

for ((i = 1 ; i <= $path_depth ; i++)); do
    if [[ $i == 6 ]]; then
        ln -s $curr_dir $curr_dir/f6
    else
        curr_dir=$curr_dir/f$i
        mkdir $curr_dir
        for fn in john paul george ringo; do
            echo -en "$i-$fn\n$lorum" > $curr_dir/$fn.txt
        done
    fi
done
