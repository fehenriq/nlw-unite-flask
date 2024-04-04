from uuid import uuid4

import pytest

from src.models.settings.connection import db_connection_handler

from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()


def test_insert_attendee():
    attendee = {
        "uuid": str(uuid4()),
        "name": "Felipe",
        "email": "fehenriq.dev@gmail.com",
        "event_id": "c054b2ef-1409-4c69-99cc-441019e515a8",
    }

    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendee)

    print(response)


def test_get_attendee_badge_by_id():
    attendee_id = "899fac9a-a2a0-4330-80a8-4783ed6abd8a"
    events_repository = AttendeesRepository()
    response = events_repository.get_attendee_badge_by_id(attendee_id)

    print(response)
