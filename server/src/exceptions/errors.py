class AppError(Exception):
  """Base application exception."""


class ResourceNotFoundError(AppError):
  """Raised when a requested resource does not exist."""

  def __init__(self, resource: str, identifier: str):
    self.resource = resource
    self.identifier = identifier
    super().__init__(f"{resource} '{identifier}' not found")
