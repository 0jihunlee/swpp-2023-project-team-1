from pydantic import UUID4, BaseModel, ConfigDict, Field



class UserBase(BaseModel):
    email: str = Field(..., description="Email")



class UserCreate(UserBase):
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")

    def create_dict(self) -> dict:
        return self.model_dump(exclude_unset=True)



class UserRead(UserBase):
    id: UUID4 = Field(..., description="User Id")
    username: str = Field(..., description="Username")
    bio: str | None = Field(None, description="Bio")
    profile_image_url: str | None= Field(None, description="Profile Image Url")

    model_config = ConfigDict(
        from_attributes=True,
    )



class UserUpdate(BaseModel):
    username: str | None = Field(None, description="Username")
    bio: str | None = Field(None, description="Bio")
    profile_image_url: str | None = Field(None, description="Profile Image Url")

    def update_dict(self) -> dict:
        return self.model_dump(exclude_unset=True)




class LoginRequest(UserBase):
    password: str = Field(..., description="Password")



class LoginResponse(BaseModel):
    access_token: str = Field(..., description="Token")
    refresh_token: str = Field(..., description="Refresh Token")
    user_id: UUID4 = Field(..., description="User Id")
    username: str = Field(..., description="Username")



class CheckUserInfoResponse(BaseModel):
    email_exists: bool | None = None
    username_exists: bool | None = None

class FollowBase(BaseModel):
    following_user_id: UUID4 = Field(..., description="Following User Id")
    followed_user_id: UUID4 = Field(..., description="Followed User Id")
    accept_status: int = Field(..., description="Follow Accept Status")

class GetFollowInfoResponse(BaseModel):
    follower_cnt: int = Field(..., description="Number of Followers")
    following_cnt: UUID4 = Field(..., description="Number of Followings")
    is_follower: bool = Field(..., description="Is My Follower")
    is_following: bool = Field(..., description="Is My Following")

class GetUsersResponse(BaseModel):
    total: int
    items: list[UserRead]
    next_cursor: int | None

class UserSearch(UserRead):
    is_following: bool = Field(..., description="Following Status")
    is_follower: bool = Field(..., description="Follower Status")

class UserSearchResponse(BaseModel):
    total: int
    items: list[UserSearch]
    next_cursor: int | None