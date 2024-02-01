#!/bin/bash

touch $1 && chmod +x $1 && echo "#!/usr/bin/env ruby \n puts ARGV[0].scan(/**/).join" > $1
