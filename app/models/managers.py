from .configs import default_session


session = default_session()


class BaseManager:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return "<%s()>" % (self.__class__.__name__,)

    @classmethod
    def create_instance(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        session.add(instance)
        if commit:
            session.commit()

    @classmethod
    def filter_first(cls, **kwargs):
        return session.query(cls).filter(**kwargs).first()
