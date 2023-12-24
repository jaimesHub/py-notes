"""This module has definition of the Post entity
"""

from dataclasses import dataclass, asdict
from src.domain.value_objects import PostId
from datetime import datetime

@dataclass
class Post:
    """Definition of the Post entity
    """
    id: PostId
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, data):
        """Convert data from a dictionary
        """

        return cls(**data)
    
    def to_dict(self):
        """Instance method
        Convert data into a dictionary
        """
        return asdict(self)