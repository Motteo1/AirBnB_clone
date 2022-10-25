#usr/env/bin bash
# This script auto-generates the project authors' names and email addresses
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

{
	cat <<- 'EOH'
		# This file lists all the project contributors
		# See the 'hack/generate-authors.sh' file for more info
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
