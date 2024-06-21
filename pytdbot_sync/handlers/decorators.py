import logging
import pytdbot_sync

from typing import Callable
from asyncio import iscoroutinefunction
from .handler import Handler
from .updates import Updates

logger = logging.getLogger(__name__)


class Decorators(Updates):
    """Decorators class."""

    def initializer(
        self: "pytdbot_sync.Client" = None,
        filters: "pytdbot_sync.filters.Filter" = None,
        position: int = None,
    ) -> None:
        """A decorator to initialize an event object before running other handlers

        Args:
            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in initializers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot_sync.Client):
                if iscoroutinefunction(func):
                    self.add_handler("initializer", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot_sync.filters.Filter):
                func._handler = Handler(func, "initializer", self, position)
            else:
                func._handler = Handler(func, "initializer", filters, position)

            return func

        return decorator

    def finalizer(
        self: "pytdbot_sync.Client" = None,
        filters: "pytdbot_sync.filters.Filter" = None,
        position: int = None,
    ) -> None:
        """A decorator to finalize an event object after running all handlers

        Args:
            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in finalizers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot_sync.Client):
                if iscoroutinefunction(func):
                    self.add_handler("finalizer", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot_sync.filters.Filter):
                func._handler = Handler(func, "finalizer", self, position)
            else:
                func._handler = Handler(func, "finalizer", filters, position)
            return func

        return decorator
