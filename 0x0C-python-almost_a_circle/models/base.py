class Base:
    """Base class for managing id attribute in all future classes."""
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """Class constructor."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
