"""Module for Value Objects

- It represents a value that doesn't have identity and is immutable.

- Value objects also provide context

- We can centralize the type definition and validation on the Value Object definition.
"""

import uuid

PostId = uuid.UUID
# UserId = uuid.UUID