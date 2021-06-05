from samestats.samestats import load_dataset


def test_load_dino():
    df = load_dataset(name="dino")
    assert df.shape == (142, 2)
