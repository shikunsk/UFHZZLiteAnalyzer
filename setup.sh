#!/bin/bash

export PYTHONPATH=${PYTHONPATH}:${PWD}/

cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_4/src/ 
eval `scramv1 runtime -sh`
cd -
