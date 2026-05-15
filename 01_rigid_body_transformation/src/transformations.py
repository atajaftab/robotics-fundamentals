import numpy as np


def rot_x(theta: float) -> np.ndarray:
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([
        [1.0, 0.0, 0.0],
        [0.0, c, -s],
        [0.0, s, c],
    ])


def rot_y(theta: float) -> np.ndarray:
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([
        [c, 0.0, s],
        [0.0, 1.0, 0.0],
        [-s, 0.0, c],
    ])


def rot_z(theta: float) -> np.ndarray:
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([
        [c, -s, 0.0],
        [s, c, 0.0],
        [0.0, 0.0, 1.0],
    ])


def make_transform(R: np.ndarray, p: np.ndarray) -> np.ndarray:
    R = np.asarray(R, dtype=float)
    p = np.asarray(p, dtype=float).reshape(3)

    if R.shape != (3, 3):
        raise ValueError("R must have shape (3, 3).")

    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = p
    return T


def inverse_transform(T: np.ndarray) -> np.ndarray:
    T = np.asarray(T, dtype=float)

    if T.shape != (4, 4):
        raise ValueError("T must have shape (4, 4).")

    R = T[:3, :3]
    p = T[:3, 3]

    T_inv = np.eye(4)
    T_inv[:3, :3] = R.T
    T_inv[:3, 3] = -R.T @ p

    return T_inv


def transform_point(T: np.ndarray, point: np.ndarray) -> np.ndarray:
    point = np.asarray(point, dtype=float).reshape(3)
    point_h = np.array([point[0], point[1], point[2], 1.0])
    transformed = T @ point_h
    return transformed[:3]