#!/bin/bash
ls | grep 'pe.bam' | xargs -P 2 -I {} -t deduplicate_bismark --bam --paired -o s_{} {}