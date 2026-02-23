#!/bin/bash
# CV PDF Generator — Shell wrapper
# Sets the Homebrew library path required by WeasyPrint on macOS, then runs the Python script.
# DO NOT AUTO-EDIT.
#
# Usage:
#   bash master/generate_cv.sh <input_md> <output_pdf>
#
# Example:
#   bash master/generate_cv.sh \
#     roles/Acme_DeploymentLead/05_tailored_CV_final.md \
#     roles/Acme_DeploymentLead/Acme_DeploymentLead_CV.pdf

export DYLD_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_LIBRARY_PATH
python3 "$(dirname "$0")/generate_cv.py" "$@"
