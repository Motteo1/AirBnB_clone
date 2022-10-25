#usr/env/bin bash
# This script auto-generates the project authors' names and email addresses, and adds them to the 'AUTHORS' file
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

{
	cat <<- 'EOH'
		# This file lists all the project contributors by name and email address
		# See the 'hack/generate-authors.sh' file for more info on generating it
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
