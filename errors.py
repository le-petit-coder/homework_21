

class BaseError(Exception):
    message = "Something went wrong"


class NotEnoughSpaceError(BaseError):
    message = "Not enough space"


class NotEnoughProductError(BaseError):
    message = "Not enough product"


class ProductUnknownError(BaseError):
    message = "Product unknown"


class TooManyDifferentProductsError(BaseError):
    message = "Too many different products"


class WrongRequest(BaseError):
    message = "Wrong request"


class UnknownStorage(BaseError):
    message = "Unknown storage"
