set shell := ["bash", "-cu"]

set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

default:
	just --list

get-pf-split-data:
	python src/p_faciparum_extraction.py
	python src/split_data.py
