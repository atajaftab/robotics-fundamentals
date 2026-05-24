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

This project implements basic tools for constructing, inverting, composing, and visualizing such transformations.

## First demo: transformation chain

The first demo creates a simple transformation chain:

```text
world -> robot base -> tool -> camera
```

Each relative pose is represented as a homogeneous transformation matrix.
The final camera pose in the world frame is obtained by composing the transformations:

$$
T_{\text{world,camera}} = T_{\text{world,base}} T_{\text{base,tool}} T_{\text{tool,camera}}
$$