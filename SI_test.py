import SI;

def test_SI():
    assert SI.si(1000,10,2) == 200.0,"simple interest function did not return correct value"
    assert SI.amount(2000,10,2)==2400.0,"amount function did not return correct value"

