"""Citation API resource."""

from typing import Dict

from gramps.gen.lib import Citation

from .base import (
    GrampsObjectProtectedResource,
    GrampsObjectResourceHelper,
    GrampsObjectsProtectedResource,
)
from .util import get_extended_attributes, get_source_by_handle


class CitationResourceHelper(GrampsObjectResourceHelper):
    """Citation resource helper."""

    gramps_class_name = "Citation"

    def object_extend(self, obj: Citation, args: Dict) -> Citation:
        """Extend citation attributes as needed."""
        if args["extend"]:
            db_handle = self.db_handle
            obj.extended = get_extended_attributes(db_handle, obj)
            obj.extended["source"] = get_source_by_handle(db_handle, obj.source_handle)
        return obj


class CitationResource(GrampsObjectProtectedResource, CitationResourceHelper):
    """Citation resource."""


class CitationsResource(GrampsObjectsProtectedResource, CitationResourceHelper):
    """Citations resource."""