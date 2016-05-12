org = "servo"

ignore_repos = ["skia", "skia-snapshots", "cairo", "libpng", "libcss",
                "libhubbub", "libparserutils", "libwapcaplet", "pixman"]
count_forks = ["glutin","rust-openssl"]


# Path to where we'll dump the bare checkouts. Must end in /
clones_dir = "repos/"

# Path to the concatenated log
log_path = "log.txt"

# Nuke the clones_dir afterwards?
destroy_clones = True
