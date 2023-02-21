import dataFrameBasics.DfBasics

class SparkObject:


class InitialiseObject(SparkObject):

    def __init__(self, class_name):
        self.obj = class_name

    @classmethod
    def get_object(cls, class_name):
        if class_name == "DfBasics":
            obj = class_name()

        return obj
