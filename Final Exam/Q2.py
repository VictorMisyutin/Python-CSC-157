class book:
    def __init__(self, title, authorName, publisherName):
        self.title = title
        self.authorName = authorName
        self.publisherName = publisherName
    
    def getTitle(self):
        return self.title
    
    def getAuthorName(self):
        return self.authorName
    
    def getPublisherName(self):
        return self.publisherName
    
    def setTitle(self, title):
        self.title = title
    
    def setAuthorName(self, authorName):
        self.authorName = authorName

    def setPublisherName(self, publisherName):
        self.publisherName = publisherName

    def __str__(self):
        return(f"{self.title} was written by {self.authorName} and published by {self.publisherName}.")
    
