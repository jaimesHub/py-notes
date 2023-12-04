class Comment:
    def __init__(self, username, text, likes = 0) -> None:
        self.username = username
        self.text = text
        self.likes = likes

comment1 = Comment("davey123", "lol you're so silly", 3)
comment2 = Comment("rosa77", "so cuteee!")