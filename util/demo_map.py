import numpy as np


def main(**kwargs):
    demomap = [
        # fmt: off
        [['@', 'X'],['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['p', '3'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['P', 'R'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['y', '1'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['b', '6'],['g', '8'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['y', '3'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['@', 'X'],['r', '2'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['@', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        [['@', 'X'],['@', 'X'],['@', 'X'],['@', 'X'],['o', '9'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X'],['.', 'X']],
        # fmt: on
    ]
    maparr = np.array(demomap)
    np.save("demo_scene.npy", maparr)


if __name__ == "__main__":
    main()
