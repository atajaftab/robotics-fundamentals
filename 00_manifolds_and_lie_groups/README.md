# 00 - Manifolds and Lie groups

## Goal

The goal of this project is to understand why rotation matrices and rigid-body
transformations are not ordinary vectors,
but elements of structured spaces called manifolds and Lie groups.

## Core idea

A manifold is a space that may be curved or constrained globally,
but locally looks like Euclidean space.

The dimension of a manifold is the number of independent local coordinates
needed to describe a point on it,
not necessarily the dimension of the space in which it is embedded.

For example, the surface of a sphere is embedded in three-dimensional space,
but it is a two-dimensional manifold because a local point on the surface can be described using two independent coordinates.

## Why this matters for robotics

Rotation matrices in 3D belong to the special orthogonal group:

$$
SO(3) = \{R \in \mathbb{R}^{3 \times 3} \mid R^T R = I,\ \det(R)=1\}
$$

Although a 3D rotation matrix has nine entries, these entries are constrained.
The space of valid 3D rotations has only three degrees of freedom.

Therefore, rotations should not be treated as arbitrary matrices or vectors.
Instead, small changes in rotation are often represented in a local tangent space
and mapped back to the rotation group using the exponential map.

## Planned demonstrations

1. **Embedding dimension vs. intrinsic dimension**  
   Show that an object can live in a higher-dimensional space while requiring fewer independent coordinates to describe motion on it.

2. **Sphere surface as a 2D manifold embedded in 3D**  
   Show that points constrained to the surface of a sphere need only two local coordinates, even though the sphere is embedded in three-dimensional space.

3. **Rotation matrices are constrained objects**  
   Show that adding two valid rotation matrices does not generally produce another valid rotation matrix, while multiplying/composing them does.

4. **Local updates on SO(3) using the exponential map**  
   Show that small rotation vectors in a local tangent space can be mapped back to valid rotation matrices using the exponential map.

Together, these demonstrations connect the abstract idea of differentiable manifolds
to a practical robotics problem: representing and updating orientations without leaving the space of valid rotations.