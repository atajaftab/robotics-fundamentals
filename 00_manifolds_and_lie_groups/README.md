# 00 - Manifolds and Lie groups

## Goal

This part provides a visual and intuitive introduction to differentiable manifolds
and Lie groups in the context of robotics.

The motivation is to understand that rotation matrices are not just arbitrary matrices.
They must satisfy special constraints, and the set of all valid rotation matrices
forms a structured space.
In robotics, these spaces are examples of Lie groups.

## Background

A differentiable manifold is a space that may be curved globally,
but locally behaves like ordinary Euclidean space.

For example, a circle is not globally the same as a straight line.
However, if we zoom in on a small part of the circle, it locally looks like a one-dimensional line.
Similarly, a sphere is a curved two-dimensional surface, but a small neighborhood on the sphere locally
looks like a flat two-dimensional plane.

This local Euclidean structure makes it possible to use calculus on curved spaces.

## Why this matters in robotics

Rotation matrices in 2D and 3D belong to special matrix groups:

$$
SO(2) = \{R \in \mathbb{R}^{2 \times 2} \mid R^T R = I,\ \det(T)=1 \}
$$

$$
SO(3) = \{R \in \mathbb{R}^{3 \times 3} \mid R^T R = I,\ \det(T)=1 \}
$$

These sets are not ordinary vector spaces.
For example, adding two rotation matrices does not generally produce another valid rotation matrix.

Instead, rotations form Lie groups: spaces that are both groups and differentiable manifolds.

This is important because robot motion, orientation interpolation,
angular velocity, and rigid-body transformations all rely on moving smoothly on these curved spaces.