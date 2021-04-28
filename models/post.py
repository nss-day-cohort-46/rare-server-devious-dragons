from datetime import date

class Post():
    def __init__(self, id, user_id, category_id, title, publication_date, image_url, content, approved):
        self.id = id
        self.userId = user_id
        self.title = title
        self.content = content
        self.publicationDate = publication_date
        self.categoryId = category_id
        self.imageUrl = image_url
        self.approved = approved