class Page:
    def __init__(self, page, total_events):
        self.page = page
        self.total_events = int(total_events)

    def __str__(self):
        return self.page

    def increment(self):
        return self.page+1

    def decrement(self):
        return self.page-1

    def max_page(self):
        return (self.total_events//50)+1
