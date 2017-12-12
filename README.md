Servo Org Stats
---------------

[![Build Status](https://travis-ci.org/servo/servo-org-stats.svg?branch=master)](https://travis-ci.org/servo/servo-org-stats)

The master branch of this repo holds assorted metadata needed to combine a
fork of
[gitstat](https://github.com/edunham/gitstat/), the
[orglog](https://github.com/edunham/orglog) tool,
[TravisCI](https://travis-ci.org/), and [nightli.es](https://nightli.es/) to
emit fancy graphs. The gh-pages branch contains the fancy graphs, overwritten
every day with the latest ones.

Gitstat's license is available
[here](https://github.com/youknowone/gitstat/blob/master/LICENSE) and Orglog's
license is available
[here](https://github.com/edunham/orglog/blob/master/LICENSE).

### Deployment: 

Travis needs `GH_USER`, `GH_PASS`, and `GH_TOKEN` environment variables 
belonging to an account that can push to this repo. The token should 
have the `repo` scope. The account @rustacean is used here because 
it does not have the same perms on other repos as @bors-servo.


