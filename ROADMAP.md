The pygridtools should be as simple as possible, not much as a wrapper for
existing tools (e.g. use Ganga).
Current foreseen functionality:
 - schedule copy from one SE to another
 - 'local' only: create a recursive list of files and folders to transfer via gridFTP
 - submit jobs to HTCondor
   - include X509 proxy
   - include setup of software (CMSSW, conda, custom)
   - can ganglia do this for CMSSW?


 CMSSW submission:
  - needs to get the current release
  - assume software in /cvmfs/cms.cern.ch
  - needs to pack everything in source
  - needs to transfer packed source to /hdfs/tmp/user/<jobid>
