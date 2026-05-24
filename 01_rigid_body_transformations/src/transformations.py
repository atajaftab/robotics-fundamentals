import numpy as np


def rot_x(theta: float) -> np.ndarray:
    """
    Returns a 3D rotation matrix for a rotation about the x-axis.

    The rotation follows the right-hand rule.
    The input angle should be in radians.

    Parameters
    ----------
    theta: float
        Rotation angle [rad]
    
    Returns
    -------
    np.ndarray
        A 3x3 rotation matrix
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
    Returns a 3D rotation matrix for a rotation about the y-axis.

    The rotation follows the right-hand rule.
    The input angle should be in radians.

    Parameters
    ----------
    theta: float
        Rotation angle [rad]
    
    Returns
    -------
    np.ndarray
        A 3x3 rotation matrix
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
    Returns a 3D rotation matrix for a rotation about the z-axis.

    The rotation follows the right-hand rule.
    The input angle should be in radians.

    Parameters
    ----------
    theta: float
        Rotation angle [rad]
    
    Returns
    -------
    np.ndarray
        A 3x3 rotation matrix
    """
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([
        [c, -s, 0.0],
        [s, c, 0.0],
        [0.0, 0.0, 1.0],
    ])


def make_transform(R: np.ndarray, p: np.ndarray) -> np.ndarray:
    """
    Create a homogeneous transformation matrix from rotation and translation.

    A homogeneous transformation matrix has the form:
        T = [R p]
            [0 1]
    where R in 3x3 rotation matrix and p is a 3D translation vector.

    Parameters
    ----------
    R: np.ndarray
        a 3x3 rotation matrix
    p: np.ndarray
        a 3x1 translation vector
    
    Returns
    -------
    np.ndarray
        A 4x4 homogeneous transformation matrix

    Raises
    ------
    ValueError
        If R does not have shape 3x3.
    """
    R = np.asarray(R, dtype=float)
    p = np.asarray(p, dtype=float).reshape(3)

    if R.shape != (3, 3):
        raise ValueError("R must have shape (3, 3).")

    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = p
    return T


def inverse_transform(T: np.ndarray) -> np.ndarray:
    """
    Invert a hmogeneous transformation matrix

    For a transformation matrix
        T = [R p]
            [0 1]
    the inverse is 
        T_inv = [R.inv -R.T@p]
                [ 0      1   ]
    The is more efficient and numerically clearer
    matrix inverse.

    Parameters
    ----------
    T: np.ndarray
        A 4x4 homogeneous transformation matrix

    Returns
    -------
    np.ndarray
        The inverse 4x4 homogenous transformation matrix
    
    Raises
    ------
    ValueError
        If T does not have shape 4x4.
    """
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
    """
    Transform a 3D point using homogeneous transformation matrix.
    
    The input point is converted to homogeneous coordinates by appending 1 as:
        point_h = [x, y, z, 1]
    
    The transformed point is then computed as:
        transformed_point = T @ point_h
    
    Parameters
    ----------
    T: np.ndarray
        A 4x4 homogeneous transformation matrix
    point: np.ndarray
        A point in 3D space
    
    Returns
    -------
    np.ndarray
        The transformed 3D point
    
    Raises
    ------
    ValueError
        If T does not have shape 4x4.
    """
    T = np.asarray(T, dtype=float)

    if T.shape != (4,4):
        raise ValueError("T must have shape (4,4).")
    
    point = np.asarray(point, dtype=float).reshape(3)
    point_h = np.array([point[0], point[1], point[2], 1.0])
    transformed = T @ point_h
    return transformed[:3]