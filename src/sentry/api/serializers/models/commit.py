from __future__ import absolute_import

from sentry.api.serializers import Serializer, register
from sentry.models import Commit


@register(Commit)
class CommitSerializer(Serializer):
    def serialize(self, obj, attrs, user):
        return {
            'id': obj.key,
            'shortId': obj.short_id,
            'message': obj.message,
            'title': obj.title,
            'author': {
                'name': obj.author.name,
                'email': obj.author.email,
            } if obj.author else None,
            'dateCreated': obj.date_added,
        }
