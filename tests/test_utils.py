import utils as utl


def test_split2list():
    assert utl.split2list(100, [10, 10, 10]) == [10, 10, 10, 70]
    assert utl.split2list(25, [10, 10, 10]) == [10, 10, 5, 0]
    assert utl.split2list(1, [10, 10, 10]) == [1, 0, 0, 0]


def test_klimaka():
    assert utl.klimaka(100, [50, 50], [10, 20, 30]) == 15
    assert utl.klimaka(200, [50, 50], [10, 20, 30]) == 45


def test_distribute():
    assert utl.distribute(val=100.02, dist=[10, 20, 30, 40]) == [10, 20, 30.01, 40.01]
    assert utl.distribute(val=356.44, dist=[10, 20]) == [118.81, 237.63]
    assert utl.distribute(val=256.44, dist=[10, 10]) == [128.22, 128.22]


def test_relu():
    assert utl.relu(val=100, threshold=10) == 100
    assert utl.relu(val=10, threshold=10) == 10
    assert utl.relu(val=9, threshold=10) == 10
    assert utl.relu(val=9) == 9
    assert utl.relu(val=-9) == 0


def test_limit():
    assert utl.limit(val=110.023, limit=110.01) == 110.01
    assert utl.limit(val=110, limit=110) == 110
    assert utl.limit(val=109.99, limit=110) == 109.99
    assert utl.limit(val=-199, limit=110) == -199
