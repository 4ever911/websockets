import trollius


try:
    trollius_ensure_future = trollius.ensure_future
except AttributeError:
    trollius_ensure_future = trollius.async
