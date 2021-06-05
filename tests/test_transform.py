from samestats.samestats import load_dataset, run_pattern


def test_run_pattern():
    df = load_dataset("dino")
    temp = run_pattern(df, target="circle", iters=10, num_frames=2)
    # EP: is there any better check? seems temp oputput is not deterministic,
    #     will vary by run
    # FIXME: the test also writes files to root of folder, must redirect
    assert temp.shape == (142, 2)
