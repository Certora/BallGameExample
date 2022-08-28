methods {
    ballPosition() returns(uint) envfree
    pass()                       envfree
}

/// The ball should never get to player 2
invariant playerTwoNeverWins()
    ballPosition() != 2

