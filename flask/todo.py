class Todo:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.completed = False

    # TODO: This feel like a hack, I shouldn't need to make this method if I knew what I was doing
    def toObj(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
