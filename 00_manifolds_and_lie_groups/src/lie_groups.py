import numpy as np


def skew(vector: np.ndarray) -> np.ndarray:
    """
    Return the skew-symmetric matrix representation of a 3D vector.

    For a vector w = [wx, wy, wz], the skew-symmetric matrix [w]_x is:

        [  0  -wz   wy ]
        [ wz    0  -wx ]
        [-wy   wx    0 ]

    It satisfies:

        [w]_x @ v = w x v

    for any 3D vector v.
    """
    vector = np.asarray(vector, dtype=float).reshape(3)
    wx, wy, wz = vector

    return np.array([
        [0.0, -wz, wy],
        [wz, 0.0, -wx],
        [-wy, wx, 0.0],
    ])


def so3_exp(rotation_vector: np.ndarray) -> np.ndarray:
    """
    Map a 3D rotation vector to a valid rotation matrix using the SO(3) exponential map.

    The input is a rotation vector phi = omega * theta:
    - its direction is the rotation axis,
    - its norm is the rotation angle in radians.

    Rodrigues' formula is used to compute the exponential map.
    """
    rotation_vector = np.asarray(rotation_vector, dtype=float).reshape(3)
    theta = np.linalg.norm(rotation_vector)

    rotation_vector_hat = skew(rotation_vector)

    if theta < 1e-12:
        return np.eye(3) + rotation_vector_hat

    return (
        np.eye(3)
        + (np.sin(theta) / theta) * rotation_vector_hat
        + ((1.0 - np.cos(theta)) / theta**2) * (rotation_vector_hat @ rotation_vector_hat)
    )


def is_rotation_matrix(R: np.ndarray, tolerance: float = 1e-9) -> bool:
    """
    Check whether a matrix is a valid 3D rotation matrix.

    A valid rotation matrix satisfies:

        R.T @ R = I
        det(R) = 1
    """
    R = np.asarray(R, dtype=float)

    if R.shape != (3, 3):
        return False

    orthogonality_error = np.linalg.norm(R.T @ R - np.eye(3))
    determinant = np.linalg.det(R)

    return (
        orthogonality_error < tolerance
        and np.isclose(determinant, 1.0, atol=tolerance)
    )

def rot_x(theta: float) -> np.ndarray:
    """
    Return a 3D rotation matrix for rotation about the x-axis.
    """
    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([
        [1.0, 0.0, 0.0],
        [0.0, c, -s],
        [0.0, s, c],
    ])


def rot_y(theta: float) -> np.ndarray:
    """
    Return a 3D rotation matrix for rotation about the y-axis.
    """
    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([
        [c, 0.0, s],
        [0.0, 1.0, 0.0],
        [-s, 0.0, c],
    ])


def rot_z(theta: float) -> np.ndarray:
    """
    Return a 3D rotation matrix for rotation about the z-axis.
    """
    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([
        [c, -s, 0.0],
        [s, c, 0.0],
        [0.0, 0.0, 1.0],
    ])



def rotation_matrix_report(R: np.ndarray, name: str) -> None:
    """
    Print diagnostic information for a candidate rotation matrix.
    """
    orthogonality_error = np.linalg.norm(R.T @ R - np.eye(3))
    determinant = np.linalg.det(R)
    valid = is_rotation_matrix(R)

    print(f"{name}")
    print("-" * len(name))
    print(f"Orthogonality error ||R.T @ R - I||: {orthogonality_error:.6e}")
    print(f"Determinant det(R): {determinant:.6f}")
    print(f"Valid rotation matrix: {valid}")
    print()