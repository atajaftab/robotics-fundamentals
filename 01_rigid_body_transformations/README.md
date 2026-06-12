# 01 — Rigid-Body Transformations

## Goal

This project implements basic tools for constructing, inverting, composing,
and visualizing rigid-body transformations.

These operations are fundamental in robotics because robots often have to involve
several coordinate frames, such as world, robot base, tool, camera, and object frames.


## Background

A common way to describe the position and orientation of a rigid body is to attach a coordinate
frame to the body.
The pose of this body-fixed frame can then be described relative to a fixed reference frame.

In robotics, this pose (position and orientation) is commonly represented by a
4x4 matrix called homogeneous transformation matrix:

$$
T = \begin{bmatrix}
R & p \\
0 & 1
\end{bmatrix}
$$

where $R$ is a rotation matrix describing the orientation of the body frame,
and $p$ is a position vector describing the origin of the body frame relative to the reference frame.

A homogeneous transformation matrix has several interpretations.
It can represent the configuration of a frame, but it can also be used to transform points,
vectors, and frames.
In particular, it can be used to:
1. rotate and translate a point or frame, and
2. change the coordinate representation of a point or frame from one reference frame to another.

Strictly speaking, translation affects points and frames,
while free vectors are affected by rotation only.


This project implements basic tools for constructing, inverting, composing, and visualizing such transformations.

## Implemented functionality

The source code implements:

- rotation matrices about the x-, y-, and z-axes,
- construction of homogeneous transformation matrices,
- inversion of homogeneous transformation matrices,
- point transformation,
- free-vector transformation,
- rotation-matrix validation.

## Demo 1: Construction of a homogeneous transformation matrix

This demo shows how a rigid-body pose can be represented by
combining a rotation matrix and a translation vector
into one homogeneous transformation matrix.

A rotation matrix $R$ describes the orientation of one coordinate frame relative to another.
A translation vector $p$ describes the position of the origin of that frame
relative to the reference frame.

Together, they form the homogeneous transformation matrix:

$$
T =
\begin{bmatrix}
R & p \\
0 & 1
\end{bmatrix}
$$

In this representation, the upper-left block contains the rotation matrix, and the upper-right column contains the translation vector.

In the implementation, this operation is performed by the function:

```python
make_transform(R, p)
```

The purpose of this demo is to show how separate rotation and translation components
can be stored in a single matrix.
This matrix can then be used for coordinate transformations,
transformation chains, and inverse transformations in the later demos.

## Demo 2: Transformation chain

This demo shows how multiple homogeneous transformation matrices
can be composed to describe a chain of coordinate frames.

The example uses the following frame chain:

    world -> robot_base -> tool -> camera

Each relative pose is represented by one homogeneous transformation matrix:

$$
T_{\text{world,base}}, \quad
T_{\text{base,tool}}, \quad
T_{\text{tool,camera}}
$$

The final camera pose in the world frame is obtained by multiplying
the transformations in the correct order:

$$
T_{\text{world,camera}}
=
T_{\text{world,base}}
T_{\text{base,tool}}
T_{\text{tool,camera}}
$$

This type of transformation chain is common in robot vision and inspection tasks,
where robot base, tool, camera, and object frames must be handled consistently.

## Demo 3: Point transformation vs. vector transformation

This demo shows the difference between transforming a point and transforming a free vector.

A point has a fixed location in space.
Therefore, transforming a point applies both rotation and translation:

$$
p' = Rp + t
$$

A free vector represents a direction and magnitude,
but not a fixed location. Therefore, transforming a free vector applies only the rotation:

$$
v' = Rv
$$

This distinction is important in robotics.
For example, the origin of a camera frame is transformed as a point,
while a surface normal, velocity direction, or optical axis is transformed as a vector.

Rotation also matters for a point when the point is expressed in a local or moving frame. For example, if a point is given as

$$
p_{\text{local}} =
\begin{bmatrix}
1 \\
0 \\
0
\end{bmatrix}
$$

this means that the point is located one unit along the local x-axis of that frame.
If the local frame is rotated relative to the world frame,
then the local x-axis does not point in the same direction as the world x-axis.

To express the point in the world frame, both rotation and translation are needed:

$$
p_{\text{world}} = R p_{\text{local}} + t
$$

Here, $R p_{\text{local}}$ describes the local offset expressed in world directions,
and $t$ describes the position of the local frame origin in the world frame.

If the point is exactly at the local frame origin,

$$
p_{\text{local}} =
\begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$

then the rotation has no effect:

$$
p_{\text{world}} = R0 + t = t
$$

Therefore, translation alone is enough only for the origin of the local frame.
For any other point attached to the local frame, rotation also matters.

## Demo 4: Inverse transformation

This demo shows how the inverse of a homogeneous transformation
maps coordinates in the opposite direction.

If a transformation maps a point from a local frame to the world frame,

$$
p_{\text{world}} = T_{\text{world,local}} p_{\text{local}}
$$

then the inverse transformation maps the point from the world frame back to the local frame:

$$
p_{\text{local}} = T_{\text{world,local}}^{-1} p_{\text{world}}
$$

For a homogeneous transformation matrix

$$
T =
\begin{bmatrix}
R & p \\
0 & 1
\end{bmatrix}
$$

the inverse is

$$
T^{-1} =
\begin{bmatrix}
R^T & -R^T p \\
0 & 1
\end{bmatrix}
$$

The demo transforms a point from a tool frame to the world frame and then uses the inverse
transformation to recover the original point in the tool frame.
The recovered point should match the original point up to numerical precision.

## Why this matters

Rigid-body transformations are one of the most important building blocks in robotics.
They are used to connect robot base frames, tool frames, camera frames,
object frames, sensor frames, and world frames.

Errors in transformation chains can lead to incorrect robot poses,
wrong camera-object alignment, failed calibration, or incorrect inspection trajectories.
Therefore, this project focuses on implementing the basic operations
explicitly and visualizing their effects.

These concepts are also the basis for the next project: forward kinematics and Jacobians.