#!/usr/bin/env python

"""
Synkamatic helps to automate the syncing of changes between mirrored
(Mozilla) hg and github repos
"""

# Things we'll need:
# - a github account to turn hg pulled events into pull requests
# - pulse monitoring of hg commits to mozilla-central

import sys
import optparse
import .api

def main(args=sys.argv[:]):

    # parse command line options
    usage = '%prog [options]'
    class PlainDescriptionFormatter(optparse.IndentedHelpFormatter):
        """description formatter for console script entry point"""
        def format_description(self, description):
            if description:
                return description + '\n'
            else:
                return ''
    parser = optparse.OptionParser(usage=usage, description=__doc__, formatter=PlainDescriptionFormatter())
    options, args = parser.parse_args(args)

    # instantiate API
    # (from .ini files?)
    # TODO
    # api.Synkamatic(...)

if __name__ == '__main__':
  main()
