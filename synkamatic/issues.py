"""
Implementations of issue trackers
"""

class IssueTracker(object):
    """ABC"""

class Bugzilla(IssueTracker):
    """bugzilla issue tracker"""
    url = 'https://api-dev.bugzilla.mozilla.org/latest/' # REST API for bugzilla

class GithubPullRequest(IssueTracker):
    """github pull request"""

    
