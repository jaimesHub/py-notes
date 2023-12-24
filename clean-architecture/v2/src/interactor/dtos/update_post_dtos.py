""" Module for UpdatePost Dtos
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from src.domain.entities.post import Post
from typing import Optional
from src.domain.value_objects import PostId

@dataclass
class UpdatePostInputDto:
    """Input Dto for Update Post
    """
    id: PostId
    title: Optional[str]
    description: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    def to_dict(self):
        """Convert data into dictionary
        """
        return asdict(self)
    
@dataclass
class UpdatePostOutputDto:
    """Output DTO for Create Post
    """
    post: Post