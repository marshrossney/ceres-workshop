from functools import wraps

from flake8.api import legacy as flake8

__all__ = ["lint"]


def verbose(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        fname = func.__name__.replace("_", " ").replace("grade", "test").capitalize()
        fname = "    " + fname
        banner = "".join(["=" for _ in fname])
        header = f"{banner}\n{fname}\n{banner}"
        print()
        print(header)
        print(func.__doc__)
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            print("    > Failed!")
            raise exc
        else:
            print("    > Passed!")

    return wrapper

def lint(*targets):
    style = flake8.get_style_guide()
    report = style.check_files(targets)
    errors = report.get_statistics("E")
    return errors
