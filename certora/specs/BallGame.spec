methods {
    ballPosition() returns(uint8) envfree
    pass()                        envfree
}

/// The ball should never get to player 2
invariant playerTwoNeverWins()
    ballPosition() != 2

