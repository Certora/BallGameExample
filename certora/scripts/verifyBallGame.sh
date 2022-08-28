#!/bin/sh

certoraRun contracts/KeepAway.sol \
    --verify KeepAway:certora/specs/KeepAway.spec \
    --solc solc8.0
    --msg  "KeepAway verification"

