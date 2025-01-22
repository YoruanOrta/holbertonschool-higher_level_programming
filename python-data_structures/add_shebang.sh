#!/bin/bash

# Shebang line to add
SHEBANG="#!/usr/bin/python3"

# Find all .py files excluding files named 0-main.py to 12-main.py
for file in $(find . -type f -name "*.py" ! -regex ".*/[0-9]\{1,2\}-main.py"); do
    # Check if the shebang is already present
    if ! grep -q "$SHEBANG" "$file"; then
        # Add the shebang to the first line of the file
        sed -i "1i $SHEBANG" "$file"
        echo "Added shebang to: $file"
    else
        echo "Shebang already exists in: $file"
    fi
done
