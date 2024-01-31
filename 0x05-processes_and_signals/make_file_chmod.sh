#!/bin/bash

touch $1 && chmod +x $1
echo "#!/usr/bin/env bash\n#pid" > $1
