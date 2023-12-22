""" Module for CreatePost Dtos
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from src.domain.entities.post import Post

@dataclass
class CreatePostInputDto:
    """Input Dto for Create Post
    """
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    def to_dict(self):
        """Convert data into dictionary
        """
        return asdict(self)
    
@dataclass
class CreatePostOutputDto:
    """Output DTO for Create Post
    """
    post: Post