class Subscription():
    def __init__(self, id, follower_id, author_id, created_on, ended_on = "NULL"):
        self.id = id
        self.followerId = follower_id
        self.authorId = author_id
        self.createdOn = created_on
        self.endedOn = ended_on