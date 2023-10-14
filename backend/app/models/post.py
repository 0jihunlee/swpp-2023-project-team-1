import uuid
from pydantic import UUID4
from app.models import Base
from app.models.comment import Comment
from app.models.post_like import PostLike
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.guid import GUID

class Post(Base):
    id: Mapped[UUID4] = mapped_column(GUID, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[UUID4] = mapped_column(GUID, ForeignKey("user.id"), nullable=False, unique=True, default=uuid.uuid4)
    
    content: Mapped[str] = mapped_column(String(500), nullable=True)
    profile_image_url: Mapped[str] = mapped_column(String(100), nullable=True)

    comments = relationship(Comment, back_populates="post")
    likes = relationship(PostLike, back_populates="post")

    class Config:
        orm_mode = True
